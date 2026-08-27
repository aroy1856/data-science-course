# Assignment 19 - Word2Vec

TMDB movie overviews again. this one is about word embeddings with gensim Word2Vec — cbow vs skip-gram, similar words, some vector math, and a 2d plot.

## How to run

1. open `word2vec.ipynb`
2. run top to bottom
3. keep `tmdb_5000_movies.csv` in this folder

needs: pandas, nltk (+ stopwords/punkt/wordnet data), gensim, scikit-learn, plotly

if nltk throws weird `nltk.data` / circular import errors: restart kernel, `import nltk` alone first, then the corpus imports. dont call `nltk.download()` in the same broken state if you can avoid it.

## What I did

**part 1–2 — concepts**
- wrote answers on embeddings, why one-hot/bow suck at meaning, what word2vec is
- cbow vs skip-gram + rough nn intuition (input → embedding weights → predict word)

**part 3 — train on overviews**
- cleaned overview text (lower, noise, stopwords, tokenize, lemmatize) → list of tokens per row
- trained CBOW (`sg=0`) and Skip-Gram (`sg=1`), vector_size=100, window=5, min_count=1
- printed vocab size + a sample vector (`movie`)
- compared train time + top similar words
- similarity helpers + vector arithmetic like king - man + woman (results were hit/miss on this dataset tbh)

**part 4 — viz + insights**
- PCA down to 2d on top ~200 words, plotted with plotly
- task 10 writeup in the notebook (cbow vs sg, w2v vs tfidf, limits, why context/transformers)

## Where I struggled

- nltk circular import / `no attribute data` stuff was annoying — kernel restart + careful imports
- king-man+woman style analogies dont always land on movie data
- plotting whole vocab is useless, had to cut to top 200 words
- gensim wasnt installed at first, needed that for Word2Vec

## Files

- `word2vec.ipynb` — notebook
- `tmdb_5000_movies.csv` — dataset
- `README.md` — this file
