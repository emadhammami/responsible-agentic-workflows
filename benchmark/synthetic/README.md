# Synthetic Engineering Corpus

This directory contains a small synthetic policy corpus used only for
engineering and pipeline validation.

It is not part of the final thesis benchmark dataset and results obtained from
these tasks must not be reported as thesis benchmark findings.

## Purpose

The corpus allows development of:

- document ingestion;
- chunking and provenance;
- retrieval;
- benchmark task loading;
- B0 integration;
- raw run logging;
- later B1 and G1 workflows;
- abstention behavior;
- cross-document reasoning;
- policy-precedence handling.

without using the real project documents.

## Documents

- DOC901 - Travel and Expense Policy
- DOC902 - Records Retention Policy
- DOC903 - Project Access Control Policy
- DOC904 - Security Incident Response Policy
- DOC905 - High-Risk Travel Addendum

These documents are fictional and were created specifically for engineering
tests.

## Tasks

The synthetic tasks cover:

- direct retrieval;
- within-document reasoning;
- cross-document reasoning;
- insufficient-evidence / abstention;
- conflicting or superseding policy requirements.

Task IDs T901-T907 are reserved for synthetic engineering use so they remain
clearly separate from future real benchmark task IDs.

## Evidence isolation

Reference answers and reference evidence in the task files are benchmark-side
data.

The runtime workflow must receive only the task question and the permitted
document corpus. Reference answers must not be placed in the retrieval index or
generation prompt.

## Status

Synthetic tasks may change during engineering.

They are not frozen scientific evidence.
