# Read the 1,000 lines of taxi data from the taxi_1000.csv file
# Calculate the total of all fares, average fare, and the maximum
# trip distance.
import csv

with open("taxi_1000.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    total_fare = 0.0
    max_distance = 0.0
    average_fare = 0.0
    num_rows = 0

    for line in csv_reader:
        if (num_rows > 0):  # Skip header row
            tripFare = float(line[10])
            distance = float(line[5])
            total_fare += tripFare
            if (distance > max_distance):
                max_distance = distance
        num_rows += 1

    if num_rows > 0:
        average_fare = round(total_fare / num_rows, 2)

    print(f"We read {num_rows} rows")
    print(f"Total Fare: ${total_fare:.2f}")
    print(f"Average Fare: ${average_fare:.2f}")
    print(f"Maximum Distance: {max_distance:.2f}")