import csv

def analyze_measurement(measurement, min_tol, max_tol):
    if min_tol <= measurement <= max_tol:
        return "PASS"
    return "FAIL"

with open('inspection_data.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        measurement = float(row['Measurement'])
        min_tol = float(row['MinTol'])
        max_tol = float(row['MaxTol'])

        result = analyze_measurement(measurement, min_tol, max_tol)

        print(f"Part {row['PartID']}: {result}")
