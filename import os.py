import csv

input_file = "medicall.csv"
output_file = "abcmedical.csv"

with open(input_file, "r", encoding="utf-8") as f_input, open(output_file, "w", encoding="utf-8", newline='') as f_output:
    reader = csv.DictReader(f_input)
    writer = csv.DictWriter(f_output, fieldnames=reader.fieldnames)
    writer.writeheader()
    
    for row in reader:
        if row["abstract"].strip():
            writer.writerow(row)
