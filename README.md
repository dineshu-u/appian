# Case-Aware Policy Attachment System

This project demonstrates a functional prototype of a **case-aware knowledge retrieval system**.
Instead of searching documents manually, relevant policy rules are automatically attached to a case
based on its attributes.

---

## Problem
Support agents waste time searching through PDFs and policy documents.
This leads to longer handling times and compliance errors.

---

## Solution
We introduce a **Policy Mapping Layer** that links case attributes
(e.g., claim type, state) directly to relevant policy clauses.

The system:
- Reads structured case data
- Finds relevant policy sections
- Displays them with document name and page number

---

## How It Works
**Input:** Case details (Claim Type, State)  
**Processing:** Match case fields with policy text  
**Output:** Relevant policy clauses with citations

---

## How to Run
```bash
pip install -r requirements.txt
streamlit run ui/app.py
