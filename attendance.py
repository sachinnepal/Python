import csv
import sys

# Read the CSV file
with open("attendance.csv", "r", newline="") as file:
    csv_data = list(csv.reader(file))

# Check if Attendance % column already exists
if "Attendance %" in csv_data[0]:
    print("Attendance already calculated.")
    sys.exit()

# Add new columns
csv_data[0].extend([
    "Total Days",
    "Total Present",
    "Total Absent",
    "Attendance %"
])

# Calculate attendance for each student
for row in csv_data[1:]:

    attendance = row[2:]          # Attendance records only

    total_days = len(attendance)
    total_present = attendance.count("P")
    total_absent = attendance.count("A")

    attendance_percentage = round((total_present / total_days) * 100, 2)

    row.extend([
        total_days,
        total_present,
        total_absent,
        attendance_percentage
    ])

# Save the updated CSV file
with open("attendance.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("Attendance calculated successfully.")