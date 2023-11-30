import re
import pandas as pd

# Read the text data from the file
with open('questionbank.txt', 'r', encoding='utf-8') as file:
    text_data = file.read()

# Use regex to find matches for questions and answers
matches = re.findall(r'question-(.*?)(?:ans-(.*?)(?=(question-|$)))', text_data, re.DOTALL)

# Initialize lists to store questions and answers
questions = []
answers = []

# Process each match to extract questions and answers
for match in matches:
    question = match[0].strip()
    answer = match[1].strip() if match[1] else ''  # Handle the case where the answer is empty
    
    questions.append(question)
    answers.append(answer)

# Create a DataFrame
df = pd.DataFrame({'Question': questions, 'Answer': answers})

# Save to CSV with UTF-8 encoding
df.to_csv('questions_and_answers.csv', index=False, encoding='utf-8')
