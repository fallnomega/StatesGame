import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
new_shape = "blank_states_img.gif"
screen.register_shape(new_shape)
turtle.shape(new_shape)


data = pandas.read_csv("50_states.csv")
# print(data)
# user_input = input("Toss me a state: ")
user_input = "Texas".lower()
data_dict = data.to_dict()

for x in range(0, len(data_dict["state"])):
    lowered = data_dict["state"][x]
    lowered = lowered.lower()
    if lowered == user_input:
        print(f"{data_dict['state'][x]} WINNNER")
        print(data_dict['x'][x])
        print(data_dict['y'][x])
    else:
        continue



screen.exitonclick()



