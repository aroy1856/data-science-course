# Assignment 20 - Movie Recommendation System

TMDB movies again. build a content-based recommender — clean text, tf-idf, cosine similarity, then a tiny streamlit app.

## How to run

**Notebook**
1. open `movie-reccomendation.ipynb`
2. run top to bottom
3. keep `tmdb_5000_movies.csv` in this folder

needs: pandas, nltk, scikit-learn

**Streamlit app (part 4)**
```bash
cd app
streamlit run app.py
```

app needs `titles.pkl` + `similarity_matrix.pkl` (generate from notebook — see below)

## What I did

**part 1 — preprocessing**
- loaded tmdb csv, used overview + genres + keywords + tagline + title as `movie_blob`
- genres/keywords are json strings — parsed with `json.loads` and pulled out `name` fields
- nltk preprocess (lower, noise, stopwords, tokenize, lemmatize) → `clean_text`

**part 2 — vectorization**
- `TfidfVectorizer(max_features=15000, ngram_range=(1, 3))`
- cosine similarity matrix on all movies (3959 rows in my run — movies with taglines)
- saved matrix as pickle

**part 3 — recommend function**
- pick movie by title, sort similarity scores, skip first result (same movie), return top 5

**part 4 — streamlit**
- simple dropdown + button in `app/app.py`
- shows numbered recommendations, nothing fancy

**part 5–6 — git / render**
- not done in repo yet (submission stuff)

## Where I struggled

- genres col looked like a list but its actually a json string in csv — cant just split on comma
- `df['col'].dropna()` on a series doesnt drop rows from the dataframe
- first similar movie is always itself — had to slice `[1:top_n+1]` not `[0:top_n]`
- similarity matrix pickle is huge (~125mb) so didnt commit it — regenerate locally
- nltk same circular import headache as assignment 19 sometimes

## Files

- `movie-reccomendation.ipynb` — main notebook
- `tmdb_5000_movies.csv` — dataset
- `app/app.py` — streamlit ui
- `app/requirements.txt` — just streamlit
- `app/titles.pkl` — movie titles in matrix order
- `similarity_matrix.pkl` — run notebook to create (not in git, too big)
- `README.md` — this file

## regenerate app data (after retraining)

```python
import pickle

with open("similarity_matrix.pkl", "wb") as f:
    pickle.dump(similarity_matrix, f)

with open("app/titles.pkl", "wb") as f:
    pickle.dump(data.reset_index(drop=True)["title"].tolist(), f)
```
