import csv
import os

def clean_csv(input_path, output_path):
    seen = set()
    cleaned_rows = []

    with open(input_path, 'r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = ['id', 'score']
        for row in reader:
            row = {k.lower(): v.strip() for k, v in row.items()}
            if not row.get('id') or not row.get('score'):
                continue
            try:
                score = float(row['score'])
                if score < 0 or score > 100:
                    continue
            except:
                continue
            row_tuple = (row['id'], row['score'])
            if row_tuple in seen:
                continue
            seen.add(row_tuple)
            cleaned_rows.append({'id': row['id'], 'score': row['score']})

    with open(output_path, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

if __name__ == "__main__":
    input_file = 'raw/test.csv'
    output_file = 'processed/cleaned_test.csv'
    os.makedirs('processed', exist_ok=True)
    clean_csv(input_file, output_file)
