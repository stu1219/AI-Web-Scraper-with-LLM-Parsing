import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

# Custom Styles
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 24px;
            margin: 10px 0;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            background-color: #ffffff;
            color: #333333;
            font-size: 16px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .stExpander>summary {
            font-size: 18px;
            font-weight: bold;
            color: #4CAF50;
            cursor: pointer;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            background-color: #f1f1f1;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
            color: black;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit UI - Title and Description
st.title("🌐 Interactive AI Web Scraper")
st.markdown(
    """
    **Welcome to the AI Web Scraper Tool!**  
    🧹 Use this tool to scrape and analyze the content of any website effortlessly.  
    🔍 Enter a URL and let the scraper do the rest.  
    ✨ Ask specific questions about the content, and our AI model will fetch the details for you!
    """
)

# Input for Website URL
url = st.text_input("🔗 Enter Website URL:", placeholder="https://example.com")

# Step 1: Scrape the Website
if st.button("🧹 Scrape Website"):
    if url.strip():
        st.info("🔄 Scraping the website, please wait...")

        try:
            # Scrape the website
            dom_content = scrape_website(url)
            body_content = extract_body_content(dom_content)
            cleaned_content = clean_body_content(body_content)

            # Store the DOM content in Streamlit session state
            st.session_state.dom_content = cleaned_content

            # Display the DOM content in an expandable text box
            with st.expander("🗄 View Scraped Content"):
                st.text_area("DOM Content", cleaned_content, height=300)
        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")
    else:
        st.error("⚠️ Please enter a valid URL before proceeding.")

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area(
        "❓ Describe what you want to extract:", 
        placeholder="e.g., Extract all product prices or Extract headings..."
    )

    if st.button("🤖 Parse Content"):
        if parse_description.strip():
            st.info("🔍 Parsing the content...")
            try:
                # Parse the content with Ollama
                dom_chunks = split_dom_content(st.session_state.dom_content)
                parsed_result = parse_with_ollama(dom_chunks, parse_description)
                st.success("✅ Parsed Result:")
                st.write(parsed_result)
            except Exception as e:
                st.error(f"❌ Error occurred: {str(e)}")
        else:
            st.error("⚠️ Please describe what you want to extract.")

# Footer
st.markdown(
    '<div class="footer">© 2024 AI Web Scraper Project. All rights reserved.</div>',
    unsafe_allow_html=True
)
