import csv

# Read the CSV file
with open("library.csv", "r", newline="") as file:
    csv_data = list(csv.reader(file))

# Count total books
count = len(csv_data) - 1

# Count borrowed and available books
available_count = 0
borrowed_count = 0

for row in csv_data[1:]:
    if row[2] == "":
        available_count += 1
    else:
        borrowed_count += 1

print("Total number of books:", count)
print("Borrowed books:", borrowed_count)
print("Available books:", available_count)

# Prevent duplicate columns
if "Total Books" in csv_data[0]:
    print("Statistics already added.")
    exit()

# Add new columns
csv_data[0].extend(["Total Books", "Borrowed", "Available"])

# Add values to every row
for row in csv_data[1:]:
    row.extend([count, borrowed_count, available_count])

# Save the updated CSV
with open("library.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("CSV file updated successfully.")