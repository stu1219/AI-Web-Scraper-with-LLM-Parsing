# AI-Web-Scraper-with-LLM-Parsing
AI Web Scraper with LLM Parsing - A Streamlit-based tool for scraping website content and extracting insights using Large Language Models (LLMs).

# Overview
This project is designed to streamline web scraping and content analysis by combining the power of web scraping with LLM-based parsing. It allows users to input a website URL, extract content, and use advanced language models to parse and analyze the data for specific queries.

# Features
Web Scraping: Scrape data from any website URL.
Content Cleaning: Processes raw HTML into clean text data.
LLM Parsing: Utilizes Large Language Models for natural language processing and data extraction.
User-Friendly UI: Built with Streamlit for an interactive and responsive interface.
Expandable Content Viewer: Displays scraped content in a collapsible view.
Custom Styling: Modern design with CSS enhancements.

# Installation and Setup
## Prerequisites
Python 3.8 or later
Pip (Python Package Manager)

## Clone the Repository
git clone https://github.com/username/AI-Web-Scraper-with-LLM-Parsing.git
cd AI-Web-Scraper-with-LLM-Parsing

## Install Dependencies
pip install -r requirements.txt

## Start the Application
streamlit run app.py

## Open in Browser
Visit the application at:localhost

## Usage Guide
Input Website URL: Enter the URL of the website to scrape.
Click on the 'Scrape Website' button.
View Scraped Content: Expand the 'View Scraped Content' section to see the raw extracted text.

## Parse Content with LLM: Describe the required information (e.g., Extract all product prices).
## Click 'Parse Content' to process the data.
## Get Results: View parsed insights directly on the screen.

# Key Components

## Functions
scrape_website(): Scrapes raw HTML content.
extract_body_content(): Extracts meaningful text from HTML.
clean_body_content(): Cleans and refines text content.
split_dom_content(): Splits DOM content into manageable parts.
parse_with_ollama(): Processes content using LLM for extracting structured insights.

# LLM Integration
The application leverages Ollama, a powerful LLM-based framework, for parsing text. It breaks down website data into structured parts and processes it based on user-defined queries, enabling seamless interaction with complex datasets.

# Error Handling
Invalid URL: Prompts users to enter a valid URL.
Parsing Errors: Displays details of issues during parsing.
Empty Queries: Reminds users to input query descriptions.

# Troubleshooting
## Port Already in Use:
Close any existing Streamlit sessions or specify a new port:
streamlit run app.py --server.port 8502

## Missing Dependencies:
Ensure all dependencies are installed:
pip install -r requirements.txt
LLM Parsing Errors:
Check query formats.
Verify Ollama setup and server availability.

## Future Enhancements
Multi-page Scraping: Enable scraping of multiple web pages.
Authentication Support: Handle login-based scraping.
Advanced NLP Features: Integrate NER and sentiment analysis.
Data Export Options: Provide CSV/JSON export options for parsed data.

## Contact
### Author: Sai Ram Gandla
Email: sairamgandla11@gmail.com
GitHub: github.com/stu1219

# License
© 2024 AI Web Scraper with LLM Parsing. All rights reserved.
