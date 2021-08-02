import turtle
import pandas

screen = turtle.Screen()
screen.title("States Game")
image = "./Day-25/states_game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
todd = turtle.Turtle()
todd.penup()
todd.hideturtle()

is_game_on = True
correct_guesses = 0

data = pandas.read_csv("./Day-25/states_game/50_states.csv")
all_states = data["state"].to_list()

while is_game_on:
    answer_state = screen.textinput(title=f"Score : {correct_guesses}/50", prompt="Enter a State Name: ")
    
    state = data[data.state == answer_state.title()]

    if answer_state == "exit":
        break

    if not state.empty:
        state_pos = (state.values[0][1], state.values[0][2])
        correct_guesses += 1
        todd.goto(state_pos)
        todd.write(state.values[0][0], font=("Arial", 10, "normal"))
        all_states.remove(state.values[0][0])

    if correct_guesses == 50:
        is_game_on = False
        print("Congratulations! You won!")
        print(f"Your score is {correct_guesses}/50")
        print("Game Over!")
        print("Thanks for playing!")

if len(all_states) > 0:
    print("States to learn")
    print(all_states)
    pandas.DataFrame(all_states).to_csv("./Day-25/states_game/states_to_learn.csv")

turtle.mainloop()
