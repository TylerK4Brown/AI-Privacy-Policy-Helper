# Purpose of this folder
This is where the templates for our privacy policy formats will be stored.

## Important note
You will have to pip install the requirements from requirements.txt to load this website properly.
1. Open a command prompt window and navigate to your AI-Privacy-Policy-Helper folder.
2. Type this command: ``pip install -r requirements.txt``
3. Once this process is finished, navigate into the Privacy-Policy-Templates folder.
4. Type this command: ``streamlit run home_page.py``
5. The landing page should load in a new browser window!
##
We will be using the Python library [Streamlit](https://streamlit.io/) to make our formats, and these formats will be used by the LLM that is responsible for turning summarizations of privacy policies into consistently formatted web pages.

[Streamlit Components](https://streamlit.io/components) seem to be a good place to start, so we'll try to leverage as many of these as possible to make nice-looking privacy policies!
