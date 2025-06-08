from google_play_scraper import Sort, reviews_all
import pandas as pd

def scrape_reviews(app_id, bank_name):
    print(f"Scraping reviews for {bank_name}...")
    all_reviews = reviews_all(
        app_id,
        sort=Sort.NEWEST,
        sleep_milliseconds=0,
    )

    data = []
    for r in all_reviews:
        review_text = r.get('content', '')
        rating = r.get('score', None)
        date = r.get('at', None)
        if date:
            date = date.strftime('%Y-%m-%d')
        else:
            date = None

        data.append({
            'review': review_text,
            'rating': rating,
            'date': date,
            'bank': bank_name,
            'source': 'Google Play',
        })

    df = pd.DataFrame(data)
    print(f"Collected {len(df)} reviews for {bank_name}")
    return df

if __name__ == "__main__":
    bank_apps = {
        'Commercial Bank of Ethiopia': 'com.combanketh.mobilebanking',
        'Bank of Abyssinia': 'com.boa.boaMobileBanking',
        'Dashen Bank': 'com.dashen.dashensuperapp',
    }

    all_dfs = []
    for bank, app_id in bank_apps.items():
        df = scrape_reviews(app_id, bank)
        all_dfs.append(df)

    all_reviews_df = pd.concat(all_dfs, ignore_index=True)
    all_reviews_df.to_csv('./output/raw_reviews.csv', index=False)
    print("Saved raw reviews to raw_reviews.csv")
