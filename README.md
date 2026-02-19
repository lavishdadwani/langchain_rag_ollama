# LangChain RAG with Ollama

Before installing the packages, make sure you have:

1. **Python 3.8 or higher** installed on your system
2. **Ollama** installed and running on your machine
   - Download from: https://ollama.ai/
   - Install the required models:
     ```bash
     ollama pull llama3.2
     ollama pull nomic-embed-text
     ```

## Installation

### Step 1: Install Python Packages

Install all required packages using pip:

```bash
pip install langchain-community langchain-text-splitters langchain-core langchain-chroma langchain-ollama
```

### Step 2: Verify Ollama Models

Make sure Ollama is running and you have the required models:

```bash
# Check if Ollama is running and you have the required model
ollama list
```

## Project Structure

```
Langchain_rag_ollama/
├── data/                    # Place your PDF files here
│   ├── monopoly.pdf
│   └── ticket_to_ride.pdf
├── chroma/                  # Vector database (auto-generated)
├── get_embedding_function.py
├── populate_database.py     # Script to process PDFs and create database
├── query_data.py            # Script to query the database
└── test_rag.py              # Test script
```

### Step 1: Prepare Your Documents

Place your PDF files in the `data/` directory.

### Step 2: Populate the Database

Run the script to process PDFs and create the vector database:

```bash
python populate_database.py
```

To reset and rebuild the database from scratch:

```bash
python populate_database.py --reset
```

### Step 3: Query the Database

Ask questions about your documents:

```bash
python query_data.py "Your question here"
```

Example:
```bash
python query_data.py "How much money does a player start with in Monopoly?"
```

### Step 4: Run Tests (Optional)

Test the system with predefined questions:

```bash
python test_rag.py
```

## Troubleshooting

### Ollama Connection Issues
- Make sure Ollama is running: `ollama list`
- Check if models are installed: `ollama list`
- Restart Ollama if needed

### Import Errors
- Make sure all packages are installed: `pip list | grep langchain`
- Try reinstalling: `pip install --upgrade langchain-community langchain-text-splitters langchain-core langchain-chroma langchain-ollama`

### Database Issues
- If you encounter database errors, try resetting: `python populate_database.py --reset`

## Dependencies Summary

- **langchain-community**: Provides PDF document loaders
- **langchain-text-splitters**: Splits documents into chunks
- **langchain-core**: Core LangChain components (Document, prompts)
- **langchain-chroma**: Chroma vector database integration
- **langchain-ollama**: Ollama LLM and embeddings integration

