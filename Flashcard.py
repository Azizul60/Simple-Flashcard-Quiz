import json
import time
import random
import os

def main():
    filename='Flashcard.json'
    questions=load_file(filename)
    print(" Start the quiz !")
    while True:
        
        simple_quiz(questions)
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again != 'yes':
            break



def load_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: The JSON file is invalid or empty.")
                return []
    else:
        print(f"Error: The file {filename} does not exist.")
        return []

def simple_quiz(questions):

    print(" Welcome to the Flashcard Quiz!")
    score=0
    
    random.shuffle(questions)
    
    for question in questions:

       
        print (f"\nWhat is the meaning of the word {question["word"]}")

        for options in question["definitions"]:
            print(options)

        start_time=time.time()

        answer= input("What is the correct defination :").upper()

        if time.time() - start_time>100:
            print("Time is up !")
        elif answer== question["correct_definition"]:
            print ("Correct ")
            score+=1
        else:
            print(f"the correct answer is {question["correct_definition"]}")
        
    print(f"\nQuiz finished! Your score: {score}")


if __name__=="__main__":
    main()