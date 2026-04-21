# Purpose of this folder
Modelfiles are how we will prompt engineer our LLM.

**In this file, we can edit a few different things about our model:**

1. Which model we'll be using (right now it is set to cogito:8b - you can try out other models by visiting [this website](https://ollama.com/search)).
2. The context window of the model - how many tokens it can use to generate its next token
3. Temperature (range 0 - 1), where lower values provide more deterministic outputs, and higher values allow for more "creativity".
4. A system prompt, which will contain our prompt engineered instructions to the model.

Essentially, this folder will house the most important aspects of our project, since this LLM portion is the overall basis of our outputs.