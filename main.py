import tkinter as tk
import matplotlib.pyplot as plt
import math as mth
#import widget_funcs as wf

def draw_matplot():
    plt.ylabel('some numbers')
    plt.show()

def test_redraw():
    func_range_text_box.grid()
    func_domain_text_box.grid()
    func_domain_Label.grid()
    func_range_Label.grid()
    number_dots_Label.grid()
    number_of_dots_text_box.grid()
    display_func_range_low_text_box.grid()
    display_func_range_high_text_box.grid()
    display_func_range_Label.grid()

#linear
def enable_func1_params():
    test_redraw()
    a_const.grid()
    b_const.grid()
    a_const_Label.grid()
    b_const_Label.grid()
    DrawPlotButton.grid()
    dots =int(number_of_dots_text_box.get())
    if dots<1:
        dots = 1
    low = int(display_func_range_low_text_box.get())
    high = int(display_func_range_high_text_box.get())
    print(high, low)
    quant = (high - low)/(dots+1)
    x_list = []
    y_list = []
    x_list.append(low)
    y_list.append(low*int(a_const.get())+int(b_const.get()))
    for n in range(dots+1):
        x_list.append(low+n*quant)
        y_list.append((low+n*quant)*int(a_const.get())+int(b_const.get()))
        print(x_list[len(x_list)-1], y_list[len(y_list)-1])
    plt.plot(x_list, y_list)
#x to the power of a
def enable_func2_params():
    test_redraw()
    a_const.grid()
    b_const.grid_remove()
    a_const_Label.grid()
    b_const_Label.grid_remove()
    DrawPlotButton.grid()
    dots =int(number_of_dots_text_box.get())
    if dots<1:
        dots = 1
    low = int(display_func_range_low_text_box.get())
    high = int(display_func_range_high_text_box.get())
    print(high, low)
    quant = (high - low)/(dots+1)
    a = float(a_const.get())
    x_list = []
    y_list = []
    x_list.append(low)
    y_list.append(mth.pow(low,a))
    for n in range(dots+1):
        x_list.append(low+n*quant)
        y_list.append(mth.pow(low+n*quant,a))
        print(x_list[len(x_list)-1], y_list[len(y_list)-1])
    plt.plot(x_list, y_list)

#a to the power of x
def enable_func3_params():
    draw_matplot()

#logarithm
def enable_func4_params():
    draw_matplot()

#sin
def enable_func5_params():
    draw_matplot()

#cos
def enable_func6_params():
    draw_matplot()

#tg
def enable_func7_params():
    draw_matplot()

#ctg
def enable_func8_params():
    draw_matplot()

#asin
def enable_func9_params():
    draw_matplot()

#acos
def enable_func10_params():
    draw_matplot()

#atg
def enable_func11_params():
    draw_matplot()

#actg
def enable_func12_params():
    draw_matplot()

main_window = tk.Tk()

#Frame for func buttons
func_button_frame = tk.LabelFrame(main_window, text="Commands", relief=tk.RIDGE)
func_button_frame.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S)

Label1 = tk.Label(func_button_frame, text="Functions")
Label1.grid(row=0, column=0)
#func Buttons

FuncButton1 = tk.Button(func_button_frame, text="y=ax+b",
                    height=1, width=10,
                 command=lambda: enable_func1_params())
FuncButton1.grid(row=1, column=0)

FuncButton2 = tk.Button(func_button_frame, text="y=a^x",
                    height=1, width=10,
                 command=lambda: enable_func2_params())
FuncButton2.grid(row=2, column=0)

FuncButton3 = tk.Button(func_button_frame, text="y=x^a", 
                    height=1, width=10,
                 command=lambda: enable_func3_params())
FuncButton3.grid(row=3, column=0)

FuncButton4 = tk.Button(func_button_frame, text="y=log(x)", 
                    height=1, width=10,
                 command=lambda: enable_func4_params())
FuncButton4.grid(row=4, column=0)

FuncButton5 = tk.Button(func_button_frame, text="y=sin(x)", 
                    height=1, width=10,
                 command=lambda: enable_func5_params())
FuncButton5.grid(row=5, column=0)

FuncButton6 = tk.Button(func_button_frame, text="y=cos(x)", 
                    height=1, width=10,
                 command=lambda: enable_func6_params())
FuncButton6.grid(row=6, column=0)

FuncButton7 = tk.Button(func_button_frame, text="y=tg(x)", 
                    height=1, width=10,
                 command=lambda: enable_func7_params())
FuncButton7.grid(row=7, column=0)

FuncButton8 = tk.Button(func_button_frame, text="y=ctg(x)", 
                    height=1, width=10,
                 command=lambda: enable_func8_params())
FuncButton8.grid(row=8, column=0)

FuncButton9 = tk.Button(func_button_frame, text="y=asin(x)", 
                    height=1, width=10,
                 command=lambda: enable_func9_params())
FuncButton9.grid(row=9, column=0)

FuncButton10 = tk.Button(func_button_frame, text="y=acos(x)", 
                    height=1, width=10,
                 command=lambda: enable_func10_params())
FuncButton10.grid(row=10, column=0)

FuncButton11 = tk.Button(func_button_frame, text="y=atg(x)", 
                    height=1, width=10,
                 command=lambda: enable_func11_params())
FuncButton11.grid(row=11, column=0)

FuncButton12 = tk.Button(func_button_frame, text="y=actg(x)", 
                    height=1, width=10,
                 command=lambda: enable_func12_params())
FuncButton12.grid(row=12, column=0)

DrawPlotButton = tk.Button(main_window, text="draw plot", 
                    height=1, width=10,
                 command=lambda: draw_matplot())
DrawPlotButton.grid(row=1, column=1)
DrawPlotButton.grid_remove()

message_Label = tk.Label(main_window, text="to recalculate new func and add it to  plot, press func button again")
message_Label.grid(row=2, column=1)

#frame for function options
func_options_frame = tk.LabelFrame(main_window, text="options", relief=tk.RIDGE)
func_options_frame.grid(row=0, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

#text inputs function options
func_domain_Label = tk.Label(func_options_frame, text="Function domain")
func_domain_Label.grid(row=0, column=3)
func_domain_Label.grid_remove()

func_domain_text_box = tk.Entry(func_options_frame)
func_domain_text_box.grid(row=1, column=3)
insert_str = "+"+chr(8734)+":"+"-"+chr(8734)
func_domain_text_box.insert(0,insert_str)
func_domain_text_box.grid_remove()

func_range_Label = tk.Label(func_options_frame, text="Function range")
func_range_Label.grid(row=0, column=5)
func_range_Label.grid_remove()

func_range_text_box = tk.Entry(func_options_frame)
func_range_text_box.grid(row=1, column=5)
insert_str = "+"+chr(8734)+":"+"-"+chr(8734)
func_range_text_box.insert(0,insert_str)
func_range_text_box.grid_remove()

display_func_range_Label = tk.Label(func_options_frame, text="Display func. rng.")
display_func_range_Label.grid(row=2, column=5)
display_func_range_Label.grid_remove()

display_func_range_low_text_box = tk.Entry(func_options_frame)
display_func_range_low_text_box.grid(row=3, column=5)
insert_str = "-10"
display_func_range_low_text_box.insert(0,insert_str)
display_func_range_low_text_box.grid_remove()

display_func_range_high_text_box = tk.Entry(func_options_frame)
display_func_range_high_text_box.grid(row=3, column=6)
insert_str = "+10"
display_func_range_high_text_box.insert(0,insert_str)
display_func_range_high_text_box.grid_remove()

number_dots_Label = tk.Label(func_options_frame, text="Number of dots")
number_dots_Label.grid(row=2, column=3)
number_dots_Label.grid_remove()

number_of_dots_text_box = tk.Entry(func_options_frame)
number_of_dots_text_box.grid(row=3, column=3)
insert_str = "100"
number_of_dots_text_box.insert(0,insert_str)
number_of_dots_text_box.grid_remove()



a_const_Label = tk.Label(func_options_frame, text="Const a")
a_const_Label.grid(row=4, column=3)
a_const_Label.grid_remove()

a_const = tk.Entry(func_options_frame)
a_const.grid(row=5, column=3)
insert_str = "1"
a_const.insert(0,insert_str)
a_const.grid_remove()

b_const_Label = tk.Label(func_options_frame, text="Const b")
b_const_Label.grid(row=4, column=5)
b_const_Label.grid_remove()

b_const = tk.Entry(func_options_frame)
b_const.grid(row=5, column=5)
insert_str = "1"
b_const.insert(0,insert_str)
b_const.grid_remove()

main_window.geometry("450x450")
main_window.mainloop()