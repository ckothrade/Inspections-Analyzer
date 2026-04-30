# Inspection Analyzer

A Python-based inspection analysis tool that processes measurement data and validates each part feature against defined tolerance limits.

## Purpose

This project was built to demonstrate how software can support manufacturing quality workflows by automating tolerance verification, pass/fail classification, and inspection reporting.

## Tools Used

- Python
- CSV data processing
- Conditional logic
- File input/output
- Basic report generation

## Features

- Reads structured inspection data from a CSV file
- Converts measurement and tolerance values into numerical data
- Compares each measurement against minimum and maximum tolerance limits
- Assigns PASS/FAIL results
- Generates a new inspection report CSV
- Prints a summary of total parts checked, passed, and failed

## How To Run

```bash
python main.py
```

## Example Input

```csv
PartID,Feature,Measurement,MinTol,MaxTol
A001,Hole Diameter,10.02,9.95,10.05
A002,Hole Diameter,9.91,9.95,10.05
```

## Example Output

Inspection Analysis Complete
Total Parts Checked: 5
Passed: 3
Failed: 2
Report Generated: inspection_report.csv
