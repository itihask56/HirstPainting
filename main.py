
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('/Users/mr_verma/PycharmProjects/HirstPainting/ hirst.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82), (115, 134, 139)]

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed('fastest')
tim.setheading(225)

tim.forward(300)
tim.setheading(0)

no_of_dots =100

for dot_count in range(1, no_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    if dot_count%10==0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()


