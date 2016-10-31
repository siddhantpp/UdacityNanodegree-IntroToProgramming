# IPND Stage 2 Final Project

# --- GLOBAL IMPORTS ---
import sys

# --- GLOBAL CONSTANTS ---
MIN_COUNT = 0
INITIAL_MIN_ATTEMPTS = 3
INVALID_MIN_RETURN_VALUE = -1

LIST_INDEX_LEVEL_EASY = 0
LIST_INDEX_LEVEL_MEDIUM = 1
LIST_INDEX_LEVEL_HARD = 2

NORMAL_PROGRAM_EXIT_CODE = 0

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
''' The LIST_INDEX_LEVEL_xxxx constants defined in GLOBAL CONSTANTS correspond to the indexes of the
    below list '''
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
        Assumes an initial value for the choice iteself '''
    print 'You need to make many choices in this game, but have a limited number of chances'
    print 'For instance, you now have ' + str(INITIAL_MIN_ATTEMPTS) + ' chances to set this limit.'
    attempts = INITIAL_MIN_ATTEMPTS
    while attempts > MIN_COUNT:
        print
        max_attempts = getResponseInLowerCase("Enter a maximum number of attempts that is greater than zero: ")
        if int(max_attempts) and int(max_attempts) > MIN_COUNT:
            return int(max_attempts)
        else:
            attempts -= 1
            if attempts > MIN_COUNT:
                print 'Invalid response. Please try again. You have ' + str(attempts) + ' chances left'
    print 'Sorry, you have exceeded the maximum number of allowed attempts.'
    return INVALID_MIN_RETURN_VALUE

def getLevel(allowed_attempts):
    ''' Inputs: The number of allowed attempts to select a level
        Returns: The level selected by the user as integer'''
    # could use a global variable for attempts outside, but keeping this function exportable
    print 'Select your difficulty level. Available choices are easy, medium and hard.'
    attempts = allowed_attempts
    while attempts > MIN_COUNT:
        level_string = getResponseInLowerCase("Type in your choice: ")
        if level_string == 'easy':
            print 'You have chosen Easy!'
            return LIST_INDEX_LEVEL_EASY
        elif level_string == 'medium':
            print 'You have chosen Medium!'
            return LIST_INDEX_LEVEL_MEDIUM
        elif level_string == 'hard':
            print 'You have chosen Hard!'
            return LIST_INDEX_LEVEL_HARD
        else:
            attempts -= 1
            if attempts > MIN_COUNT:
                print 'Invalid choice! Please try again. You have ' + str(attempts) + ' chances left'
    print 'Sorry, you have exceeded the maximum number of allowed attempts.'
    return INVALID_MIN_RETURN_VALUE

def selectParagraph(level):
    ''' Input: Level selected, as number
        Returns: The corresponding paragraph '''
    if level == LIST_INDEX_LEVEL_EASY:
        return easy_para
    elif level == LIST_INDEX_LEVEL_MEDIUM:
        return medium_para
    elif level == LIST_INDEX_LEVEL_HARD:
        return hard_para
    else:
        return None

def getBlanks(para):
    ''' Input: The paragraph
        Returns: number of blanks in the paragraph '''
    number = 1
    count = MIN_COUNT
    while para.find(str(number)) > INVALID_MIN_RETURN_VALUE:
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
    while blanksToFill > MIN_COUNT:
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
            if attempts_left > MIN_COUNT:
                print 'Incorrect response. ' + str(attempts_left) + ' chances left.'
            else:
                print 'Oh, no! You have run out of chances!'
                return [False, para]
    return [True, para]

# --- MAIN FUNCTION ---
def runGame():
    ''' Calls helper functions and controls execution '''
    printBlock('Welcome to pyWise v1.0 - A Python refresher game by Siddhant Pardeshi')
    attempts = getAttempts()
    if attempts > INVALID_MIN_RETURN_VALUE:
        level = getLevel(attempts)
        if level > INVALID_MIN_RETURN_VALUE:
            answerState = checkAnswers(level, attempts)
            if (answerState[0] == True):
                printBlock(answerState[1])
                printBlock('You Win! Well done.')
                return NORMAL_PROGRAM_EXIT_CODE
            else:
                endGame()
        else:
            endGame()
    else:
        endGame()

runGame()
