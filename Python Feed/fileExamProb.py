# Open the file
with open('Python Feed\QandA.txt', 'r') as file:
    # Initialize variables to store questions and answers
    questions = []
    answers = []
    
    # Read each line in the file
    for line in file:
        # Strip leading and trailing whitespace
        line = line.strip()
        
        # Check if the line starts with 'Q '
        if line.startswith('Q '):
            # Extract the question (excluding 'Q ')
            question = line[2:]
            questions.append(question)
        # Check if the line starts with 'A '
        elif line.startswith('A '):
            # Extract the answer (excluding 'A ')
            answer = line[2:]
            answers.append(answer)

# Print questions and answers
for q, a in zip(questions, answers):
    print("Question:", q)
    print("Answer:", a)
    print()  # Add an empty line between each question and answer pair
