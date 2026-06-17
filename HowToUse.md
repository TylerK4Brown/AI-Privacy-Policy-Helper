# How To Use the AI Privacy Policy Helper

After running `streamlit run home.py`, click on the first localhost link. You should land on this page:

<img width="2494" height="1245" alt="Screenshot 2026-06-16 183747" src="https://github.com/user-attachments/assets/6f5db90c-6a66-44e1-bc7c-d7decae2a41d" />

Enter some privacy policy text into the text box. [We've provided some sample privacy policy texts in the PrivacyPolicies directory](PrivacyPolicies/). Feel free to use these, or find your own privacy policy text to test out!

After you finish entering the text into the text box, click on the Generate Summary button. **Since this LLM is being hosted locally, the speed of the generated responses will vary based on your computer's hardware.**

There will be two responses from the LLM - one will be an intermediary debugging response with the header "Summary". It will look similar to this image below:

<img width="2350" height="639" alt="image" src="https://github.com/user-attachments/assets/59b2cc05-7bfc-4ba0-878c-1d627fd3fceb" />

The final response will be titled "Generated Webpage JSON". It will look similar to the image below:

<img width="2022" height="1159" alt="image" src="https://github.com/user-attachments/assets/70d7ea39-0c99-49ac-bc53-d1e358e8e5c2" />

Below the summary, there is a button titled "Go to Nutrition Label". When you click on this, you will see a "Nutrition Label-esc" format of the privacy policy text that was used as input.

<img width="2496" height="1162" alt="image" src="https://github.com/user-attachments/assets/ac091926-dfc7-403e-be5b-9ea213214da6" />

Click on the "Back" button to enter new privacy policy text, should you wish to do further testing.
