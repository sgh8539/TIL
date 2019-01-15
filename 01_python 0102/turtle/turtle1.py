import turtle as t

class MagicBrush:
    t.color('yellow')
    def draw_square(self):
        for i in range (4):
            t.forward(100)
            t.right (90)
    def draw_triangle(self):
        for i in range (3):
            t.forward (100)
            t.left (120)
    def go(self):
        t. forward(200)
    def turn(a):
        t.right(90)

print(type(MagicBrush))
print(type(t))

# m = MagicBrush()
# m2 = MagicBrush()


# m.draw_square()
# m.draw_triangle()
# m2.go()
# m2.draw_square()
# m2.draw_triangle()

# t.mainloop()

# # turtle.Screen() 
