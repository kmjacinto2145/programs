#!/usr/bin/env python
# coding: utf-8

# In[2]:


##Interview Simulator with Python##

#Imports required libraries
import time
import random
import sys
import pandas as pd


# In[3]:


#Creates a Pandas dataframe showing the questions, the types of question, and the time taken to answer each question
time_df = pd.DataFrame(columns = ['Question Type', 'Question', 'Time Taken'])

#Delays the program for t seconds.
def wait_t_seconds(t):
    now = time.time()
    future = now + t
    while time.time() < future:
        pass
    
#Displays the controls for the types of organisations the user might be interviewing with
def organisation_dialogue():
    for i in types_dictionary:
        print('{0}: {1}'.format(i, types_dictionary[i]))
    
#Displays a dialogue asking the interviewee if they would like to change their profile before the interview begins
def profile_dialogue():
    print('Y: Yes')
    print('N: Change profile')
    print('E: Exit interview simulator')

#Prints the time elapsed from the start of the question.
def stopwatch(start, end):
    interval = end - start
    minutes = int(interval / 60)
    seconds = int(interval % 60)
    print('{:d}:{:02d}'.format(minutes, seconds))
    
def time_to_add(start, end):
    interval = end - start
    minutes = int(interval / 60)
    seconds = int(interval % 60)
    return '{:d}:{:02d}'.format(minutes, seconds)

#Prints the question controls.
def display_controls():
    print('N: Move to the next question')
    print('T: Check time elapsed')
    print('E: Exit interview simulator')

#Prints a warning and controls asking the user if they are certain they want to exit the simulator.
def display_exit_controls():
    print('Are you sure you want to exit?')
    print('Y: Yes')
    print('N: No') 
    
#Template code for exiting the simulator
def sim_exit():
    display_exit_controls()
    command = input()
    while (command != 'N') and (command != 'n'):
        if (command == 'Y') or (command == 'y'):
            print('Goodbye.')
            wait_t_seconds(1.5)
            sys.exit(0)
        command = input()
    print('Returning to question menu.')    
    
#Exits the simulator (used in introduction only)
def sim_exit_intro():
    sim_exit()
    profile_dialogue()
    
#Exits the simulator (used for questions only)
def sim_exit_question():
    sim_exit()
    display_controls()
        
#Runs a given question    
def question(q_type, question, count):
    global time_df
    print('{0} Question {1}: {2}\n'.format(q_type, count, question))
    wait_t_seconds(2) 
    display_controls()
    start = time.time()
    command = input()
    while (command != 'N') and (command != 'n'):
        if (command == 'T') or (command == 't'):
            #Displays the time elapsed from the start of the question.
            now = time.time()
            stopwatch(start, now)
        elif (command == 'E') or (command == 'e'):
            sim_exit_question()
        command = input()
    now = time.time()
    question_stats = pd.DataFrame(
        {
            "Question Type" : [q_type], 
            "Question": [question], 
            "Time Taken": [time_to_add(start, now)]
        }
    )
    time_df = time_df.append(question_stats, ignore_index = True)


# In[4]:


#Pre-simulator questions
print('Hello, and Welcome to the Interview Simulator! Before we begin...\n')
wait_t_seconds(2)
print('What is your first name?')
name = input()
print('Hi %s! What is the name of the organisation you are interviewing with?' % name)
company = input()

'''
print('How would you best describe this organisation?')
organisation_dialogue()
org_type = int(input())
types_dictionary = {
    1: 'Corporate', 
    2: 'Government', 
    3: 'Startup',
    4: 'Social Enterprise',
    5: 'University Society'
}
while org_type not in list(types_dictionary.keys()):
    print('Please try again.')  
    org_type = int(input())
'''
    
print('What is the name of the role you are applying for?')
role = input()
print('Alright. Let\'s begin!\n')
wait_t_seconds(5)


# In[5]:


#Introduction
profile_set = False
while(profile_set is False):
    print('Hello {0}, and welcome to your interview for {1}.'.format(name, company))
    wait_t_seconds(2)   
    print('According to your application you are applying for the role of %s, right?' % role)
    wait_t_seconds(2)
    profile_dialogue()
    command = ''
    while (command != 'Y') and (command != 'y') and (command != 'N') and (command != 'n'):
        #Allows the user to reset their profile details.
        command = input()
        if (command == 'Y') or (command == 'y'):
            profile_set = True
            break
        elif (command == 'N') or (command == 'n'):
            print('What is your first name?')
            name = input()
            print('Hi %s! What is the name of the organisation you are interviewing with?' % name)
            company = input()
            print('What is the name of the role you are applying for?')
            role = input()
            print('Alright. Let\'s return to the interview.\n')
            wait_t_seconds(2)
            break
        elif (command == 'E') or (command == 'e'):
            sim_exit_intro()        


# In[ ]:


#Question sets
openers = [
    'Tell me a little bit about yourself.',
    'If your friends or work colleagues could describe you in three words, what would they be?',
    'If I were to call your current boss right now, what would he or she say about you?',
    'If you could be an animal, what would it be and why?',
    'If you could be a fruit, what would it be and why?',
    'If you could go on holidays anywhere, where would it be?',
]

motivationals = [
    'Why do you want to work for %s?' % company,
    'Why do you want to work as a(n) %s?' % role,
    'What made you choose your university degree?',
    'Why did you choose %s over some of our competitors?' % company,
    'What makes you a good %s?' % role,
    'Tell me everything you know about our company\'s product offering.',
    'Tell me everything you know about our company\'s leadership.',
    'What do you think the ideal company culture is?',
    'How did you learn about this role?',
    'Describe your dream job.',
    'What do you expect to achieve in the first 100 days after we hire you?'
]

personals = [
    'What are your biggest strengths and weaknesses?',
    'What is your greatest accomplishment?',
    'What is your plan over the next five years?',
    'What was your biggest failure?',
    'What motivates you in life?',
    'What has been your favourite university course?',
    'Tell us about a project or new idea you pursued recently.',
    'At %s, we pride ourselves on diversity in the workplace. Tell me, what does diversity mean to you?' % company,
    'Do you prefer a more laid-back or more fast-paced working environment and why?'
]

behaviourals = [
    'Tell us a time you were under pressure. How did you deal with it?',
    'Tell us a time you did multiple jobs at once',
    'Tell us a time when your commitments clashed.',
    'Tell us a time when you paid attention to detail.',
    'What is your role in a team? Give me an example of when you played this role.',
    'Tell us a time when you had to work with someone who you didn\'t like or was uncooperative.',
    'Tell us a time you went above and beyond.',
    'Tell us a time you had to make a difficult decision.',
    'Tell us a time you experienced a diverse team.',
    'Tell us a time you had to adapt to a change quickly.',
    'Tell us a time you had to make a last-second change.',
    'Tell us a time you had to learn something quickly.'
]

situationals = [
    'You are running an event or meeting featuring a guest speaker. ' 
    'However, on the morning, the guest speaker calls in sick and is unable to attend. What do you do?',
    'You are working on a project with two other individuals. However, one of them is repeatedly either late '
    'or absent to meetings, and is struggling to meet deadlines. How would you deal with this situation?'
]

market_sizers = [
    'How many chairs are there in Australia?',
    'How many chairs are there in Sydney',
    'How many steps are taken in Sydney per day?',
    'How many windows are there in Sydney?',
    'How many tennis balls can you fit in ANZ Stadium?',
    'How many cars cross the Harbour Bridge per day?'
]


# In[ ]:


'''
Future modifications:
-Displaying hints for the questions using dictionaries
-Linking to audio clips
-Enabling the user to record their responses
'''


# In[1]:


#Opening questions   
print('Great.')
wait_t_seconds(2)    
q_type = 'Icebreaker'
print('Let\'s start with some icebreaker questions. I\'d like to get to know you a little more.\n')
wait_t_seconds(2)   
count = 1
total_questions = random.sample(range(1, 3), 1)[0]
opener_questions = random.sample(range(0, len(openers)), total_questions)
while count <= len(opener_questions):
    question(q_type, openers[opener_questions[count - 1]], count)
    print('\n')
    count += 1
    wait_t_seconds(2)  

#Chooses between motivational and individual questions to complete first.
motivations_vs_individuals = random.sample(range(0, 2), 1)[0]
wait_t_seconds(2)       

#Motivational and personal questions
if motivations_vs_individuals == 0:
    #Motivational questions
    q_type = 'Motivations'
    print('Now, I am going to ask you some questions on your motivations for the role.\n')
    wait_t_seconds(2)   
    count = 1
    total_questions = random.sample(range(2, 4), 1)[0]
    motive_questions = random.sample(range(0, len(motivationals)), total_questions)
    while count <= len(motive_questions):
        question(q_type, motivationals[motive_questions[count - 1]], count)
        print('\n')
        count += 1
        wait_t_seconds(2)    

    #Personal questions
    wait_t_seconds(2) 
    q_type = 'Personal'
    print('Thanks %s. Next, I am going to ask you some questions on how you are as an individual.\n' % name)
    wait_t_seconds(2)   
    count = 1
    personal_questions = random.sample(range(0, len(personals)), 2)
    while count <= len(personal_questions):
        question(q_type, personals[personal_questions[count - 1]], count)
        print('\n')
        count += 1
        wait_t_seconds(2)              
else:
    #Personal questions
    q_type = 'Personal'
    print('Thanks %s. Next, I am going to ask you some questions on how you are as an individual.\n' % name)
    wait_t_seconds(2)   
    count = 1
    personal_questions = random.sample(range(0, len(personals)), 2)
    while count <= len(personal_questions):
        question(q_type, personals[personal_questions[count - 1]], count)
        print('\n')
        count += 1
        wait_t_seconds(2)    
        
    #Motivational questions
    wait_t_seconds(2)       
    q_type = 'Motivations'
    print('Now, I am going to ask you some questions on your motivations for the role.\n')
    wait_t_seconds(2)   
    count = 1
    total_questions = random.sample(range(2, 4), 1)[0]
    motive_questions = random.sample(range(0, len(motivationals)), total_questions)
    while count <= len(motive_questions):
        question(q_type, motivationals[motive_questions[count - 1]], count)
        print('\n')
        count += 1
        wait_t_seconds(2)   

#Chooses between behavioural and situational questions to complete first.
behaviourals_vs_situationals = random.sample(range(0, 2), 1)[0]
wait_t_seconds(2)       

#Behavioural and situational questions
if behaviourals_vs_situationals == 0:
    #Behavioural questions
    q_type = 'Behavioural'
    print('Alright, now I\'m going to ask you a couple of behavioural questions.\n')
    wait_t_seconds(2)
    count = 1
    total_questions = random.sample(range(2, 4), 1)[0]
    behavioural_questions = random.sample(range(0, len(behaviourals)), 2)
    while count <= len(behavioural_questions):
        question(q_type, behaviourals[behavioural_questions[count - 1]], count)
        print('\n')
        count += 1
        wait_t_seconds(2)
        
    #Situational questions
    wait_t_seconds(2)
    q_type = 'Situational'
    print('Moving on, now we\'re heading into the situational questions.\n')
    wait_t_seconds(2)   
    count = 1
    situational_questions = random.sample(range(0, len(situationals)), 1)
    while count <= len(situational_questions):
        question(q_type, situationals[situational_questions[count - 1]], count)
        print('\n')
        count += 1
        wait_t_seconds(2)   
else:
    #Situational questions
    q_type = 'Situational'
    print('Moving on, now we\'re heading into the situational questions.\n')
    wait_t_seconds(2)
    count = 1
    situational_questions = random.sample(range(0, len(situationals)), 1)
    while count <= len(situational_questions):
        question(q_type, situationals[situational_questions[count - 1]], count)
        print('\n')
        count += 1
        wait_t_seconds(2)  
    
    #Behavioural questions
    wait_t_seconds(2)   
    q_type = 'Behavioural'
    print('Alright, now I\'m going to ask you a couple of behavioural questions.\n')
    wait_t_seconds(2) 
    count = 1
    total_questions = random.sample(range(2, 4), 1)[0]
    behavioural_questions = random.sample(range(0, len(behaviourals)), 2)
    while count <= len(behavioural_questions):
        question(q_type, behaviourals[behavioural_questions[count - 1]], count)
        print('\n')
        count += 1
        wait_t_seconds(2)    
        
wait_t_seconds(2)

#Conclusion of the interivew
print('That wraps up the formal part of the interview.')
wait_t_seconds(2)
print('Do you have any questions for me?\n')
wait_t_seconds(2) 
print('C: Complete the interview')
print('T: Check time elapsed')
print('E: Exit interview simulator')
start = time.time()
command = input()
while (command != 'C') and (command != 'c'):
    if (command == 'T') or (command == 't'):
        now = time.time()
        stopwatch(start, now)
    if (command == 'E') or (command == 'e'):
        sim_exit_question()
    command = input()
now = time.time()
question_stats = pd.DataFrame(
    {
        "Question Type" : ['Conclusion'], 
        "Question": ['Do you have any questions for me?'], 
        "Time Taken": [time_to_add(start, now)]
    }
)
time_df = time_df.append(question_stats, ignore_index = True)

print('Alright, that concludes the interview. Thanks for coming, %s!' % name)
wait_t_seconds(2)
print('We will let you know the outcome by next week.\n')
wait_t_seconds(4)

print('Congratulations on finishing the interview simulator!')
wait_t_seconds(2)
print('Here are your times for each question in the interview:')
wait_t_seconds(1)
print(time_df.to_string(index = False))

print('Press E to exit.')
command = ''
while (command != 'E') and (command != 'e'):
    command = input()

