
from turtle import Turtle, Screen
import pandas

image = "blank_states_img.gif"
screen = Screen()
screen.addshape(image)
screen.title("The United States Game.")
t = Turtle(image)

state_name = Turtle()
state_name.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
print(data.state)
score = 0

def goto_location(x, y, text):
    state_name.penup()
    state_name.goto(x,y)
    state_name.write(f"{text}", align="center", font=("Courier", 10, "bold"))

guess_is_on = True

correct_state_list = []
while guess_is_on:
    user_ans = screen.textinput(title=f"Score: {score}/50", prompt="Guess a state in the U.S.").title()
    states = data[data.state == user_ans]


    if user_ans  in states_list  and user_ans not in correct_state_list:
        i = states_list.index(user_ans)
        x_cor = states.x[i]
        y_cor = states.y[i]
        s = states.state[i]
        score += 1
        correct_state_list.append(user_ans)
        goto_location(x_cor, y_cor, user_ans)
        print(correct_state_list)


    if user_ans not in states_list or  user_ans == "exit":
        missing_states = [state for state in states_list if state not in correct_state_list]
        print(correct_state_list)
        goto_location(0, 0, "GAME 0VER!")
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states_from_game.csv")
        guess_is_on = False
        print("Game over")







screen.mainloop()