from get_tracks_chart import get_tracks
import csv
def add_header(file):
# Define the column names as a list
    column_names = ['date', 'position', 'title', 'artist', 'label', 'isrc']

    # Read the existing data from the CSV file, and add column_names.
    with open(file, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        data = [row for row in reader]
        data.insert(0, column_names)

    # Write the data with column names as header to the CSV file
    with open('uk_top_singles_chart.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(data)

if __name__ == '__main__':
    # Enter start page to start the loop from 27th April 2018
    add_header('uk_top_singles_chart.csv')