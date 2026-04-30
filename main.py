import csv

INPUT_FILE = "inspection_data.csv"
OUTPUT_FILE = "inspection_report.csv"


def analyze_measurement(measurement, min_tol, max_tol):
    if min_tol <= measurement <= max_tol:
        return "PASS"
    return "FAIL"


def process_inspection_data(input_file, output_file):
    results = []
    pass_count = 0
    fail_count = 0

    with open(input_file, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            measurement = float(row["Measurement"])
            min_tol = float(row["MinTol"])
            max_tol = float(row["MaxTol"])

            result = analyze_measurement(measurement, min_tol, max_tol)

            if result == "PASS":
                pass_count += 1
            else:
                fail_count += 1

            results.append({
                "PartID": row["PartID"],
                "Feature": row["Feature"],
                "Measurement": measurement,
                "MinTol": min_tol,
                "MaxTol": max_tol,
                "Result": result
            })

    with open(output_file, mode="w", newline="") as file:
        fieldnames = ["PartID", "Feature", "Measurement", "MinTol", "MaxTol", "Result"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    print("Inspection Analysis Complete")
    print(f"Total Parts Checked: {len(results)}")
    print(f"Passed: {pass_count}")
    print(f"Failed: {fail_count}")
    print(f"Report Generated: {output_file}")


if __name__ == "__main__":
    process_inspection_data(INPUT_FILE, OUTPUT_FILE)
