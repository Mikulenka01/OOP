from gui import View, Button, TextLabel#, Color


def foo():
    print("foo")

def foo2():
    print("foo2")


b1 = Button("b1", (1,1), "test1", foo)
b2 = Button("b2", (2,2), "test2", foo2)

#1.show()
#b1.on_click()
#b1.name()

#print(type(foo))
#b2.show()
#b2.on_click()

l1 = TextLabel("tl1", (1,2), "ja jsem label1")
l2 = TextLabel("tl2", (1,3), "ja jsem label3")


window: [View] = [b1, b2, l1, l2]

for element in window:
    element.show()

"""
favorite_color = Color.RED
print(type(favorite_color))

if favorite_color == Color.RED:
    print("Máte radi červenú!")"""