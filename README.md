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