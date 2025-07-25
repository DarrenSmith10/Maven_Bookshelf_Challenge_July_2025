import csv

#I wrote a program to filter / reduce file size for github commit and Analysis
def filter_stream(input_path, output_path, keep_idxs, row_filter, batch_size=50000):
    with open(input_path, newline='', encoding='utf-8') as infile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)
        writer.writerow([header[i] for i in keep_idxs])
        batch = []
        for row in reader:
            if row_filter(row):
                batch.append([row[i] for i in keep_idxs])
            if len(batch) >= batch_size:
                writer.writerows(batch)
                batch = []
        if batch:
            writer.writerows(batch)



# Read and clean header
with open('Scripts/cleaned_goodreads_reviews.csv', newline='', encoding='utf-8') as f:
    hdr = next(csv.reader(f))
    hdr = [col.strip() for col in hdr]

keep_cols = ['review_id', 'user_id', 'rating']
keep_idxs = [hdr.index(c) for c in keep_cols]

def row_filter(row):
    try:
        return row[keep_cols.index('rating')] and float(row[keep_cols.index('rating')]) >= 5
    except:
        return False

filter_stream(
    input_path='Scripts/cleaned_goodreads_reviews.csv',
    output_path='Final_cleaned_goodreads_reviews.csv',
    keep_idxs=keep_idxs,
    row_filter=row_filter,
    batch_size=50000
)

