import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import time
from rag_engine import RAGEngine

# Load environment variables
load_dotenv()

# Initialize RAG engine
rag_engine = RAGEngine()

# Set page configuration
st.set_page_config(
    page_title="Literature Review Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def display_paper_details(paper):
    """Display details of a paper in an expandable container"""
    with st.expander(f"📄 {paper.metadata.get('title', 'N/A')}"):
        st.markdown(f"**Authors:** {paper.metadata.get('authors', '')}")
        st.markdown(f"**Source:** {paper.metadata.get('source', 'N/A')} | **Date:** {paper.metadata.get('date', 'N/A')}")
        st.markdown(f"**Categories:** {paper.metadata.get('categories', 'N/A')}")
        
        # Extract abstract from the document
        document = paper.document
        abstract = document
        if "Title:" in document and "Abstract:" in document:
            abstract = document.split("Abstract:", 1)[1].strip()
        
        st.markdown(f"**Abstract:** {abstract}")
        st.markdown(f"**Relevance Score:** {paper.score:.4f}")
        
        # Add a button to save the paper to a personal collection (demo feature)
        if st.button("Save to Collection", key=f"save_{paper.id}"):
            st.success("Paper saved to your collection! (Demo feature)")

def generate_sample_query():
    """Generate a sample query for demonstration purposes"""
    sample_queries = [
        "What are the latest advancements in transformer models for natural language processing?",
        "How is reinforcement learning being applied to robotics?",
        "Compare supervised and unsupervised learning approaches for image classification.",
        "What are the ethical considerations in developing AI for healthcare applications?",
        "How are graph neural networks used for recommendation systems?",
        "What are the current challenges in federated learning?"
    ]
    return sample_queries[int(time.time()) % len(sample_queries)]

def main():
    # Sidebar
    with st.sidebar:
        st.markdown("# 📚")
        st.title("Literature Review Assistant")
        st.title("Literature Review Assistant")
        st.markdown("*Your AI research companion*")
        
        st.markdown("---")
        st.markdown("## Settings")
        
        # Number of papers to retrieve
        top_k = st.slider("Number of papers to retrieve", min_value=1, max_value=10, value=5)
        
        # Response type
        response_type = st.selectbox(
            "Response type",
            options=["general", "summary", "comparison", "future_research"],
            format_func=lambda x: {
                "general": "General Response",
                "summary": "Comprehensive Summary",
                "comparison": "Comparison Analysis",
                "future_research": "Future Research Directions"
            }[x]
        )
        
        st.markdown("---")
        st.markdown("## About")
        st.markdown("""
        This application helps researchers explore academic literature using AI.
        
        1. Enter your research question
        2. Review the retrieved papers
        3. Get AI-generated insights
        
        Built with Streamlit, ChromaDB, and vector search.
        """)
    
    # Main content
    st.title("🔍 Research Question Explorer")
    
    # Query input
    query = st.text_area(
        "Enter your research question",
        height=100,
        placeholder=generate_sample_query()
    )
    
    col1, col2 = st.columns([1, 5])
    
    with col1:
        search_button = st.button("Search", type="primary", use_container_width=True)
    
    with col2:
        sample_button = st.button("Try a sample question", use_container_width=True)
    
    # Process query when button is clicked
    if search_button and query:
        with st.spinner("Searching for relevant papers..."):
            result = rag_engine.process_query(query, top_k=top_k, response_type=response_type)
        
        # Display results
        st.markdown("---")
        st.subheader("🤖 AI Research Assistant Response")
        st.markdown(result["response"])
        
        st.markdown("---")
        st.subheader(f"📚 Top {len(result['papers'])} Relevant Papers")
        
        # Display paper details
        for paper in result["papers"]:
            display_paper_details(paper)
        
        # Save session data
        st.session_state.last_query = query
        st.session_state.last_result = result
    
    # Try a sample question
    elif sample_button:
        sample_query = generate_sample_query()
        st.session_state.query = sample_query
        
        with st.spinner(f"Trying sample question: {sample_query}"):
            result = rag_engine.process_query(sample_query, top_k=top_k, response_type=response_type)
        
        # Display results
        st.markdown("---")
        st.subheader("🤖 AI Research Assistant Response")
        st.markdown(result["response"])
        
        st.markdown("---")
        st.subheader(f"📚 Top {len(result['papers'])} Relevant Papers")
        
        # Display paper details
        for paper in result["papers"]:
            display_paper_details(paper)
        
        # Update the text area with the sample query
        st.session_state.last_query = sample_query
        st.session_state.last_result = result
    
    # Show last query result if available
    elif hasattr(st.session_state, 'last_result'):
        st.markdown("---")
        st.subheader("🤖 Previous AI Research Assistant Response")
        st.markdown(st.session_state.last_result["response"])
        
        st.markdown("---")
        st.subheader(f"📚 Previously Retrieved Papers")
        
        # Display paper details
        for paper in st.session_state.last_result["papers"]:
            display_paper_details(paper)

if __name__ == "__main__":
    main()