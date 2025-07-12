## Overview
The Research Assistant Agent is an AI-powered assistant that leverages language models and the Tavily search API to provide real-time, internet-enabled research capabilities. Designed for professionals, researchers, and students, this tool enables seamless access to up-to-date information and intelligent conversation.


## Open Source Tools Used
This project is built using the following open source libraries and frameworks:

- **[AutoGen](https://github.com/microsoft/autogen)**: Framework for building LLM-powered agents and tools.
- **[Tavily Python SDK](https://github.com/tavily/tavily-python)**: Python client for the Tavily search API.
- **[Pydantic](https://github.com/pydantic/pydantic)**: Data validation and settings management using Python type annotations.
- **[python-dotenv](https://github.com/theskumar/python-dotenv)**: Loads environment variables from a `.env` file.
- **[Groq Python SDK](https://github.com/groq/groq-python)**: Python client for interacting with Groq's language models.

## Features
- **Conversational AI**: Interact with a state-of-the-art language model for research and information retrieval.
- **Internet Search Integration**: Utilizes the Tavily API to fetch and summarize relevant web content.
- **Customizable Search**: Supports adjustable search depth and result limits for tailored information needs.
- **Environment Variable Support**: Securely manage API keys and configuration using `.env` files.

## Requirements
- Python 3.8+
- API keys for [Groq](https://groq.com/) and [Tavily](https://www.tavily.com/)

## Installation
1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   ```
2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables**
   - Create a `.env` file in the project root with the following content:
     ```env
     GROQ_API_KEY=your_groq_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```

## Usage
Run the main script to start the assistant:
```sh
python autogen_tavily.py
```
You can interact with the assistant via the command line. Type your research queries and receive summarized, relevant results. To exit, type `exit`, `quit`, or `bye`.


## Configuration
- **Language Model**: Configured in `core/llm_config.py` via the `llm_config` dictionary. Default model is `gemma2-9b-it`.
- **Search Parameters**: Adjust `max_results` and `search_depth` in the Tavily search input model in `core/tavily_search.py` as needed.


## File Structure
- `main.py` — Main application logic and agent setup
- `core/tavily_search.py` — Tavily search logic and input model
- `core/llm_config.py` — Language model configuration
- `requirements.txt` — Python dependencies
- `README.md` — Product documentation
- `documentation.html` — HTML file 

## License
This project is released under the MIT License.

## Contact
For support or inquiries, please contact the maintainer at priyaaggarwal27@gmail.com.
