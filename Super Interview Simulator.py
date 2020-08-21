import time
#from threading import Thread
#from threading import Timer
import random
#import sys
import numpy as np
import pandas as pd
#import threading

questions = pd.read_excel("questions.xlsx")

p_controls = {0: "Start answering question", 1: "Check time remaining", 2: "Exit interview simulator"}
a_controls = {0: "Move on to next question", 1: "Check time remaining", 2: "Exit interview simulator"}
q_types = ["intro", "motivational", "behavioural"]

class Interviewee(object):

    def __init__(self, name, company, role):
        self.name = name
        self.company = company
        self.role = role

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def get_role(self):
        return self.role

'''
class Timer(object):
    def __init__(self, t):
        self.running = True
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            t -= 1
        self.running = False
        print('Time\'s up!')

    def is_running(self):
        return self.running
'''

'''
class MyThread(Thread):
    def __init__(self, time):
        Thread.__init__(self)
        self.start()
        self.time_allotted = time
        self.time_remaining = time

    def run(self):
        while self.time_remaining > 0:
            self.time_remaining -= 1
            print('{:02d}:{:02d}'.format(self.time_remaining // 60, self.time_remaining % 60))
            time.sleep(1)

'''

class Question(object):
    def __init__(self, q_code, question, category, prep_time, q_time):
        self.q_code = q_code
        self.question = question
        self.category = category
        self.prep_time = prep_time
        self.q_time = q_time



    def start_question(self):

        input("Are you ready? Enter any key to start the question.")

        self.print_q_preamble()
        print("Begin prep time")
        #self.print_prep_preamble()

        self.prep_timer()

        print("\n")

        print("Begin answer time")
        #self.print_ans_preamble()

        self.ans_timer()

        print("\nTime's up!\n")

        return

    def prep_timer(self):
        time_left = self.prep_time
        for x in range(self.prep_time):
            #print(x, end = "\r")
            time_left -= 1
            print('\r{:02d}:{:02d}'.format(time_left // 60, time_left % 60), end="")
            time.sleep(1)

        return

    '''
    def prep_timer(self):
        def countdown():
            global time_left

            time_left = self.prep_time
            for x in range(self.prep_time):
                print('{:02d}:{:02d}'.format(time_left // 60, time_left % 60), end = "\r")
                time_left -= 1
                time.sleep(1)

            return

        timer = threading.Thread(target = countdown)
        timer.start()

        while time_left > 0:
            pass
        
        while time_left > 0:
            command = int(input("Command: "))
            if command == 0:
                return
            elif command == 1:
                print('{:02d}:{:02d}'.format(time_left // 60, time_left % 60))
            elif command == 2:
                print("Goodbye!")
                command = input("Enter any key to exit.")
                sys.exit(0)
        
    '''

    def ans_timer(self):
        time_left = self.q_time
        for x in range(self.q_time):
            #print(x, end = "\r")
            time_left -= 1
            print('\r{:02d}:{:02d}'.format(time_left // 60, time_left % 60), end="")
            time.sleep(1)
        return

    '''
    def prep_countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            t -= 1
        print('Time\'s up!')
    '''

    def print_q_preamble(self):
        print(self.question)
        print("Prep time: %d seconds" % self.prep_time)
        print("Answer time: %d seconds" % self.q_time)


    def print_prep_preamble(self):
        for i in p_controls:
            print("{0}: {1}".format(i, p_controls[i]))

    def print_ans_preamble(self):
        for i in a_controls:
            print("{0}: {1}".format(i, a_controls[i]))

    def get_time_remaining(self, time_allotted, start_time, end_time):
        print("You have %d seconds remaining." % int(time_allotted - (end_time - start_time)))
        return



#Interviewee settings
def question_category(category, number_of_questions):
    current_question_set = random.sample(list(questions[questions["type"] == category]["q_code"]), number_of_questions)
    for i in current_question_set:
        current_question = Question(i,
                                    np.array(questions[questions["q_code"] == i]["question"])[0],
                                    np.array(questions[questions["q_code"] == i]["type"])[0],
                                    np.array(questions[questions["q_code"] == i]["prep_time"])[0],
                                    np.array(questions[questions["q_code"] == i]["q_time"])[0])
        current_question.start_question()

#Questions
if __name__ == '__main__':
    print("Hello, and welcome to your interview.")
    time.sleep(1)

    intro_number = int(input("Let's get started with introductory questions. How many questions do you want? "))
    time.sleep(1)
    question_category("intro", intro_number)

    motivations_number = int(input("Now I'm going to ask some questions about your motivations. How many questions do you want? "))
    time.sleep(1)
    question_category("motivational", motivations_number)

    technicals_number = int(input("Next, I want to ask you a couple of technical questions. How many questions do you want? "))
    time.sleep(1)
    question_category("data_sci", technicals_number)

    behaviourals_number = int(input("Lastly, I'm going to ask you a few behavioural questions. How many questions do you want? "))
    time.sleep(1)
    question_category("behavioural", behaviourals_number)

    time.sleep(1)
    input("That concludes the interview. Do you have any questions for me? (Enter any key to finish the interview)")



'''
To do:
-Fix the goddamn timer
'''
