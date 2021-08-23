from tkinter import *
import matplotlib.pyplot as plt
#import widget_funcs as wf

def change_label_number(num):
    counter = int(str(Button1.cget("text")))
    counter += num
    Button1.config(text=str(counter))

def draw_matplot():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()

main_window = Tk()

Label1 = Label(main_window, text="1")
Label1.grid(row=0, column=0)

Button1 = Button(main_window, text="2", 
                 command=lambda: change_label_number(2))
Button1.grid(row=1, column=0)

Button2 = Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button2.grid(row=2, column=0)

main_window.mainloop()

print("hello")