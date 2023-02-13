import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
new_shape = "blank_states_img.gif"
screen.register_shape(new_shape)
turtle.shape(new_shape)
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
all_states = data['state'].tolist()
player_score = 0
correct_guesses = []
game_on = True

while game_on:
    user_input = screen.textinput(f"Correctly Guessed States {player_score}/50",
                                  "Guess the name of a state in the United States:   ")

    if user_input == 'exit':
        states_to_learn = []
        for x in all_states:
            if x not in correct_guesses:
                states_to_learn.append(x)
        print(states_to_learn)
        pd_temp = pandas.DataFrame(states_to_learn)
        pd_temp.to_csv("states_to_learn.csv")
        break
    for x in range(0, len(data_dict["state"])):
        lowered = data_dict["state"][x]
        lowered = lowered.lower()
        if lowered == user_input.lower():
            apply_state = turtle.Turtle()
            apply_state.hideturtle()
            apply_state.shape("circle")
            apply_state.shapesize(.1, .1, .1)
            apply_state.penup()
            apply_state.goto(data_dict['x'][x], data_dict['y'][x])
            apply_state.write(data_dict['state'][x])
            player_score += 1
            correct_guesses.append(data_dict['state'][x])

        else:
            continue

screen.mainloop()
