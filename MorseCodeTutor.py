
#
#   Morse Tutor
#   -----------
#
#   This simple Morse Tutor is intended to help the user recall
#   the Di / Dah patterns for Morse Code characters. It supports
#   the following:
#
#   Letters:        A - Z
#   Digits:         0 - 9
#   Punctutaion:    ?./,:=
#
#   When starting up the user will be prompted to ask which
#   characters sets they want to be tested on. This is done
#   by asking 3 questions to which the answer is either:
#
#   Yes:    Press button B
#   No:     Press button A
#
#   The questions take the form of single characters:
#
#   A:      Include letters?
#   9:      Include digits?
#   ?:      Include punctutaion?
#
#   These questions will be repeated until some characters
#   are chosen.
#
#   It will display random characters from the ones selected and
#   the user has a number of seconds to enter the correct Morse
#   code patterm for the one display. The pattern is entered using
#   the buttons:
#
#   Di:     Press button a
#   Dah:    Press button b
#   
#   When the time period expires it will show a sad face or a happy 
#   face to reflect whether the pattern is correct or not.
#
#   Every ten characters it will display your score as a string
#   similar to 9/10
#
#       Author: M.D.Waller G0PJO
#       December 12th, 2016                 V1.0
#
#       December 13th, 2016                 V1.1
#       a) Added an indication of score. It simple shows
#       how many you got right out of the total asked.
#       b) Added the ability to chose letters, digits or
#       punctuation or any combination of the three.
#
from microbit import *

import random

# Build the Morse Code dictionaries.

MorseCode = {}
MorseCodeLetters = {}
MorseCodeDigits = {}
MorseCodePunctuation = {}

# Put in the alpahbet

MorseCodeLetters['A'] = '._'
MorseCodeLetters['B'] = '_...'
MorseCodeLetters['C'] = '_._.'
MorseCodeLetters['D'] = '_..'
MorseCodeLetters['F'] = '.._.'
MorseCodeLetters['G'] = '__.'
MorseCodeLetters['H'] = '....'
MorseCodeLetters['I'] = '..'
MorseCodeLetters['J'] = '.___'
MorseCodeLetters['K'] = '_._'
MorseCodeLetters['L'] = '._..'
MorseCodeLetters['M'] = '__'
MorseCodeLetters['N'] = '_.'
MorseCodeLetters['O'] = '___'
MorseCodeLetters['P'] = '.__.'
MorseCodeLetters['Q'] = '__._'
MorseCodeLetters['R'] = '._.'
MorseCodeLetters['S'] = '...'
MorseCodeLetters['T'] = '_'
MorseCodeLetters['U'] = '.._'
MorseCodeLetters['V'] = '..._'
MorseCodeLetters['W'] = '.__'
MorseCodeLetters['X'] = '_.._'
MorseCodeLetters['Y'] = '_.__'
MorseCodeLetters['Z'] = '__..'

# Put in the digits

MorseCodeDigits['1'] = '.____'
MorseCodeDigits['2'] = '..___'
MorseCodeDigits['3'] = '...__'
MorseCodeDigits['4'] = '...._'
MorseCodeDigits['5'] = '.....'
MorseCodeDigits['6'] = '_....'
MorseCodeDigits['7'] = '__...'
MorseCodeDigits['8'] = '___..'
MorseCodeDigits['9'] = '____.'
MorseCodeDigits['0'] = '_____'

#
# Put in the punctuation
#

MorseCodePunctuation['?'] = '..__..';
MorseCodePunctuation['.'] = '._._._';
MorseCodePunctuation['/'] = '_.._.';
MorseCodePunctuation[','] = '__..__';
MorseCodePunctuation[':'] = '___...';
MorseCodePunctuation['='] = '_..._';

# Manifest Constants and variables

Dot = 1
Dash = 2
SecondTimeOut = 3
FaceDelaySeconds = 1
CurrentLine = 0

def AskAndBuildDictionary(questionCharacter,outDictionary,addDictionary):

    display.show(questionCharacter)
    while True:
        if button_a.was_pressed():
            break;
        if button_b.was_pressed():
            outDictionary.update(addDictionary)
            break;
            
    return(outDictionary)
    
#
# This function is called to add a Dot / Dash to the
# display.clear
#
def ShowDotDash(dotDash,line):
    if 0 == line:
        display.clear()
        
    line = line % 5
    if dotDash == Dot:
        display.set_pixel(2,line,9)
    else:
        display.set_pixel(1,line,9)
        display.set_pixel(2,line,9)
        display.set_pixel(3,line,9)
        
    return
 
#
# This is the main function to display a characters and read the
# user input.
#
def DoMorseCharacter():
    
    # Chose the character to be tested.
    
    randomCharacterKey = random.choice(list(MorseCode))
    
    # Display the character
    
    display.show(randomCharacterKey)
    
    # Initialise the guess
    
    guess = ''
    
    # Initialise the display line
    
    CurrentLine = 0
    
    # Get going and remember the time so we can stop
    
    now = running_time()
    endTime = now + SecondTimeOut * 1000
    while running_time() < endTime:
        
        # Process the button pressed, update the display and
        # update the guess.
        
        if button_a.was_pressed():
            ShowDotDash(Dot,CurrentLine)
            CurrentLine = CurrentLine + 1
            guess = guess + '.'
        if button_b.was_pressed():
            ShowDotDash(Dash,CurrentLine)
            CurrentLine = CurrentLine + 1
            guess = guess + '_'
    
    # We now have a guess, but is it correct?
    
    returnValue = 0
    if guess != MorseCode[randomCharacterKey]:
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)
        returnValue = 1
        
    # Give the user time to see the answer
    
    sleep(FaceDelaySeconds * 1000)
    return (returnValue)

#
# Put out the title and go...
#

display.scroll('MORSE CODE TUTOR V1.1 - G0PJO')

# What characters are we going to use?

while True:
    
    MorseCode = AskAndBuildDictionary('A',MorseCode,MorseCodeLetters)
    MorseCode = AskAndBuildDictionary('9',MorseCode,MorseCodeDigits)
    MorseCode = AskAndBuildDictionary('?',MorseCode,MorseCodePunctuation)
    
    if len(MorseCode) > 0:
        break

# Give the user some time

display.clear()
sleep(FaceDelaySeconds * 1000)

TotalQuestionsAsked = 0
QuestionAnsweredCorrectly = 0

while True:
    QuestionAnsweredCorrectly = QuestionAnsweredCorrectly + DoMorseCharacter()
    
    # Update the question count and display if necessary
    
    TotalQuestionsAsked = TotalQuestionsAsked + 1
    if TotalQuestionsAsked % 10 == 0:
        display.scroll(str(QuestionAnsweredCorrectly) + '/' + str(TotalQuestionsAsked))
    