import tkinter as tk
import matplotlib.pyplot as plt
#import widget_funcs as wf

def change_label_number(num : int):
    counter = int(str(Button1.cget("text")))
    counter += num
    Button1.config(text=str(counter))

def draw_matplot():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()

main_window = tk.Tk()
#Labels
Label1 = tk.Label(main_window, text="Functions")
Label1.grid(row=0, column=0)

#text inputs
text_box = tk.Entry(main_window)
text_box.grid(row=0, column=1)
text_box.insert(0,"asdasdasdasd")
#Buttons

Button1 = tk.Button(main_window, text="2", 
                 command=lambda: change_label_number(2))
Button1.grid(row=1, column=0)

Button2 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button2.grid(row=2, column=0)

Button3 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button3.grid(row=3, column=0)

Button4 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button4.grid(row=4, column=0)

Button5 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button5.grid(row=5, column=0)

Button6 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button6.grid(row=6, column=0)

Button7 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button7.grid(row=7, column=0)

Button8 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button8.grid(row=8, column=0)

Button9 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button9.grid(row=9, column=0)

Button10 = tk.Button(main_window, text="draw_matplot", 
                 command=lambda: draw_matplot())
Button10.grid(row=10, column=0)

main_window.geometry("250x400")
main_window.mainloop()