wr# Assignment 21 - Document Loaders & Text Splitters

LangChain loaders + splitters. load txt/csv/pdf/web, then chunk with length, recursive, markdown-header, and a small semantic demo.

## How to run

1. open `document_loaders_and_text_splitter.ipynb`
2. run top to bottom
3. keep `data/` next to the notebook (`notes.txt`, `sales_data.csv`, `d2l-en-mxnet.pdf`)

needs: langchain, langchain-community, langchain-text-splitters, pypdf, bs4, requests, scikit-learn

web loader needs network. if `USER_AGENT` warning shows up it’s fine — requests still work.

## What I did

**part 1 — document loaders**

- `TextLoader` on `data/notes.txt` → 1 doc + metadata
- `CSVLoader` on `data/sales_data.csv` → one doc per row
- `PyPDFLoader` on the d2l pdf → 12 pages
- `DirectoryLoader` with globs for txt/csv/pdf → combined ~113 docs
- `WebBaseLoader` on langchain overview docs → first ~500 chars

**part 2 — text splitters**

- task 6: context window + why chunking helps RAG / noise / hallucinations
- `CharacterTextSplitter(chunk_size=100, chunk_overlap=20)` on pdf pages
- `RecursiveCharacterTextSplitter` same settings — prefers `\n\n` → `\n` → space
- `MarkdownHeaderTextSplitter` on a sample md doc (headers kept in metadata); pdf pages already carry page metadata
- semantic demo: TF-IDF sentence vectors + cosine drop as topic breakpoint (no API key needed)

**part 3 — pipeline + insights**

- `load_and_split_documents(path_or_url)` picks loader by url / dir / extension, then recursive split
- ran on local `data/` and a web url
- task 12 notes: which loader/splitter for what, why overlap matters

## Where I struggled

- pdf text from this file is kinda smashed together (missing spaces) so tiny chunk sizes look weird
- `DirectoryLoader` needs separate globs per type if you want the right `loader_cls`
- real `SemanticChunker` wants `langchain_experimental` + embeddings API — used a sklearn TF-IDF stand-in instead
- web cell needs network; `USER_AGENT` warning is noisy but harmless

## Files

- `document_loaders_and_text_splitter.ipynb` — main notebook
- `data/notes.txt` — sample text
- `data/sales_data.csv` — sample csv
- `data/d2l-en-mxnet.pdf` — sample pdf (12 pages)
- `README.md` — this file
