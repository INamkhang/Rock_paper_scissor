from tkinter import * 
from tkinter.ttk import *
import random
## def function ##

## cal ##
def cal(user):
    choicem = [1,0,-1]
    com = random.choice(choicem)
    calcu = user - com
    if com == 1:
        comout = 'Rock'
    elif com == 0:
        comout = 'scissor'
    elif com == -1:
        comout = 'paper'   

    if calcu == 1 or calcu == -2 :
        pop = Toplevel(root)
        pop.title("Result")
        Button(pop, text = f'WIN computer choses : {comout}' ,command= lambda : pop.destroy()).pack(side = TOP, pady = 10)

    elif calcu == 0 :
        pop = Toplevel(root)
        pop.title("Result")
        Button(pop, text = f'DRAW computer choses : {comout}' ,command= lambda : pop.destroy()).pack(side = TOP, pady = 10)

    elif calcu == -1 or calcu == 2 :
        pop = Toplevel(root)
        pop.title("Result")
        Button(pop, text = f'LOSE computer choses : {comout}' ,command= lambda : pop.destroy()).pack(side = TOP, pady = 10)
 



# creating tkinter window
root = Tk()
root.title("RPS")

## center screen ##
root.eval('tk::PlaceWindow . center')
# Adding widgets to the root window
Label(root, text = 'TEST', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
  
# Creating a photoimage object to use image
paper = PhotoImage(file =r"D:\test\rock_paper_scissor\image\paper.png")
rock =  PhotoImage(file =r"D:\test\rock_paper_scissor\image\rock.png")
scissor = PhotoImage(file =r"D:\test\rock_paper_scissor\image\scissor.png")
  
# here, image option is used to
# set image on button

Button(root, image = rock,command= lambda : cal(1)).pack(side = LEFT)
Button(root, image = scissor,command= lambda : cal(0)).pack(side = LEFT)
Button(root, image = paper,command= lambda : cal(-1)).pack(side = RIGHT) 



mainloop()