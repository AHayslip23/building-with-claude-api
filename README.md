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

### 05 · RAG and Agentic Search *(in progress)*
| Notebook | Lesson |
|---|---|
| `01_text_chunking_and_embeddings.ipynb` | Text chunking strategies (by character, sentence and section), text embeddings with Voyage AI, and a vector index |
| `02_vector_database.ipynb` | The full RAG flow: chunk, embed and store sections in a vector index, then search it |

`report.md` is the sample document used for chunking, and `VoyageAI_API_Key_Directions.pdf` covers setting up a Voyage AI key for embeddings.

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
Python · Jupyter · Anthropic Python SDK · Voyage AI embeddings
