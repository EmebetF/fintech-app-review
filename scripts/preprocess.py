import pandas as pd

def preprocess_reviews(input_csv='./output/raw_reviews.csv', output_csv='./output/clean_reviews.csv'):
    df = pd.read_csv(input_csv)

    print(f"Initial rows: {len(df)}")

    # Drop duplicates (same review text from same bank)
    df.drop_duplicates(subset=['review', 'bank'], inplace=True)
    print(f"After removing duplicates: {len(df)}")

    # Drop rows with missing review or rating or date
    df.dropna(subset=['review', 'rating', 'date'], inplace=True)
    print(f"After dropping missing values: {len(df)}")

    # Optional: Filter ratings to valid range 1-5
    df = df[(df['rating'] >= 1) & (df['rating'] <= 5)]

    # Save cleaned data
    df.to_csv(output_csv, index=False)
    print(f"Saved cleaned data to {output_csv}")

if __name__ == "__main__":
    preprocess_reviews()
