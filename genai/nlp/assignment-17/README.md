# Assignment 17 - Text Cleaning & NLP Pipeline

TMDB movie overviews (`tmdb_5000_movies.csv`). Mostly text cleaning + classic NLP preprocessing (tokenize, stem, lemmatize) and one combined `nlp_preprocess` function at the end.

## How to run

1. Open `nlp_pipeline.ipynb`
2. Run from the top
3. Keep `tmdb_5000_movies.csv` in this folder (credits CSV is there too but I used movies)

Needs: `pandas`, `nltk`, `spacy` + `en_core_web_sm`

```bash
# if spaCy model missing:
uv pip install --python .venv/bin/python https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
```

## What I did

**Part 1 — Basic cleaning**

- Loaded overviews, dropped nulls with `df.dropna(subset=['overview'])`
- Built `clean_text_basic`: lowercase, punctuation, numbers, extra spaces

**Part 2 — Advanced cleaning**

- `clean_text_advanced`: URLs, emails, HTML tags, special chars
- Removed English stopwords → `text_no_stopwords`
- Optional: collapse repeated chars (`soooo` → `so`) + small slang dict

**Part 3 — Tokenize / stem / lemmatize**

- NLTK word + sentence tokenization
- Porter + Snowball stemming on tokens
- WordNet + spaCy lemmatization (spaCy needed `' '.join(tokens)` because `nlp()` wants a string not a list)

**Part 4 — Pipeline + insights**

- One function `nlp_preprocess(text)` doing lowercase → noise removal → stopwords → tokenize → lemmatize
- Applied on full `overview` → `final_clean_text`
- Task 10 writeup in the notebook (basic vs advanced, lemma vs stem, why preprocess)

## Where I struggled

- `df['overview'].dropna(inplace=True)` looked like it worked but nulls were still in the dataframe — needed `subset=['overview']`
- pandas/Arrow `.str.replace` hates backreferences (`\1`) — had to use `re.sub` via `.apply` for repeated characters
- spaCy model wasn't installed (`en_core_web_sm`) until I downloaded it into the venv
- Forgot spaCy takes strings not token lists → E1041 until I joined them

## Files

- `nlp_pipeline.ipynb` — notebook
- `tmdb_5000_movies.csv` — main dataset
- `tmdb_5000_credits.csv` — extra / unused for this one
- `README.md` — this file
