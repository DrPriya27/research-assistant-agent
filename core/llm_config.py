import os

llm_config = {
    "config_list": [
        {
            "model": "gemma2-9b-it",
            "api_key": os.getenv("GROQ_API_KEY"),
            "api_type": "groq",
        }
    ]
}
