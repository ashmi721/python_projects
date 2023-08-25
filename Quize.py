
import time
import random
def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def check_answer(user_answer, answer):
    return user_answer == answer

def main():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
            "answer": "2"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "2"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
            "answer": "2"
        },
        {
            "question": "which language used to develope facebook",
            "options": ["Js", "python", "java", "php"],
            "answer": "4"
        },
         {
            "question": "What is the capital of Australia?",
            "options": ["Canberra", "Delhi", "sidny", "Chennai"],
            "answer": "1"
        },
    {
        "question": "Who is the inventor of Python programming language?",
        "options": [ "Larry Page","Guido van Rossum", "Mark Zuckerberg", "Elon Musk"],
        "answer": "2"
    },
    {
        "question": "Which programming language is often used for web development?",
        "options": [ "Java", "HTML", "Python","Swift"],
        "answer": "3"  
    },
    {
        "question": "Which year was the C programming language developed?",
        "options": [ "1985","1970", "1995", "2000"],
        "answer": "2"  
    },
    {
        "question": "What does IDE stand for in programming?",
        "options": ["Internet Data Exchange", "Interpreted Design Entity", "Inherited Development Element","Integrated Development Environment"],
        "answer": "4" 
    }
           
    ]

    num_random_questions = 9  # Set the number of random questions you want to display
    
    # Randomly select a set of questions
    random_questions = random.sample(questions, num_random_questions)

    score = 0
    for i, question in enumerate(random_questions):
        print("\nGet ready for the next question...")
        time.sleep(2)
        print("\nHere's your question:")
        display_question(question["question"], question["options"])
        user_answer = input("Your answer (enter the option number): ")
        if check_answer(user_answer, question["answer"]):
            print("Correct answer!")
            score += 1
        else:
            print("Sorry, wrong answer!")
            break  # End the game if the answer is wrong

    print("\nGame Over!")
    print(f"You scored {score} point(s) out of {num_random_questions}.")

if __name__ == "__main__":
    main()