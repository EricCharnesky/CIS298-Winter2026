# bing copilot - pyplot examples

import matplotlib.pyplot as plt
import csv

with open('Electric_Vehicle_Population_Data.csv') as file_data:
    csv_reader = csv.reader(file_data)
    next(csv_reader, None)

    years = []
    ranges = []

    for row in csv_reader:
        try:
            if int(row[10]):
                years.append(int(row[5]))
                ranges.append(int(row[10]))
        except:
            pass

    plt.scatter(years, ranges)

    plt.show()


#
#
# MILES_PER_YEAR = 10_000
# SUV_GALLONS_USED = 1_000
# SEDAN_GALLONS_USED = 500
#
# # Data for the plot
# x_miles_per_gallons = range(10, 51)
# y_gallons_used = [ MILES_PER_YEAR / mpg for mpg in x_miles_per_gallons ]
#
# suv_gallons_saved = [ SUV_GALLONS_USED - (MILES_PER_YEAR / mpg ) for mpg in x_miles_per_gallons[:11]]
# sedan_gallons_saved = [ SEDAN_GALLONS_USED - (MILES_PER_YEAR / mpg ) for mpg in x_miles_per_gallons[10:]]
#
# # Create the plot
# plt.plot(x_miles_per_gallons, y_gallons_used, label='Gallons Used')
# plt.plot(x_miles_per_gallons[:11], suv_gallons_saved, label='Gallons saved for SUVs')
# plt.plot(x_miles_per_gallons[10:], sedan_gallons_saved, label='Gallons saved for Sedans')
#
# #bing copilot - pyplot how to add legend to label multiple lines
# plt.legend()
#
# # Add labels and title
# plt.xlabel('Miles Per Gallon')
# plt.ylabel('Gallons Used')
# plt.title('Huh')
#
# # Display the plot
# plt.show()