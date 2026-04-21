# Main Python file
#
# Our Python code will be responsible for:
# 1. Accepting user input for the privacy policy text
# 2. Calling upon the locally hosted LLM to generate a summary of the privacy policy text
# 3. Calling upon another LLM that will generate Streamlit code to display the summary in a user-friendly format
# 4. Pushing the generated Streamlit code to the Privacy-Policy-Webpage folder
#
# This will all be separated into functions at some point, but for now, this is a high-level summary of what will be happening
# This code is a very simple implementation of the first two steps, and will be expanded upon in the future.
# This is just to give an idea of what this may look like down the line.

import ollama, os

# Calls upon the locally hosted LLM to generate a summary of the privacy policy text
def privacy_policy_summary(privacy_policy_text, client):
    # Clear the console screen before generating the summary
    os.system("cls")
    print("Generating summary...")
    # Generate a response using a specific model
    privacy_policy_summarizer = "privacy-policy-summarizer"  # Model name
    response = client.generate(model=privacy_policy_summarizer, prompt=privacy_policy_text)
    return response.response

# Main function
def main():
    # Create a client to interact with the Ollama model, clear the console screen as well
    client = ollama.Client()
    os.system("cls")
    print("Welcome to the Privacy Policy Summarizer!")
    print("Please enter the text of the privacy policy you want to summarize: \n")
    # Accepts privacy policy text input from user
    privacy_policy_text = str(input())
    # Begin summarization process
    summary = privacy_policy_summary(privacy_policy_text, client)

    # clear console screen and display summary of the privacy policy
    os.system("cls")
    print("Summary of the Privacy Policy: ")
    print(summary)
    

if __name__ == "__main__":
    main()