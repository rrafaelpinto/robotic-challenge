import csv
import main
from collections import Counter

def sort_multiple_packages(path):
    results = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                width = float(row['width'])
                height = float(row['height'])
                length = float(row['length'])
                mass = float(row['mass'])
                result = main.sort(width, height, length, mass)                
                results.append(result)
            except (ValueError, TypeError) as e:
                results.append(f"Error processing row {row}: {e}")
    counts = Counter(results)
    return dict(counts)


if __name__ == "__main__":
    result = sort_multiple_packages('data/packages_valid.csv')
    print(result)