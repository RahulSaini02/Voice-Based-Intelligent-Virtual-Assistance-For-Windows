import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#Globals 
FRIDAY_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
friday_choice = ""


def choice_to_number(choice):
    """Convert choice to number."""

    return {'rock': 0, 'paper': 1, 'scissors': 2}[choice]


def number_to_choice(number):
    """Convert number to choice."""

    return {0: 'rock', 1: 'paper', 2: 'scissors'}[number]


def random_friday_choice():
    """Choose randomly for computer."""

    return random.choice(['rock', 'paper', 'scissors'])


def choice_result(human_choice, friday_choice):
    """Return the result of who wins."""

    global FRIDAY_SCORE
    global HUMAN_SCORE

    friday_choice_number = choice_to_number(friday_choice)
    human_choice_number = choice_to_number(human_choice)

    if human_choice == friday_choice:
        print("Tie")

    elif (human_choice_number - friday_choice_number) % 3 == 1:
        print("Computer wins!")
        FRIDAY_SCORE += 1

    else:
        print("Human wins!")
        HUMAN_SCORE += 1


def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2


def test_number_to_choice():
    assert number_to_choice(0) == 'rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'


def test_all():
    test_choice_to_number()
    test_number_to_choice()

# Handler for mouse click on rock button.
def rock():
    global human_choice, friday_choice
    global HUMAN_SCORE, FRIDAY_SCORE

    human_choice = 'rock'
    friday_choice = random_friday_choice()
    choice_result(friday_choice, human_choice)


# Handler for mouse click on paper button.
def paper():
    global human_choice, friday_choice
    global HUMAN_SCORE, FRIDAY_SCORE

    human_choice = 'paper'
    friday_choice = random_friday_choice()
    choice_result(friday_choice, human_choice)

# Handler for mouse click on scissors button.
def scissors():
    global human_choice, friday_choice
    global HUMAN_SCORE, FRIDAY_SCORE

    human_choice = 'scissors'
    friday_choice = random_friday_choice()
    choice_result(friday_choice, human_choice)

# Handler to draw on canvas
def draw(canvas):
    try:
        # Draw choices
        canvas.draw_text("You: " + human_choice, [10, 40], 48, "Green")
        canvas.draw_text("Friday: " + friday_choice, [10, 80], 48, "Red")

        # Draw scores
        canvas.draw_text("Your Score: " + str(HUMAN_SCORE),
                         [10, 150], 30, "Green")
        canvas.draw_text("Friday Score: " + str(FRIDAY_SCORE),
                         [10, 190], 30, "Red")

    except TypeError:
        pass


# Create a frame and assign callbacks to event handlers
def RockPaperScissors():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()


