# Building with the Claude API

My notebooks and exercises from Anthropic's [**Claude with the Anthropic API**](https://anthropic.skilljar.com/claude-with-the-anthropic-api) course. Each folder lines up with a section of the course, and the notebooks inside are numbered in lesson order.

## Contents

### 01 · Accessing Claude with the API
| Notebook | Lesson |
|---|---|
| `01_making_a_request.ipynb` | Making a request |
| `02_multi_turn_conversations.ipynb` | Multi-turn conversations |
| `03_chat_exercise.ipynb` | Chat exercise: a looping terminal chatbot |
| `04_system_prompts_ai_tutor.ipynb` | System prompts: steering Claude to act as a math tutor |
| `05_system_prompts_exercise.ipynb` | System prompts exercise |
| `06_temperature.ipynb` | Temperature |
| `07_response_streaming.ipynb` | Response streaming |
| `08_structured_data.ipynb` | Structured data |
| `09_structured_data_exercise.ipynb` | Structured data exercise |

### 02 · Prompt Evaluation
| Notebook | Lesson |
|---|---|
| `01_generating_test_datasets.ipynb` | Generating test datasets |
| `02_running_the_eval.ipynb` | Running the eval |
| `03_model_based_grading.ipynb` | Model-based grading |
| `04_code_based_grading.ipynb` | Code-based grading |
| `05_prompt_eval_exercise.ipynb` | Exercise on prompt evals |

### 03 · Prompt Engineering Techniques
| Notebook | Lesson |
|---|---|
| `01_prompt_engineering.ipynb` | Baseline prompt and evaluation pipeline (`.py` export included) |
| `02_being_clear_and_direct.ipynb` | Being clear and direct |
| `03_being_specific.ipynb` | Being specific |
| `04_structure_with_xml_tags.ipynb` | Structure with XML tags |
| `05_prompting_exercise.ipynb` | Exercise on prompting |

`dataset.json`, `output.json` and `output.html` are the eval dataset and the generated evaluation report.

### 04 · Tool Use with Claude
| Notebook | Lesson |
|---|---|
| `01_tool_use.ipynb` | Tool functions, schemas, message blocks, tool results and multi-turn tool use |
| `02_fine_grained_tool_calling.ipynb` | Streaming tool calls and fine-grained tool calling |
| `03_text_edit_tool.ipynb` | The text editor tool (`main.py` and `test.py` were written by Claude using it) |

### 05 · RAG and Agentic Search
| Notebook | Lesson |
|---|---|
| `01_text_chunking_and_embeddings.ipynb` | Text chunking strategies (by character, sentence and section), text embeddings with Voyage AI, and a custom `VectorIndex` |
| `02_vector_database.ipynb` | The full RAG flow: chunk `report.md` by section, embed each chunk, store it in the vector index and run a semantic query ("What did the software engineering department do last year?") |
| `03_vector_db.ipynb` | The same pipeline run with an exact-ID query ("What happened with INC-2023-Q4-011?"), showing where embedding search struggles with specific identifiers |
| `004_bm25.ipynb` | BM25 lexical search: a from-scratch `BM25Index` (tokenizing, IDF, term-frequency scoring and score normalization) searched with the same incident-ID query |
| `05_Hybrid_Rag_Implementation.ipynb` | A multi-index (hybrid) RAG pipeline: a `Retriever` runs the `VectorIndex` and `BM25Index` together and merges their rankings with reciprocal rank fusion (RRF) |

`report.md` is the sample document every notebook in this section searches, and `VoyageAI_API_Key_Directions.pdf` covers setting up a Voyage AI key for embeddings.

**What the BM25 notebook shows:** for the incident-ID query, BM25 ranks *Section 2: Software Engineering* above *Section 10: Cybersecurity*. That isn't a bug. Section 2 mentions `INC-2023-Q4-011` three times and Section 10 mentions it twice, and BM25 only counts matching words. Semantic search and lexical search each miss something, which is why the hybrid notebook combines them.

**What the hybrid notebook shows:** with RRF (`k_rrf = 60`), Section 2 and Section 10 come out in an exact tie (score 0.0325, which is 1/61 + 1/62). One index ranks Section 2 first and Section 10 second, and the other index ranks them the other way around, so the fusion scores them equally. Methodology is a distant third. The hybrid retriever puts both sections that are relevant to the incident at the top, and neither index's mistakes push either one down.

**Voyage AI free tier:** without a payment method, Voyage allows 3 requests and 10K tokens per minute. The hybrid notebook adds every chunk with `retriever.add_documents([...])`, which embeds the whole report in **one** request instead of one request per chunk.

## Setup

```bash
git clone https://github.com/AHayslip23/building-with-claude-api.git
cd building-with-claude-api
pip install -r requirements.txt
```

Copy `.env.example` to `.env` in the repo root and add your keys:

```
ANTHROPIC_API_KEY=...
VOYAGE_API_KEY=...
```

Each notebook calls `load_dotenv()`, which finds the `.env` file in the root folder. Then open any notebook with `jupyter lab`.

## Tech
Python · Jupyter · Anthropic Python SDK · Voyage AI embeddings · BM25 · Reciprocal rank fusion

## Changelog
See [CHANGELOG.md](CHANGELOG.md) for what changed in each commit.
