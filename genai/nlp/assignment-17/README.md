Here's the extracted text (document: "GenAI - A17: Text Cleaning, Preprocessing & NLP Pipeline"):

_(top, cut off)_

- Focus on correctness and understanding.

## PART 1 — NLP Pipeline & Basic Text Cleaning

**Task 1: Understanding Raw Text Data**

1. Load the text dataset using Pandas.
2. Print:
   - First 5 text samples
   - Length of each text
3. Identify common issues in raw text such as:
   - Uppercase/lowercase mismatch
   - Punctuation
   - Numbers
   - Extra spaces

---

**Task 2: Basic Text Cleaning**
Apply the following basic cleaning steps:

1. Convert text to lowercase
2. Remove punctuation
3. Remove numbers
4. Remove extra whitespaces
5. Other Techniques Mentioned in the Lectures

Store cleaned text in a new column: clean_text_basic.
Extra (optional): Compare original text vs cleaned text side by side.

## PART 2 — Advanced Text Cleaning

**Task 3: Removing Noise**
Apply advanced cleaning techniques:

1. Remove URLs
2. Remove email addresses
3. Remove HTML tags
4. Remove special characters & emojis
5. All Other Techniques Mentioned in the Lectures

Store result in: clean_text_advanced.

**Task 4: Handling Stopwords**

1. Load stopwords using NLTK or spaCy.
2. Remove stopwords from clean_text_advanced.
3. Save output as text_no_stopwords.

**Task 5: Handling Repeated Characters & Slang (Optional)**

1. Normalize repeated characters:
   - soooo good → so good
2. Create a small slang dictionary:
   - u → you
   - gr8 → great
3. Replace slang words.

## PART 3 — Basic Text Preprocessing in NLP

**Task 6: Tokenization**

1. Perform word tokenization.
2. Perform sentence tokenization.
3. Display tokens for at least 3 text samples.

**Task 7: Stemming**

1. Apply Porter Stemmer or Snowball Stemmer.
2. Compare original words vs stemmed words.

---

**Task 8: Lemmatization**

1. Apply WordNet Lemmatizer or spaCy lemmatisation.
2. Compare stemming vs lemmatization results.

**Task 9: Final NLP Pipeline Creation**
Create a single function `nlp_preprocess(text)` that performs:

1. Lowercasing
2. Noise removal
3. Stopword removal
4. Tokenization
5. Lemmatization

Apply this function to the full dataset and store output in final_clean_text.

**Task 10: Observations & Insights**
Write short observations:

1. Difference between basic and advanced cleaning
2. Why lemmatization is preferred over stemming
3. Importance of preprocessing in NLP models

---

**Submission Guidelines:-**
_(cut off)_
