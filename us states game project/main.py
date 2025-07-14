import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to.list()

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
print(answer_state)





turtle.mainloop( )
screen.exitonclick()