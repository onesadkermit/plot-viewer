def change_label_number(num):
    counter = int(str(Button1.cget("text")))
    counter += num
    Button1.config(text=str(counter))