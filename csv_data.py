import csv

rows = []

# Read the CSV file
with open("marks.csv", "r") as file:
    csv_read = csv.reader(file)

    for row in csv_read:
        rows.append(row)

if "Total" in rows[0]:
    print("Result already calculated.")
    exit()
    
# Add new column names
rows[0].extend(["Total", "Average", "Result"])

# Calculate Total, Average and Result for each student
for row in rows[1:]:
    math = int(row[2])
    science = int(row[3])
    english = int(row[4])

    total = math + science + english
    average = round(total / 3, 2)

    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    row.extend([total, average, result])

# Write the updated data back to the same CSV file
with open("marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV file updated successfully!")

# Display the updated data
for row in rows:
    print(row)