#!/usr/bin/env python3
"""Run all three non-destructive, reported-data reconstruction checks."""
import argparse,subprocess,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    base=Path(__file__).resolve().parent
    a.output.mkdir(parents=True,exist_ok=False)
    for name in ('study-b','resource-boundary','study-c'):
        subprocess.run([sys.executable,str(base/name/'reproduce.py'),'--output',str(a.output/name)],check=True)
    print('Supplementary reconstruction checks completed. Outputs:',a.output)
if __name__=='__main__':main()
