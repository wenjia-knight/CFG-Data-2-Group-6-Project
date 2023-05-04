import csv

def get_unique_isrc(input_file_path, output_file_path):
# Create a set to store unique isrc values
    unique_isrcs = set()

    # Create an empty dictionary to store isrc, title, artist mappings
    isrc_to_track = {}

    # Open the input CSV file and read each row
    with open(input_file_path, newline='') as input_file:
        reader = csv.DictReader(input_file)

        for row in reader:
            # Extract the isrc value from each row and add it to the isrc values if it's not a duplicate.
            isrc = row['isrc']
            unique_isrcs.add(isrc)

            # Map the isrc value to its corresponding title and artist
            title = row['title']
            artist = row['artist']

            # use isrc as the dictionary key, map corresponding tuple (title, artist) as value.
            isrc_to_track[isrc] = (title, artist)

    # Write the output to a csv file with header.
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
        content = csv.writer(output_file)
        column_names = ['isrc', 'title', 'artist']
        content.writerow(column_names)

        # Write each unique ISRC and its corresponding title and artist to the output CSV file
        for isrc in unique_isrcs:
            title, artist = isrc_to_track[isrc]
            content.writerow([isrc, title, artist])

if __name__ == '__main__':
    get_unique_isrc(input_file_path = 'uk_top_singles_chart.csv', output_file_path = 'unique_isrc.csv')