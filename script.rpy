# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define T = Character("AP Statistics Teacher", image ="teacher")
define S = Character("AP Statistics Student", image="student")
image outsideClassroom="Clasroom.jpg"


label start:

    scene outsideClassroom
    pause
    "On a sunny Wednesday afternoon, in an AP Stats class..."

    T talk "Alright settle down class, as promised we’ll be going over your new assignment for this unit!"

    S three "Ooh sir, will this be weighed the same as the test?"
    return
