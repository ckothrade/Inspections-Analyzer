# Inspection Analyzer

A Python-based tool that simulates automated inspection systems used in manufacturing to validate part measurements against tolerance limits.

## Features
- Reads measurement data from a structured dataset
- Compares values against min/max tolerances
- Flags PASS/FAIL results
- Demonstrates quality control automation concepts

## Why I Built This
This project was created to connect software engineering with real-world manufacturing quality and inspection workflows.

## Example Input

PartID,Measurement,MinTol,MaxTol  
A1,10.02,9.95,10.05  
A2,9.80,9.95,10.05  

## Example Output

Part A1: PASS  
Part A2: FAIL  

## How to Run
```bash
python main.py
