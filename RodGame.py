
from tkinter import *
import random
import Rod.Rod


class Window:

    #firstButton = Button()
    #secondButton = Button()
    #thirdButton = Button()
    #fourthButton = Button()
    def __init__(self):
        self.window = Tk()

        self.upImage = PhotoImage(file='images/up_arrow.png')
        self.rightImage = PhotoImage(file='images/right_arrow.png')
        self.leftImage = PhotoImage(file='images/left_arrow.png')
        self.downImage = PhotoImage(file='images/down_arrow.png')



        f1 = Frame(self.window)
        f1.pack()
        '''
        upButton = Button(f1, image=self.upImage).pack()
        rightButton = Button(f1, image=self.rightImage).pack()
        leftButton = Button(f1, image=self.leftImage).pack()
        downButton = Button(f1, image=self.downImage).pack()
        '''
        #self.make_rod()
        #command = lambda: change_pic(vlabel)
        #self.firstLabel = Label(f1, image=self.downImage).pack()

        self.firstButton = Button(f1, image=self.downImage, command=lambda: self.shootA(f1))

        self.firstButton.image = self.downImage
        self.firstButton['image'] = self.downImage
        self.firstButton.pack()

        self.secondButton = Button(f1, image=self.downImage, command=lambda: self.shootB(f1))
        self.secondButton.image = self.downImage
        self.secondButton['image'] = self.downImage
        self.secondButton.pack()

        self.thirdButton = Button(f1, image=self.downImage, command=lambda: self.shootC(f1))
        self.thirdButton.image = self.downImage
        self.thirdButton['image'] = self.downImage
        self.thirdButton.pack()

        self.fourthButton = Button(f1, image=self.downImage, command=lambda: self.shootD(f1))
        self.fourthButton.image = self.downImage
        self.fourthButton['image'] = self.downImage
        self.fourthButton.pack()

        self.submitButton = Button(f1, text='Submit', command=lambda: self.submit(f1))
        self.submitButton.pack()
        #firstButton = Button(f1, image=self.downImage, command=self.rotateFirst).pack()
        #secondButton = Button(f1, image=self.downImage).pack()
        #thirdButton = Button(f1, image=self.downImage).pack()
        #fourthButton = Button(f1, image=self.downImage).pack()
        self.setDirections(random.randint(0,3),random.randint(0,3),random.randint(0,3),random.randint(0,3))

        self.window.protocol("WM_DELETE_WINDOW", self.endprogram)
        self.window.mainloop()

    def endprogram(self):
        self.window.destroy()

    def make_rod(self):
        self.frameRod = Frame(self.window)
        self.frameRod.pack()
        self.firstButton = Button(self.frameRod, image=self.downImage, command=self.rotateFirst(self,self.firstButton.image)).pack()
        self.secondButton = Button(self.frameRod, image=self.downImage).pack()
        self.thirdButton = Button(self.frameRod, image=self.downImage).pack()
        self.fourthButton = Button(self.frameRod, image=self.downImage).pack()

    def setDirections(self, a, b, c, d):
        if a == 0:
            self.firstButton.image = self.downImage
            self.firstButton['image'] = self.downImage
        elif a == 1:
            self.firstButton.image = self.rightImage
            self.firstButton['image'] = self.rightImage
        elif a == 2:
            self.firstButton.image = self.upImage
            self.firstButton['image'] = self.upImage
        elif a == 3:
            self.firstButton.image = self.leftImage
            self.firstButton['image'] = self.leftImage

        if b == 0:
            self.secondButton.image = self.downImage
            self.secondButton['image'] = self.downImage
        elif b == 1:
            self.secondButton.image = self.rightImage
            self.secondButton['image'] = self.rightImage
        elif b == 2:
            self.secondButton.image = self.upImage
            self.secondButton['image'] = self.upImage
        elif b == 3:
            self.secondButton.image = self.leftImage
            self.secondButton['image'] = self.leftImage

        if c == 0:
            self.thirdButton.image = self.downImage
            self.thirdButton['image'] = self.downImage
        elif c == 1:
            self.thirdButton.image = self.rightImage
            self.thirdButton['image'] = self.rightImage
        elif c == 2:
            self.thirdButton.image = self.upImage
            self.thirdButton['image'] = self.upImage
        elif c == 3:
            self.thirdButton.image = self.leftImage
            self.thirdButton['image'] = self.leftImage

        if d == 0:
            self.fourthButton.image = self.downImage
            self.fourthButton['image'] = self.downImage
        elif d == 1:
            self.fourthButton.image = self.rightImage
            self.fourthButton['image'] = self.rightImage
        elif d == 2:
            self.fourthButton.image = self.upImage
            self.fourthButton['image'] = self.upImage
        elif d == 3:
            self.fourthButton.image = self.leftImage
            self.fourthButton['image'] = self.leftImage


    def getDirections(self):
        a,b,c,d = 0,0,0,0
        if self.firstButton.image == self.downImage:
            a = 0
        elif self.firstButton.image == self.rightImage:
            a = 1
        elif self.firstButton.image == self.upImage:
            a = 2
        elif self.firstButton.image == self.leftImage:
            a = 3

        if self.secondButton.image == self.downImage:
            b = 0
        elif self.secondButton.image == self.rightImage:
            b = 1
        elif self.secondButton.image == self.upImage:
            b = 2
        elif self.secondButton.image == self.leftImage:
            b = 3

        if self.thirdButton.image == self.downImage:
            c = 0
        elif self.thirdButton.image == self.rightImage:
            c = 1
        elif self.thirdButton.image == self.upImage:
            c = 2
        elif self.thirdButton.image == self.leftImage:
            c = 3

        if self.fourthButton.image == self.downImage:
            d = 0
        elif self.fourthButton.image == self.rightImage:
            d = 1
        elif self.fourthButton.image == self.upImage:
            d = 2
        elif self.fourthButton.image == self.leftImage:
            d = 3
        return [a,b,c,d]
    def shootA(self,parent):
        for x in range(2):
            self.rotateFirst(parent)
        self.rotateSecond(parent)

    def shootB(self,parent):
        self.rotateFirst(parent)
        for x in range(2):
            self.rotateSecond(parent)
        self.rotateThird(parent)
    def shootC(self,parent):
        self.rotateSecond(parent)
        for x in range(2):
            self.rotateThird(parent)
        self.rotateFourth(parent)

    def shootD(self,parent):

        self.rotateThird(parent)
        for x in range(2):
            self.rotateFourth(parent)

    def rotateFirst(self, parent):
        if self.firstButton.image == self.downImage:
            self.firstButton['image'] = self.rightImage
            self.firstButton.image = self.rightImage
        elif self.firstButton.image == self.rightImage:
            self.firstButton['image'] = self.upImage
            self.firstButton.image = self.upImage
        elif self.firstButton.image == self.upImage:
            self.firstButton['image'] = self.leftImage
            self.firstButton.image = self.leftImage
        elif self.firstButton.image == self.leftImage:
            self.firstButton['image'] = self.downImage
            self.firstButton.image = self.downImage

    def rotateSecond(self, parent):
        if self.secondButton.image == self.downImage:
            self.secondButton['image'] = self.rightImage
            self.secondButton.image = self.rightImage
        elif self.secondButton.image == self.rightImage:
            self.secondButton['image'] = self.upImage
            self.secondButton.image = self.upImage
        elif self.secondButton.image == self.upImage:
            self.secondButton['image'] = self.leftImage
            self.secondButton.image = self.leftImage
        elif self.secondButton.image == self.leftImage:
            self.secondButton['image'] = self.downImage
            self.secondButton.image = self.downImage

    def rotateThird(self, parent):
        if self.thirdButton.image == self.downImage:
            self.thirdButton['image'] = self.rightImage
            self.thirdButton.image = self.rightImage
        elif self.thirdButton.image == self.rightImage:
            self.thirdButton['image'] = self.upImage
            self.thirdButton.image = self.upImage
        elif self.thirdButton.image == self.upImage:
            self.thirdButton['image'] = self.leftImage
            self.thirdButton.image = self.leftImage
        elif self.thirdButton.image == self.leftImage:
            self.thirdButton['image'] = self.downImage
            self.thirdButton.image = self.downImage

    def rotateFourth(self, parent):
        if self.fourthButton.image == self.downImage:
            self.fourthButton['image'] = self.rightImage
            self.fourthButton.image = self.rightImage
        elif self.fourthButton.image == self.rightImage:
            self.fourthButton['image'] = self.upImage
            self.fourthButton.image = self.upImage
        elif self.fourthButton.image == self.upImage:
            self.fourthButton['image'] = self.leftImage
            self.fourthButton.image = self.leftImage
        elif self.fourthButton.image == self.leftImage:
            self.fourthButton['image'] = self.downImage
            self.fourthButton.image = self.downImage

    def submit(self, parent):
        print()
        a,b,c,d = self.getDirections()
        print("GOT DIRECTIONS",a,b,c,d)
        r = Rod.Rod.Rod(a, b, c, d)
        print(Rod.Rod.findSolution(r))


Window()