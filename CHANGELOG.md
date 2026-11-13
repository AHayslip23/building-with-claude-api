# Changelog

All notable changes to this repository are listed here, newest first.

## Commit #3: Hybrid RAG, 2026-11-13
### Added
- `05-rag-and-agentic-search/05_Hybrid_Rag_Implementation.ipynb`: the multi-index RAG pipeline, which finishes the RAG and Agentic Search section.
  - `VectorIndex` (Voyage `voyage-3-large` embeddings, cosine or Euclidean distance) and `BM25Index`, combined behind a `SearchIndex` protocol.
  - A `Retriever` that sends each query to every index, collects the top `k * 5` from each, and merges them with reciprocal rank fusion (`k_rrf = 60`).
  - Result for "What happened with INC-2023-Q4-011?": Section 2 (Software Engineering) and Section 10 (Cybersecurity) tie at 0.0325 (1/61 + 1/62) because each index ranks them in the opposite order, and Methodology is third at 0.0310.

### Fixed (in the hybrid notebook before committing)
- **Voyage `RateLimitError`:** the free tier (no payment method) allows 3 requests and 10K tokens per minute. Adding chunks one at a time with `add_document` made one embedding request per chunk and hit the limit. The notebook now calls `retriever.add_documents([...])` once, which embeds every chunk in a single request.
- `retriever.add_documents(...)` was passed a generator instead of a list. Added the square brackets so it gets a list, which both indexes need (a generator can only be read once).
- The search cell printed `results` without first creating it with `retriever.search(...)`.
- `VectorIndex`: fixed the `LIst` typo, `contents.appends` → `append`, the `search(self, query, Any, k)` signature → `query: Any`, `sort(ley=...)` → `key=`, `distance[:k]` → `distances[:k]`, and the `consine_similarity` misspelling.
- `Retriever.search`: `scored_docs = List[...] = [...]` → `scored_docs: List[...] = [...]`.
- `BM25Index`: the missing `]` in the `tokenizer` type hint (a SyntaxError), `self.documents = List[...]` → `:`, the `_update_stat_add` / `_update_stats_add` name mismatch, and missing underscores on `_doc_len`, `_doc_freqs`, `_build_index()` and `_avg_doc_len`.

### Changed
- README: added the hybrid notebook, explained the RRF tie and the Voyage free-tier limits, marked the RAG section complete and added reciprocal rank fusion to the tech list.

## README and changelog update (`b6d0ab1`), 2026-11-12
### Added
- `CHANGELOG.md` (this file).

### Changed
- README: added `03_vector_db.ipynb` and `004_bm25.ipynb` to the RAG section table, explained the BM25 ranking result, added BM25 to the tech list and linked this changelog.

## Commit #2 (`7826d74`), 2026-11-12
### Added
- `05-rag-and-agentic-search/03_vector_db.ipynb`: the vector-database pipeline from `02_vector_database.ipynb`, rerun with the exact-ID query "What happened with INC-2023-Q4-011?" to test semantic search on a specific identifier.
- `05-rag-and-agentic-search/004_bm25.ipynb`: BM25 lexical search with a from-scratch `BM25Index` class (tokenizer, document frequencies, IDF, BM25 scoring and exponential score normalization), searched with the same incident-ID query.

### Fixed (in `004_bm25.ipynb` before committing)
- `search()` returned after scoring only the first chunk because its sort, normalize and return steps were indented inside the scoring loop, so the search printed no results. All chunks are now scored before ranking.
- Renamed `__len` to `__len__`, so `len(store)` and the class's `__repr__` work.
- `_calculate_idf` now resets `self._idf` (it was resetting a misspelled `self.idf`).
- `_build_index` now sets `self._avg_doc_len` (it was setting a misspelled `self.avg_doc_len`).

## Commit #1 (`89abe8b`), 2026-11-12
### Added
- `05-rag-and-agentic-search/01_text_chunking_and_embeddings.ipynb`: the newest version of the text-chunking notebook, extended with Voyage AI embeddings (`generate_embedding`) and a custom `VectorIndex`.
- `05-rag-and-agentic-search/02_vector_database.ipynb`: the full RAG flow, which chunks `report.md` by section, embeds the chunks, stores them in the vector index and runs a semantic query (previously `003_vectordb.ipynb`).

### Removed
- `05-rag-and-agentic-search/01_text_chunking.ipynb`, replaced by the expanded `01_text_chunking_and_embeddings.ipynb`.

### Changed
- README: updated the RAG section table for the new notebooks.
- Repo housekeeping (not tracked in git): moved everything into the `building-with-claude-api` clone and removed the duplicate copies from the parent folder.

## Initial commit (`b2019bd`), 2026-11-12: "Organize Claude API course notebooks by section"
### Added
- Notebooks from the first five course sections, organized into numbered folders that match the course outline:
  - `01-accessing-claude-with-the-api/`: 9 notebooks (requests, multi-turn chat, system prompts, temperature, streaming, structured data and exercises)
  - `02-prompt-evaluation/`: 5 notebooks (test datasets, running evals, model- and code-based grading, exercise) plus `dataset.json`
  - `03-prompt-engineering-techniques/`: 5 notebooks (baseline, clear and direct, being specific, XML tags, exercise), a `.py` export, `dataset.json` and the `output.json` / `output.html` eval report
  - `04-tool-use-with-claude/`: 3 notebooks (tool use, fine-grained tool calling, text editor tool) plus `main.py` / `test.py` written by the text editor tool
  - `05-rag-and-agentic-search/`: `01_text_chunking.ipynb`, `report.md` and `VoyageAI_API_Key_Directions.pdf`
- `README.md` with a per-section table of notebooks and setup instructions.
- `.gitignore`, which leaves out `.env`, `.ipynb_checkpoints/`, `.backups/`, `__pycache__/` and `Untitled*.ipynb`.
- `.env.example` (key names only) and `requirements.txt`.

### Changed
- Renamed the notebooks from their original names to numbered snake_case names in lesson order (for example, `Make a Request using Claude.ipynb` became `01_making_a_request.ipynb`) and fixed the "Strcutured" typo.

### Security
- Checked every notebook and script for hard-coded API keys before the first commit; keys live only in the git-ignored `.env`.
