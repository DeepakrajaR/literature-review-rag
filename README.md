# Literature Review Assistant with ChromaDB

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-0.4.22-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-Optional-green.svg)
![RAG](https://img.shields.io/badge/Architecture-RAG-purple.svg)

This project implements a Retrieval-Augmented Generation (RAG) system for academic research, using ChromaDB as the external vector database. The system helps researchers search, retrieve, and summarize academic papers based on natural language queries.

## Features

- **Semantic Search**: Find relevant papers based on natural language queries
- **AI-Generated Insights**: Get summaries, comparisons, and research suggestions
- **External Vector Database**: Uses ChromaDB for efficient vector storage and retrieval
- **User-Friendly Interface**: Intuitive Streamlit interface for easy interaction

## Requirements

- Python 3.9+
- OpenAI API key (optional, for enhanced response generation)

## Installation

1. Clone this repository:
   ```
   git clone https:/github.com/deepakrajaR/literature-review-rag
   cd literature-review-assistant
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. (Optional) Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. First, run the data processor to download and index papers:
   ```
   python data_processor.py
   ```
   This will:
   - Download paper abstracts from arXiv or create sample data if download fails
   - Process the papers and store them in ChromaDB
   - Save the ChromaDB database in the `data/chroma_db` directory

2. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
   The application will be available at http://localhost:8501

3. Use the application:
   - Enter your research question in the text area
   - Adjust settings in the sidebar if needed
   - Click "Search" to get results
   - Explore the AI-generated response and relevant papers

## Architecture

This implementation follows a standard RAG architecture:

1. **Data Collection**: Download academic papers from arXiv (or use sample data)
2. **Vector Storage**: Store paper embeddings in ChromaDB
3. **Query Processing**: Convert user queries to vectors and find similar papers
4. **Response Generation**: Generate insights using retrieved papers

## Technologies Used

- **ChromaDB**: Open-source vector database for storing and retrieving embeddings
- **Streamlit**: For the user interface
- **OpenAI API** (optional): For generating higher quality responses
- **Pandas & NumPy**: For data processing and manipulation
- **Requests**: For downloading papers from arXiv
- **Python-dotenv**: For environment variable management

## Project Structure

- `requirements.txt`: Required Python packages
- `data_processor.py`: Script to download and index papers in ChromaDB
- `rag_engine.py`: Core RAG functionality using ChromaDB
- `app.py`: Streamlit application for the user interface
- `data/chroma_db/`: Directory where ChromaDB stores the vector database
- `data/papers.csv`: CSV file with downloaded paper metadata

## Customization

- **Paper Sources**: You can extend the `download_arxiv_dataset` function to include other sources
- **Response Types**: You can add new response types in the `generate_response` function
- **UI Customization**: Modify the Streamlit app to change the user interface

## Advantages of Using ChromaDB

- **Open Source**: Fully open-source and free to use
- **Local Operation**: Can run entirely on your local machine
- **Simple API**: Easy to use and understand
- **Efficient Storage**: Optimized for vector storage and retrieval
- **No External Dependencies**: Doesn't require external services or API keys (except OpenAI for enhanced responses)

## Troubleshooting

- **ChromaDB Connection Issues**: Make sure you've run the `data_processor.py` script first
- **No Results**: Try different queries or adjust the number of papers to retrieve
- **Slow Performance**: Try reducing the number of papers to retrieve or using a smaller embedding model
