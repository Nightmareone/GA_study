from tkinter import *
class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text = "Calculate")
        self.helloLabel.pack()
        self.quitButton = Button(self, test = "Quit", command = self.quit)
        self.quitButton.pack()

class Calculate(object):

    def __init__(self, a, b):
        self.numOne = a
        self.numTwo = b

    def getADD(self):
        print(self.numOne + self.numTwo)

    def getMinus(self):
        print(self.numOne - self.numTwo)

    def getMul(self):
        print(self.numOne * self.numTwo)

    def getDiV(self):
        print(self.numOne / self.numTwo)

app = Application()
app.master.title("Calculate")
app.mainloop()
# quitOption = 'n'
# while (quitOption == 'n'):
#     get_input_a = int(input("please input the first number:"))
#     get_input_b = int(input("please input the second number:"))
#     get_operation = int(input("Please input the demmand(0~3):"))
#     print('The number you input is:%s, %s' % (get_input_a, get_input_b))
#     cal = Calculate(get_input_a,get_input_b)
#
#     if get_operation == 0:
#         cal.getADD()
#     elif get_operation == 1:
#         cal.getMinus()
#     elif get_operation == 2:
#         cal.getMul()
#     elif get_operation == 3:
#         cal.getDiV()
#     else :
#         print("you are wrong!!")
#
#     quitOption = input("Are you sure to quit the Calculate(y/n):")
#     if quitOption == 'y':
#         print('bye')
#         break
