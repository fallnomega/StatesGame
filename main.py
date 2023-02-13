import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
new_shape = "blank_states_img.gif"
screen.register_shape(new_shape)
turtle.shape(new_shape)
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
# state_picked = turtle.Turtle()
# screen.textinput( "Guess a State","Guess the name of a state in the United States:   ")
# state_picked.shape("circle")
# state_picked.shapesize(.1,.1,.1)
# state_picked.penup()

game_on = True
while game_on:
    user_input = screen.textinput("Guess a State", "Guess the name of a state in the United States:   ").lower()
    if user_input==None:
        exit()
    for x in range(0, len(data_dict["state"])):
        lowered = data_dict["state"][x]
        lowered = lowered.lower()
        if lowered == user_input:
            print(f"{data_dict['state'][x]} WINNNER")
            print(data_dict['x'][x])
            print(data_dict['y'][x])
            apply_state = turtle.Turtle()
            apply_state.shape("circle")
            apply_state.shapesize(.1,.1,.1)
            apply_state.penup()
            apply_state.goto(data_dict['x'][x],data_dict['y'][x])
            apply_state.write(data_dict['state'][x])

        else:
            continue

# def get_mouse_click_coor(x,y):
#     print(x,y)
# screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()

# screen.exitonclick()



