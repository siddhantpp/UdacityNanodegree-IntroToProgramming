# IPND Stage 2 Final Project

import sys

# --- GLOBAL VARIABLES ---
# Open files corresponding to each level, read and save paragraphs
easy_text_file = open("levels/easy/paragraph.txt")
easy_answers_file = open("levels/easy/answers.txt")
medium_text_file = open("levels/medium/paragraph.txt")
medium_answers_file = open("levels/medium/answers.txt")
hard_text_file = open("levels/hard/paragraph.txt")
hard_answers_file  = open("levels/hard/answers.txt")

easy_para = easy_text_file.read()
easy_answers = easy_answers_file.read().splitlines()

medium_para = medium_text_file.read()
medium_answers = medium_answers_file.read().splitlines()

hard_para = hard_text_file.read()
hard_answers = hard_answers_file.read().splitlines()

para_list = [easy_para, medium_para, hard_para]
answer_list = [easy_answers, medium_answers, hard_answers]

# --- HELPER FUNCTIONS ---
def endGame():
    ''' Force ends the game'''
    print
    sys.exit('Game over.')

def getResponseInLowerCase(message):
    ''' Input: Message to be used for requesting an input from the user
        Returns: The input as string with lower case '''
    return raw_input(message).lower()

def printBlock(message):
    ''' Input: Message to be printed
        Prints a block message '''
    print
    print message
    print

def getAttempts():
    ''' Returns: The number of allowed attempts defined by the user
        Allows the user to define the number of attempts for each answer.
        Assumes an initial value of 3 for the choice iteself '''
    print 'You need to make many choices in this game, but have a limited number of chances'
    print 'For instance, you now have 3 chances to set this limit.'
    attempts = 3
    while attempts > 0:
        print
        max_attempts = getResponseInLowerCase("Enter a maximum number of attempts that is greater than zero: ")
        if int(max_attempts) and int(max_attempts) > 0:
            return int(max_attempts)
        else:
            attempts -= 1
            if attempts > 0:
                print 'Invalid response. Please try again. You have ' + str(attempts) + ' chances left'
    print 'Sorry, you have exceeded the maximum number of allowed attempts.'
    return -1

def getLevel(allowed_attempts):
    ''' Inputs: The number of allowed attempts to select a level
        Returns: The level selected by the user as integer'''
    # could use a global variable for attempts outside, but keeping this function exportable
    print 'Select your difficulty level. Available choices are easy, medium and hard.'
    attempts = allowed_attempts
    while attempts > 0:
        level_string = getResponseInLowerCase("Type in your choice: ")
        if level_string == 'easy':
            print 'You have chosen Easy!'
            return 0
        elif level_string == 'medium':
            print 'You have chosen Medium!'
            return 1
        elif level_string == 'hard':
            print 'You have chosen Hard!'
            return 2
        else:
            attempts -= 1
            if attempts > 0:
                print 'Invalid choice! Please try again. You have ' + str(attempts) + ' chances left'
    print 'Sorry, you have exceeded the maximum number of allowed attempts.'
    return -1

def selectParagraph(level):
    ''' Input: Level selected, as number
        Returns: The corresponding paragraph '''
    if level == 0:
        return easy_para
    elif level == 1:
        return medium_para
    elif level == 2:
        return hard_para
    else:
        return None

def getBlanks(para):
    ''' Input: The paragraph
        Returns: number of blanks in the paragraph '''
    number = 1
    count = 0
    while para.find(str(number)) > -1:
        count += 1
        number += 1
    return count

def fillBlanks(originalString, blankNumber, answer):
    ''' Assumption: string does not otherwise contain numbers and all numbers are enclosed within
        opening and closing __
        Input: original string, blank number to fill, value to be filled
        Returns: The original string with blanks filled '''
    originalStringList = originalString.split()
    replacedList = []
    newString = originalString
    word = '__' + str(blankNumber) + '__'
    for item in originalStringList:
        if word in item:
            item = item.replace(word, answer)
        replacedList.append(item)
    newString = ' '.join(replacedList)
    return newString

def getCorrectAnswer(level, blankNumber):
    ''' Inputs: current level, blank number
        Returns: correct answer for blank at that level '''
    return answer_list[level][blankNumber - 1]

def isCorrectAnswer(level, blankNumber, answer):
    ''' Inputs: current level, blank number, user's answer
        Returns: True if answer matches, False if not '''
    correctAnswer = getCorrectAnswer(level, blankNumber)
    return correctAnswer.lower() == answer

def checkAnswers(level, attempts):
    ''' Inputs: current level, number of attempts allowed
        Returns: Boolean corresponding to all answers being correct or not, the paragraph with
        correct answers replaced '''
    attempts_left = attempts
    para = selectParagraph(level)
    blanksToFill = getBlanks(para)
    currentBlank = 1
    while blanksToFill > 0:
        printBlock('The paragraph in its current state is:\n' + para)
        answer = getResponseInLowerCase('Enter your answer for __' + str(currentBlank) + '__: ')
        if isCorrectAnswer(level, currentBlank, answer):
            printBlock('Correct!')
            correctAnswer = getCorrectAnswer(level, currentBlank)
            para = fillBlanks(para, currentBlank, correctAnswer)
            attempts_left = attempts
            currentBlank += 1
            blanksToFill -= 1
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print 'Incorrect response. ' + str(attempts_left) + ' chances left.'
            else:
                print 'You have run out of attempts'
                return [False, para]
    return [True, para]

# --- MAIN FUNCTION ---
def runGame():
    ''' Calls helper functions and controls execution '''
    printBlock('Welcome to pyWise v1.0 - A Python refresher game by Siddhant Pardeshi')
    attempts = getAttempts()
    if attempts > -1:
        level = getLevel(attempts)
        if level > -1:
            answerState = checkAnswers(level, attempts)
            if (answerState[0] == True):
                printBlock(answerState[1])
                printBlock('You Win! Well done.')
                return 0
            else:
                endGame()
        else:
            endGame()
    else:
        endGame()

runGame()
