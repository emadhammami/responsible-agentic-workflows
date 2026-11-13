"""Native-size, vector execution/resource figures from audited companion CSVs."""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/execution-figures-v1-mplconfig')
os.environ.setdefault('MPLBACKEND','Agg')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text
from matplotlib.ticker import FuncFormatter,MaxNLocator
import numpy as np
import json,statistics,collections,math
from common import *

COLORS={'B0':'#777777','B1':'#0072B2','G1':'#D55E00'}
MARKERS={'B0':'o','B1':'s','G1':'^'}
HATCHES={'B0':'..','B1':'///','G1':'\\\\'}
SIZE_WIDTH={'single_column':3.5,'full_width':7.1}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.labelsize':8.5,
 'axes.titlesize':9,'axes.titleweight':'semibold','xtick.labelsize':7.5,'ytick.labelsize':7.5,
 'legend.fontsize':7.5,'axes.linewidth':.65,'lines.linewidth':1.1,'patch.linewidth':.65,
 'pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'none','svg.hashsalt':'primary-execution-v1',
 'savefig.facecolor':'white','figure.facecolor':'white','axes.spines.top':False,
 'axes.spines.right':False,'axes.grid':False,'axes.formatter.useoffset':False,
 'xtick.major.width':.6,'ytick.major.width':.6})
formatter=FuncFormatter(lambda x,pos:f'{x:,.0f}' if math.isclose(x,round(x),rel_tol=0,abs_tol=1e-9) else f'{x:,.6g}')
layout_records=[]
manifest={'package':'execution_figures_v1','analysis_scope':'execution and resource telemetry only',
 'source_runs':270,'primary_comparison':'B1 vs G1','supporting_reference':'B0',
 'paired_task_aggregation':'arithmetic mean of 3 repetitions, then G1 - B1 by task',
 'paired_tasks':30,'paired_tasks_per_UC':10,'scoring_results_used':False,'expert_results_used':False,
 'uncertainty':'none inferential; boxes are descriptive quartiles/1.5 IQR whiskers',
 'font':'DejaVu Sans','minimum_font_pt':7.5,'pdf_fonts':'embedded TrueType (fonttype=42)',
 'SVG_text':'editable text; DejaVu Sans font specified','PNG_DPI':600,'figures':[]}
freeze=json.loads((ROOT/'primary_benchmark_raw_freeze_manifest.json').read_text())
manifest['authoritative_sources']={'raw_records':str(ROOT/'run_records'),
 'raw_bundle_sha256':freeze['raw_record_bundle_sha256'],
 'execution_order_sha256':freeze['execution_order']['sha256'],
 'record_inventory_sha256':freeze['record_hash_inventory']['sha256'],
 'execution_code_revision':freeze['final_execution_code_revision']}

def clean(ax,numeric='y',integer=False,zero=True):
 ax.tick_params(length=3,pad=2)
 if numeric=='y':
  if zero:ax.set_ylim(bottom=0)
  low,high=ax.get_ylim()
  ax.set_yticks([tick for tick in MaxNLocator(nbins=4,integer=integer).tick_values(low,high) if low<=tick<=high])
  ax.yaxis.set_major_formatter(formatter)
 else:
  if zero:ax.set_xlim(left=0)
  low,high=ax.get_xlim()
  ax.set_xticks([tick for tick in MaxNLocator(nbins=4,integer=integer).tick_values(low,high) if low<=tick<=high])
  ax.xaxis.set_major_formatter(formatter)

def grid(size,panels,heights):
 nrows,ncols=(panels,1) if size=='single_column' else (math.ceil(panels/2),2)
 fig,axes=plt.subplots(nrows,ncols,figsize=(SIZE_WIDTH[size],heights[size]),layout='constrained',squeeze=False)
 fig.get_layout_engine().set(w_pad=.045,h_pad=.045,wspace=.08,hspace=.10)
 return fig,list(axes.flat)

def mean_median_legend(fig):
 fig.legend(handles=[Line2D([],[],marker='D',markersize=4,color='black',linestyle='none',label='Mean'),
                     Line2D([],[],color='black',linewidth=1.2,label='Median')],
            loc='outside lower center',ncol=2,frameon=False,columnspacing=1.8,handlelength=1.2)

def dot_offsets(n,span=.18):
 # Deterministic categorical-axis jitter only; numeric values never jittered.
 return np.array([(((i*.6180339887498949)%1)-.5)*2*span for i in range(n)])

def distributions(ax,groups,conds,labels=None,integer=False):
 for index,(values,cond) in enumerate(zip(groups,conds),1):
  values=np.asarray(values,float)
  result=ax.boxplot([values],positions=[index],widths=.5,showfliers=False,patch_artist=True,
      medianprops={'color':'black','linewidth':1.15},whiskerprops={'color':'#333333'},capprops={'color':'#333333'})
  result['boxes'][0].set(facecolor='white',edgecolor=COLORS[cond],hatch=HATCHES[cond],alpha=.55)
  ax.scatter(index+dot_offsets(len(values)),values,s=8 if len(values)<=30 else 5,
    marker=MARKERS[cond],facecolors=COLORS[cond],edgecolors='black',linewidths=.18,alpha=.75,zorder=3)
  ax.scatter(index+.28,mean(values.tolist()),marker='D',s=17,color='black',zorder=5)
 ax.set_xticks(range(1,len(conds)+1),labels or conds)
 ax.set_xlim(.5,len(conds)+.55)
 ax.set_ylim(0,max(max(values) for values in groups)*1.12 if any(max(v)>0 for v in groups) else 1)
 clean(ax,integer=integer)

def pair_limits(values):
 radius=max(abs(v) for v in values)
 return (-radius*1.15,radius*1.15) if radius else (-1,1)

def swarm_offsets(values,increment=.08):
 # Only equality groups are stacked; no numeric-axis perturbation.
 groups=collections.defaultdict(list)
 for i,value in enumerate(values):groups[float(value)].append(i)
 offsets=np.zeros(len(values))
 for indices in groups.values():
  shifts=(np.arange(len(indices))-(len(indices)-1)/2)*increment
  for idx,shift in zip(indices,shifts):offsets[idx]=shift
 return offsets

def paired_overall(ax,values):
 ax.axvline(0,color='#222222',ls='--',lw=.9,zorder=0)
 offsets=swarm_offsets(values)
 ax.scatter(values,offsets,s=16,color='#484848',edgecolor='black',linewidth=.3,zorder=3)
 top=max(abs(offsets).max(),.15)+.6
 ax.boxplot([values],positions=[top],widths=.25,orientation='horizontal',showfliers=False,
     patch_artist=True,boxprops={'facecolor':'white','edgecolor':'black'},medianprops={'color':'black','linewidth':1.2})
 ax.scatter(mean(values),top,marker='D',s=20,color='black',zorder=4)
 ax.set_xlim(*pair_limits(values));ax.set_ylim(-max(abs(offsets).max(),.2)-.25,top+.35)
 ax.set_yticks([0,top],['Tasks','Summary']);ax.spines['left'].set_visible(False)
 ax.tick_params(axis='y',length=0)
 clean(ax,numeric='x',zero=False)

def export(fig,stem,size,title,csv_name,analysis_unit,note):
 fig.canvas.draw();renderer=fig.canvas.get_renderer();canvas=fig.bbox
 texts=[t for t in fig.findobj(Text) if t.get_visible() and t.get_text() and t.get_alpha()!=0]
 text_fail=[]
 for text in texts:
  b=text.get_window_extent(renderer)
  if text.get_fontsize()<7.5-1e-8:text_fail.append('font below 7.5 pt: '+text.get_text())
  if b.x0<-.5 or b.y0<-.5 or b.x1>canvas.x1+.5 or b.y1>canvas.y1+.5:
   text_fail.append('text outside canvas: '+text.get_text())
 # Numeric tick labels must preserve tick coordinates; fractional call/delta
 # ticks may not be rounded to misleading integer labels.
 import re
 for ax in fig.axes:
  for axis in [ax.xaxis,ax.yaxis]:
   for tick in axis.get_major_ticks():
    label=tick.label1.get_text().replace(',','').replace('−','-')
    if re.fullmatch(r'-?\d+(?:\.\d+)?',label):
     assert math.isclose(float(label),tick.get_loc(),rel_tol=0,abs_tol=1e-8),f'Numeric tick value changed: {label}'
 bounds=[ax.get_tightbbox(renderer) for ax in fig.axes if ax.get_visible()]
 overlaps=[]
 for i,a in enumerate(bounds):
  for j,b in enumerate(bounds[i+1:],i+1):
   if min(a.x1,b.x1)-max(a.x0,b.x0)>1 and min(a.y1,b.y1)-max(a.y0,b.y0)>1:overlaps.append([i,j])
 assert not text_fail,f'{stem}/{size}: {text_fail}'
 assert not overlaps,f'{stem}/{size}: overlapping panels {overlaps}'
 assert all(not artist.get_rasterized() for ax in fig.axes for artist in ax.collections)
 base=f'{stem}_{size}'
 files={ext:f'figures/{ext}/{base}.{ext}' for ext in ['pdf','svg','png']}
 fig.savefig(OUT/files['pdf'],metadata={'Title':title,'Creator':'Matplotlib execution-only benchmark figure pipeline','CreationDate':None,'ModDate':None})
 fig.savefig(OUT/files['svg'],metadata={'Title':title,'Date':None,'Creator':'Matplotlib execution-only benchmark figure pipeline'})
 fig.savefig(OUT/files['png'],dpi=600,metadata={'Title':title,'Description':note})
 fig.savefig(OUT/'previews'/f'{base}.png',dpi=160)
 # Direct grayscale preview tests the condition marker/hatch/line encodings.
 from PIL import Image
 with Image.open(OUT/'previews'/f'{base}.png') as im:im.convert('L').save(OUT/'previews'/f'{base}_grayscale.png')
 row={'stem':stem,'size':size,'width_inches':fig.get_figwidth(),'height_inches':fig.get_figheight(),
      'minimum_font_pt':min(t.get_fontsize() for t in texts),'unclipped_texts':len(texts),'panel_overlap_count':0,
      'files':files,'companion_csv':'data/'+csv_name,'analysis_unit':analysis_unit,'title':title}
 row['additional_companion_csvs']={'figure01_overall_resource_profile':['data/figure01_call_frequency_counts.csv'],
   'figure04_control_behavior':['data/figure04_control_behavior_runs.csv']}.get(stem,[])
 manifest['figures'].append(row);layout_records.append({k:row[k] for k in ['stem','size','width_inches','height_inches','minimum_font_pt','unclipped_texts','panel_overlap_count']})
 plt.close(fig)
 print('EXPORTED '+base,flush=True)

def fig01(size):
 data=read_csv('figure01_overall_resource_profile.csv')
 frequencies=read_csv('figure01_call_frequency_counts.csv')
 fig,axes=grid(size,4,{'single_column':8.1,'full_width':4.7})
 for i,(ax,metric,label) in enumerate(zip(axes,CORE,CORE_LABELS)):
  groups=[[float(r[metric]) for r in data if r['condition']==c] for c in CONDITIONS]
  assert all(len(v)==90 for v in groups)
  distributions(ax,groups,CONDITIONS,labels=[c+'\n(n=90)' for c in CONDITIONS],integer=metric.endswith('calls'))
  if metric.endswith('calls'):
   for position,condition in enumerate(CONDITIONS,1):
    for row in frequencies:
     if row['condition']==condition and row['metric']==metric:
      ax.text(position,float(row['call_count'])+ax.get_ylim()[1]*.034,'n='+row['run_frequency'],
        ha='center',va='bottom',fontsize=7.5,zorder=6,bbox={'facecolor':'white','edgecolor':'none','pad':.2})
  ax.set_title(f'({"abcd"[i]}) {label}',loc='left');ax.set_ylabel(label)
 mean_median_legend(fig)
 export(fig,'figure01_overall_resource_profile',size,'Overall execution resource profile','figure01_overall_resource_profile.csv',
  '270 raw executions; 90 per condition, descriptive only','B0 supporting; B1/G1 primary; raw executions with box distributions, mean diamonds and medians.')

def fig02(size):
 data=read_csv('figure02_b1_g1_paired_differences.csv');assert len(data)==30
 fig,axes=grid(size,4,{'single_column':7.6,'full_width':4.6})
 for i,(ax,metric,label) in enumerate(zip(axes,CORE,CORE_LABELS)):
  values=[float(r[metric+'_difference']) for r in data]
  paired_overall(ax,values);ax.set_title(f'({"abcd"[i]}) {label}',loc='left')
  ax.set_xlabel('G1 − B1'+(' (ms)' if metric=='end_to_end_ms' else ' (calls)' if metric.endswith('calls') else ' (tokens)'))
 mean_median_legend(fig)
 export(fig,'figure02_b1_g1_paired_differences',size,'Primary paired execution resource differences','figure02_b1_g1_paired_differences.csv',
  '30 paired tasks; arithmetic mean of 3 repetitions per condition','Negative: G1 uses less resource/time; positive: G1 uses more. Zero reference; no inference.')

def fig03(size):
 data=read_csv('figure03_use_case_resource.csv')
 fig,axes=grid(size,4,{'single_column':7.7,'full_width':4.8})
 for i,(ax,metric,label) in enumerate(zip(axes,CORE,CORE_LABELS)):
  all_values=[float(r[metric+'_difference']) for r in data]
  ax.axvline(0,color='#222222',ls='--',lw=.9,zorder=0)
  for index,(uc,marker) in enumerate(zip(UCS,['o','s','^'])):
   values=[float(r[metric+'_difference']) for r in data if r['UC']==uc];assert len(values)==10
   ax.boxplot([values],positions=[index],widths=.35,orientation='horizontal',showfliers=False,
     patch_artist=True,boxprops={'facecolor':'white','edgecolor':'#555555'},medianprops={'color':'black'})
   ax.scatter(values,index+swarm_offsets(values,increment=.05),marker=marker,s=17,color='#484848',edgecolor='black',linewidth=.3,zorder=3)
   ax.scatter(mean(values),index+.28,marker='D',s=18,color='black',zorder=4)
  ax.set_yticks([0,1,2],UCS);ax.set_ylim(2.6,-.5);ax.set_xlim(*pair_limits(all_values))
  ax.set_title(f'({"abcd"[i]}) {label}',loc='left')
  ax.set_xlabel('G1 − B1'+(' (ms)' if metric=='end_to_end_ms' else ' (calls)' if metric.endswith('calls') else ' (tokens)'))
  clean(ax,numeric='x',zero=False)
 mean_median_legend(fig)
 export(fig,'figure03_use_case_resource',size,'Paired execution resources by use case','figure03_use_case_resource.csv',
  '10 paired tasks per UC; arithmetic mean of 3 repetitions per condition','Same resource-difference scale across use cases within each panel; negative favors G1 resource use.')

def fig04(size):
 data=read_csv('figure04_control_behavior_runs.csv')
 plotted=read_csv('figure04_control_behavior.csv')
 width=SIZE_WIDTH[size]
 if size=='single_column':
  fig,axs=plt.subplots(3,1,figsize=(width,8.1),layout='constrained',gridspec_kw={'height_ratios':[1.3,1.15,1]});a,b,c=axs
 else:
  fig=plt.figure(figsize=(width,5.1),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[1.35,1]);a=fig.add_subplot(gs[0,0]);b=fig.add_subplot(gs[0,1]);c=fig.add_subplot(gs[1,:])
 fig.get_layout_engine().set(w_pad=.045,h_pad=.06,wspace=.14,hspace=.12)
 incidence=[('recovery_attempt_count','Recovery starts'),('recovery_retrieval_count','Re-retrieval'),
            ('pre_recovery_abstention','Pre-recovery abstain'),('final_abstention','Final abstention'),('resource_stop','Resource stops')]
 for index,(metric,label) in enumerate(incidence):
  totals=[float(next(r['plotted_value'] for r in plotted if r['panel']=='a' and r['metric']==metric and r['condition']==cond)) for cond in ['B1','G1']]
  assert totals==[sum(float(r[metric]) for r in data if r['condition']==cond) for cond in ['B1','G1']]
  a.plot(totals,[index-.07,index+.07],color='#999999',lw=.7,zorder=1)
  for total,y,cond in zip(totals,[index-.07,index+.07],['B1','G1']):
   a.scatter(total,y,color=COLORS[cond],marker=MARKERS[cond],s=28,edgecolor='black',linewidth=.35,zorder=3)
 a.set_yticks(range(len(incidence)),[label for metric,label in incidence]);a.set_ylim(len(incidence)-.45,-.5)
 a.set_xlim(-.7,30);a.set_xlabel('Runs (of 90 per condition)');a.set_title('(a) Control incidence',loc='left')
 clean(a,numeric='x',integer=True,zero=False)
 a.legend(handles=[Line2D([],[],marker=MARKERS[cond],color=COLORS[cond],ls='none',label=cond,markeredgecolor='black') for cond in ['B1','G1']],loc='lower right',frameon=False,ncol=2,handletextpad=.3,columnspacing=.8)
 task_groups=[]
 for cond in ['B1','G1']:
  task_groups.append([float(r['plotted_value']) for r in plotted if r['panel']=='b' and r['condition']==cond])
  assert task_groups[-1]==[mean([float(r['verification_calls']) for r in data if r['task_id']==task and r['condition']==cond]) for task in sorted({r['task_id'] for r in data})]
 distributions(b,task_groups,['B1','G1'],labels=['B1\n(n=30 tasks)','G1\n(n=30 tasks)'])
 b.set_title('(b) Verification calls',loc='left');b.set_ylabel('Calls per run (task mean)')
 actions=['ACCEPT','REVISE_ONLY','RERETRIEVE_REVISE','ABSTAIN'];labels=['Accept','Revise only','Re-retrieve + revise','Abstain']
 fills=['#CCCCCC','#56B4E9','#E69F00','#FFFFFF'];hatches=['','///','\\\\','xx']
 for y,cond in enumerate(['B1','G1']):
  counts={r['metric']:float(r['plotted_value']) for r in plotted if r['panel']=='c' and r['condition']==cond};left=0;assert sum(counts.values())==90
  assert counts=={action:sum(r['selected_action']==action for r in data if r['condition']==cond) for action in actions}
  for action,label,fill,hatch in zip(actions,labels,fills,hatches):
   n=counts[action];c.barh(y,n,left=left,height=.43,color=fill,edgecolor='black',hatch=hatch,linewidth=.65,label=label if y==0 else None)
   if n>=6:c.text(left+n/2,y,f'{n:g}',ha='center',va='center',fontsize=7.5)
   left+=n
 c.set_yticks([0,1],['B1','G1']);c.set_ylim(1.5,-.5);c.set_xlim(0,90)
 c.set_title('(c) Logged policy actions',loc='left');c.set_xlabel('Runs (of 90 per condition)');clean(c,numeric='x',integer=True)
 c.set_xticks([0,30,60,90])
 c.legend(loc='upper center',bbox_to_anchor=(.5,-.34),ncol=2 if size=='single_column' else 4,frameon=False,columnspacing=.9,handlelength=1.5)
 export(fig,'figure04_control_behavior',size,'Logged recovery and control behavior','figure04_control_behavior.csv',
  'Incidence/actions: 90 executions per condition. Verification distribution: 30 task means of 3 repetitions.',
  'Operational actions only; no correctness/grounding labels or judged recovery success. B0 structurally excluded.')

def fig05(size):
 data=read_csv('figure05_latency_distribution.csv')
 fig,axes=grid(size,4,{'single_column':8.1,'full_width':4.9})
 max_value=max(float(r['end_to_end_ms']) for r in data)
 styles={'B0':':','B1':'-','G1':'--'}
 for index,(ax,uc) in enumerate(zip(axes,['ALL']+UCS)):
  for cond in CONDITIONS if uc=='ALL' else ['B1','G1']:
   selected=sorted([r for r in data if r['condition']==cond and (uc=='ALL' or r['UC']==uc)],key=lambda r:(float(r['end_to_end_ms']),r['run_id']))
   xs=[0]+[float(r['end_to_end_ms']) for r in selected]+[max_value*1.03]
   ys=[0]+[float(r['overall_ecdf'] if uc=='ALL' else r['UC_ecdf']) for r in selected]+[1]
   ax.step(xs,ys,where='post',color=COLORS[cond],ls=styles[cond],lw=1.3,label=cond,
       marker=MARKERS[cond],markevery=[i+1 for i in range(0,len(selected),max(1,len(selected)//5))],markersize=2.8,markerfacecolor='white',markeredgewidth=.6)
  ax.set_title(f'({"abcd"[index]}) '+('Overall (n=90/condition)' if uc=='ALL' else uc+' (n=30/condition)'),loc='left')
  ax.set_ylabel('Cumulative fraction');ax.set_xlabel('Latency (ms)');ax.set_ylim(0,1.025);ax.set_yticks([0,.25,.5,.75,1])
  ax.set_yticklabels(['0','0.25','0.5','0.75','1']);ax.set_xlim(0,max_value*1.03);clean(ax,numeric='x')
  ax.legend(loc='lower right',frameon=False,handlelength=1.4,labelspacing=.3)
 export(fig,'figure05_latency_distribution',size,'Linear-scale latency distributions','figure05_latency_distribution.csv',
  'Raw executions: overall 90/condition; within UC 30/condition, descriptive only',
  'ECDF on logged milliseconds, linear scale including entire range; B0 supporting overall, B1/G1 primary within each UC.')

def figS01(size):
 data=read_csv('figureS01_token_decomposition.csv')
 fig,axes=grid(size,2,{'single_column':4.4,'full_width':2.65})
 for index,(ax,metric) in enumerate(zip(axes,['input_tokens','output_tokens'])):
  groups=[[float(r[metric]) for r in data if r['condition']==cond] for cond in CONDITIONS]
  distributions(ax,groups,CONDITIONS,labels=[cond+'\n(n=30 tasks)' for cond in CONDITIONS])
  label='Input tokens' if metric=='input_tokens' else 'Output tokens'
  ax.set_title(f'({"ab"[index]}) '+label,loc='left');ax.set_ylabel(label)
 mean_median_legend(fig)
 export(fig,'figureS01_token_decomposition',size,'Input and output token decomposition','figureS01_token_decomposition.csv',
  '30 task means per condition, 3 repetitions each','Input/output tokens separately; B0 supporting, B1/G1 primary. No normalization or scoring.')

def figS02(size):
 data=read_csv('figureS02_repetition_variability.csv')
 fig,ax=plt.subplots(figsize=(SIZE_WIDTH[size],2.8 if size=='single_column' else 3.0),layout='constrained')
 groups=[[float(r['latency_sample_sd_ms']) for r in data if r['condition']==cond] for cond in CONDITIONS]
 distributions(ax,groups,CONDITIONS,labels=[cond+'\n(n=30 tasks)' for cond in CONDITIONS])
 ax.set_ylabel('Within-task latency SD (ms)');ax.set_title('Latency repetition variability',loc='left')
 mean_median_legend(fig)
 export(fig,'figureS02_repetition_variability',size,'Within-task latency repetition variability','figureS02_repetition_variability.csv',
  '30 task-condition sample SDs per condition, each from exactly 3 repetitions',
  'Sample SD (n-1) of three raw latency observations. This is variability, not an inferential interval. Token SDs all zero, retained in companion CSV.')

def main():
 for size in SIZE_WIDTH:
  for fn in [fig01,fig02,fig03,fig04,fig05,figS01,figS02]:fn(size)
 (OUT/'figure_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 (OUT/'validation/layout_checks.json').write_text(json.dumps({'status':'PASS','figures':layout_records,'no_clipped_text':True,'no_panel_overlap':True,'minimum_font_pt':7.5},indent=2)+'\n')

if __name__=='__main__':main()
