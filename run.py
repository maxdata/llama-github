from llama_github import GithubRAG

def main():
    # Initialize GithubRAG with your credentials
    github_rag = GithubRAG(
        github_access_token="your_github_access_token", 
        openai_api_key="your_openai_api_key",
        jina_api_key="your_jina_api_key"
    )

    # Retrieve context for a coding question
    query = "How to create a NumPy array in Python?"
    context = github_rag.retrieve_context(query)

    print(context)

if __name__ == "__main__":
    main()