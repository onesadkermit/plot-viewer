import tkinter as tk
import matplotlib.pyplot as plt
import math as mth
#import widget_funcs as wf

def draw_matplot():
    dots =int(number_of_dots_text_box.get())
    #at least one point 
    if dots<1:
        dots = 1
    low = float(display_func_range_low_text_box.get())
    high = float(display_func_range_high_text_box.get())
    #increment interval
    interval = (high - low)/(dots+1)
    x_list = []
    y_list = []
    if current_function == "linear":
        a = float(a_const.get())
        b = float(b_const.get())
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(a*(low+n*interval)+b)
        plt.ylabel('linear function')

    elif current_function == "power":
        a = float(a_const.get())
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.pow(low+n*interval,a))
        plt.ylabel('power of x')

    elif current_function == "exponential":
        #add domain restriction
        a = float(a_const.get())
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.pow(a,low+n*interval))
        plt.ylabel('exponential function')
        
    elif current_function == "logarithm":
        #add domain restriction
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.log(low+n*interval))
        plt.ylabel('logarithm')
        
    elif current_function == "sin":
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.sin(low+n*interval))
        plt.ylabel('sin')
        
    elif current_function == "cos":
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.cos(low+n*interval))
        plt.ylabel('cos')
#
#
#TO DO add asymthotic lines
#
#
    elif current_function == "tg":
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.tan(low+n*interval))
        plt.ylabel('tan')
    
    elif current_function == "ctg":
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(1/mth.tan(low+n*interval))
        plt.ylabel('ctg')
        
    elif current_function == "asin":
        #add restriction domain
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.asin(low+n*interval))
        plt.ylabel('asin')
        
    elif current_function == "acos":
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.acos(low+n*interval))
        plt.ylabel('acos')
        
    elif current_function == "atg":
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.atan(low+n*interval))
        plt.ylabel('atg')
        
    elif current_function == "actg":
        for n in range(dots+1):
            x_list.append(low+n*interval)
            y_list.append(mth.pi/2 - mth.atan(low+n*interval))
        plt.ylabel('actg')
        
    
    plt.plot(x_list, y_list)
    plt.show()

def test_redraw():
    display_func_range_low_text_box.grid()
    display_func_range_high_text_box.grid()
    display_func_range_Label.grid()
    
#linear
def enable_func1_params():
    global current_function
    current_function = "linear"
    test_redraw()
    a_const.grid()
    b_const.grid()
    a_const_Label.grid()
    b_const_Label.grid()
    DrawPlotButton.grid()
    
#x to the power of a
def enable_func2_params():
    global current_function
    current_function = "power"
    test_redraw()
    a_const.grid()
    b_const.grid_remove()
    a_const_Label.grid()
    b_const_Label.grid_remove()
    DrawPlotButton.grid()

#a to the power of x
def enable_func3_params():
    global current_function
    current_function = "exponential"
    a_const.grid()
    b_const.grid_remove()
    a_const_Label.grid()
    b_const_Label.grid_remove()

#logarithm
def enable_func4_params():
    global current_function
    current_function = "logarithm"
    

#sin
def enable_func5_params():
    global current_function
    current_function = "sin"
    

#cos
def enable_func6_params():
    global current_function
    current_function = "cos"
    

#tg
def enable_func7_params():
    global current_function
    current_function = "tg"
    

#ctg
def enable_func8_params():
    global current_function
    current_function = "ctg"
    

#asin
def enable_func9_params():
    global current_function
    current_function = "asin"
    

#acos
def enable_func10_params():
    global current_function
    current_function = "acos"
    

#atg
def enable_func11_params():
    global current_function
    current_function = "atg"
    

#actg
def enable_func12_params():
    global current_function
    current_function = "actg"

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

FuncButton2 = tk.Button(func_button_frame, text="y=x^a",
                    height=1, width=10,
                 command=lambda: enable_func2_params())
FuncButton2.grid(row=2, column=0)

FuncButton3 = tk.Button(func_button_frame, text="y=a^x", 
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

ClearPlotButton = tk.Button(main_window, text="clear plot", 
                    height=1, width=10,
                 command=lambda: plt.clf())
ClearPlotButton.grid(row=1, column=0)

message_Label = tk.Label(main_window, text="to recalculate new func and add it to  plot, press func button again")
message_Label.grid(row=2, column=1)

#frame for function options
func_options_frame = tk.LabelFrame(main_window, text="options", relief=tk.RIDGE)
func_options_frame.grid(row=0, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

#text inputs function options
func_domain_Label = tk.Label(func_options_frame, text="Function domain")
func_domain_Label.grid(row=0, column=3)

func_domain_text_label = tk.Label(func_options_frame)
func_domain_text_label.grid(row=1, column=3)
insert_str = "+"+chr(8734)+":"+"-"+chr(8734)
func_domain_text_label.config(text = insert_str)

func_range_Label = tk.Label(func_options_frame, text="Function range")
func_range_Label.grid(row=0, column=5)

func_range_text_label = tk.Label(func_options_frame)
func_range_text_label.grid(row=1, column=5)
insert_str = "+"+chr(8734)+":"+"-"+chr(8734)
func_range_text_label.config(text = insert_str)

display_func_range_Label = tk.Label(func_options_frame, text="Display func. rng.")
display_func_range_Label.grid(row=2, column=5)

display_func_range_low_text_box = tk.Entry(func_options_frame)
display_func_range_low_text_box.grid(row=3, column=5)
insert_str = "-10"
display_func_range_low_text_box.insert(0,insert_str)

display_func_range_high_text_box = tk.Entry(func_options_frame)
display_func_range_high_text_box.grid(row=3, column=6)
insert_str = "+10"
display_func_range_high_text_box.insert(0,insert_str)

number_dots_Label = tk.Label(func_options_frame, text="Number of dots")
number_dots_Label.grid(row=2, column=3)

number_of_dots_text_box = tk.Entry(func_options_frame)
number_of_dots_text_box.grid(row=3, column=3)
insert_str = "100"
number_of_dots_text_box.insert(0,insert_str)

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

current_function = "linear"
main_window.geometry("450x450")
main_window.mainloop()