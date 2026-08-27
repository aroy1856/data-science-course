# Assignment 18 - Text Vectorization

TMDB overviews again. Turning text into numbers — one-hot, bow, ngrams, tfidf. mostly sklearn on a sample of 10 overviews so it doesnt explode.

## How to run

1. open `vectorization.ipynb`
2. run top to bottom
3. `tmdb_5000_movies.csv` needs to be in this folder

needs: pandas, scikit-learn

## What I did

**part 1 — one hot**
- grabbed 10 overviews, made vocab by hand, built one-hot manually
- then did the same with CountVectorizer(binary=True)

**part 2 — bow**
- normal CountVectorizer for counts
- summed columns for top/least frequent words

**part 3 — ngrams**
- uni / bi / tri vocab sizes
- also (1,2) combined — vocab got bigger, a bit more phrase context

**part 4 — tfidf**
- TfidfVectorizer, checked shape
- compared bow vs tfidf weights
- wrote 8.3 on why common words get downweighted

**part 5**
- messed with max_features / min_df / max_df, vocab size changes a lot
  - max_features=100 → (10, 100)
  - min_df=5 → only 6 words left lol
  - max_df=0.8 → (10, 335)
- task 10 answers are in the notebook

## Where I struggled

- notebook file got insanely big from printing full matrices, kinda regret that
- summing tfidf still put "the" near the top which was confusing until i thought about it
- manual one-hot vs sklearn doc vectors — different things, mixed them up initially

## Files

- `vectorization.ipynb`
- `tmdb_5000_movies.csv`
- `README.md`
