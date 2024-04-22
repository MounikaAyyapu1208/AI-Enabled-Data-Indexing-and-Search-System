# AI-Enabled-Data-Indexing-and-Search-System

This project provides a comprehensive document search and analysis system built using Python and various libraries such as Flask, NLTK, and Gensim. The system allows users to search for information within a corpus of documents, perform spell correction and query expansion, and retrieve relevant search results.

## Description

The Document Search and Analysis system is designed to assist users in searching for specific information within a collection of documents, particularly focusing on topics related to technology and artificial intelligence. The system comprises several components:

- **Web Interface**: Users interact with the system through a web interface where they can enter search queries and view search results.
  
- **Crawler**: A web crawler is responsible for fetching relevant documents from specified sources, such as websites or databases. In this project, a crawler is implemented using Scrapy to retrieve documents from the Britannica website.

- **Indexer**: The Indexer component processes the fetched documents, extracts relevant content, and builds indices for efficient search operations. It utilizes techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) and word embedding models (Word2Vec) for document representation and indexing.

- **Query Engine**: The Query Engine processes user queries, performs spell correction and query expansion, and retrieves relevant search results from the document indices. It employs techniques like cosine similarity and faiss indexing for efficient similarity search.

## Key Features

- **Spell Correction**: The system automatically corrects spelling mistakes in user queries using NLTK's WordNet.
  
- **Query Expansion**: User queries are expanded using synonyms and related terms to improve search accuracy.
  
- **Web Interface**: A user-friendly web interface allows users to interact with the system and view search results.
  
- **Efficient Search**: Document indices are built using advanced indexing techniques for fast and accurate search operations.
  
- **Scalability**: The system is designed to scale with the size of the document corpus, allowing for efficient processing of large volumes of data.

## Dependencies

- **Python**: Programming language used for backend logic and web development.
  
- **Flask**: Web framework for building the web interface and handling user requests.
  
- **NLTK**: Natural Language Toolkit for text processing tasks such as spell correction and query expansion.
  
- **Scrapy**: Web crawling framework used to fetch documents from web sources.
  
- **Gensim**: Library for topic modeling, document similarity analysis, and word embedding models.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/document-search-analysis.git
cd document-search-analysis
```

2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python server.py
python Utilites.py
```

4. Access the web interface in your browser at `http://127.0.0.1:5001/`.

## Usage

1. Open the web interface in your browser.
  
2. Enter your query in the search box and press Enter.
  
3. View the search results displayed on the web interface.

## Acknowledgments

- This project makes use of various open-source libraries and tools, including Flask, NLTK, and Gensim.
