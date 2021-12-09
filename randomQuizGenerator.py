#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key
import random

#The quiz data. Keys are states and values are their capitals.
capitals={'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
          'Arkansas':'Little Rock','California':'Sacramento','Colorado':'Denver',
          'Connecticut':'Hartford','Dellaware':'Dover','Florida':'Tallahassee',
          'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise','Illinois':'Springfield','Indiana':'Indianapolis', ' Iowa': 'Des Moines','Kansas':'Topeka','Kentucky':' Frankfort', 'Louisiana':' Baton Rouge',
          'Augusta':'Maryland',
          'Maine':'Annapolis','Massachusetts': ' Boston',  'Michigan':'Lansing', 'Minnesota': 'Saint Paul','Mississippi': 'Jackson', 'Missouri':'Jefferson City','Montana':'Helena',
          'Nebraska':'Lincoln','Nevada':'Carson City', 'New Hampshire': ' Concord','New Jersey': 'Trenton','Mexico':'Santa Fe','New York': 'Albany', ' North Carolina': ' Raleigh',
          'North Dakota': 'Bismarck', 'Ohio': 'Columbus', ' Oklahoma': 'Oklahoma City','Oregon':'Salem',' Pennsylvania': ' Harrisburg','Rhode Island': 'Providence ' ,'South Carolina': ' Columbia',' South Dakota' : 'Pierre','Tennessee':'Nashville','Texas':'Austin', 'Utah':'Salt Lake City', 'Vermont':
          'Montpelier', 'Virginia':' Richmond','Washington': 'Olympia', 'Virginia':'Charleston','Wisconsin':'Madison', 'Wyoming':'Cheyenne '}

#There are 49 questions in total

# Generate 35 quiz files .
for quizNum in range(35):
    #Todo:Create the quiz and answer key files
    quizFile=open(f'capitalsquiz{quizNum+1}.txt','w')
    answerKeyFile=open(f'capitalsquiz_answers{quizNum+1}.txt','w')
    #write out the header for the quiz.
    quizFile.write(('  '*20)+f'State Capitals Quiz (Form{quizNum+1})')
    quizFile.write('\n\n')

    #Shuffle the order of the states.
    states=list(capitals.keys())
    random.shuffle(states)
    
    #Todo:Loop through all 50 states, making a question for each
    for questionNum in range(49):
        #get right and wrong answers.
        correctAnswer=capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswer]
        random.shuffle(answerOptions)

        #Todo:Write the question and answer options to the quiz file
        quizFile.write(f'{questionNum+1}.What  is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}.{answerOptions[i]}\n")
        quizFile.write('\n')
        
        #Todo:Write the answer key to a file
        answerKeyFile.write(f"{questionNum+1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
    quizFile.close()
    answerKeyFile.close()
    

