# AI-Privacy-Policy-Helper
A tool aimed to assist users with reading privacy policies.

# Setup
If you're setting up this application for the first time, navigate to the [Modelfiles directory](./Modelfiles/) and read the README.md to get started!

If you'd like to see the ideal usage of this application, read the [HowToUse.md](./HowToUse.md) markdown file.

## Problem Domain: *The Privacy Policy*
Privacy policies are, simply put, important. 
- Companies stay legally compliant by disclosing necessary privacy information to the user.
- The user is prompted to agree to the statements in this policy.

But still, many users opt to not read a privacy policy.
### Why?
1. The formatting of a policy can varies between companies.
2. Many existing privacy policy formats are not very user-friendly.
3. Legal terminology can make information much harder to process.

And the list goes on.

Overall, **there lacks a level of consistency.**

### Is there a way that we can introduce consistency into this process?

## The Solution: *Make Privacy Policies Universally Consistent*
### But... how?
This is the problem our project aims to tackle!

We will use an LLM that is prompt engineered to provide clear, concise summaries of specific sections of a privacy policy. This formatted text will then be passed into another LLM that will use these summaries to create a consistent privacy policy format out of it.

The LLMs will be locally hosted using [Ollama's open-source LLM library](https://ollama.com/search), and we will be using [Streamlit](https://streamlit.io/) to generate simplistic, consistent and digestible privacy policy interfaces!

## Purpose of this project

This project will initially serve as a proof-of-concept for future research in the domain of Natural Language Processing (NLP) and its usage in summarization that can be beneficial for human information processing.

