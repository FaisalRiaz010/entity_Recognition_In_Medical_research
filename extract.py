import csv
import json

# Read the article data from the CSV file
with open('medical.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    articles = [row for row in reader]

# Initialize a dictionary to store the authors for each year
authors_by_year = {}

# Collect the authors for each year
for article in articles:
    year = article['publish_time']
    # Split the author string into a list of authors
    author_list = article['authors'].split(';')
    # Add each author to the set for the corresponding year
    if year not in authors_by_year:
        authors_by_year[year] = set()
    for author in author_list:
        authors_by_year[year].add(author)

# Convert the data to a dictionary and save it to a JSON file
data = [{'year': year, 'num_authors': len(authors_by_year[year])} for year in authors_by_year]
with open('authors_by_year.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
