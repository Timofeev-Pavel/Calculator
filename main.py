import math
import tkinter as tk

window = tk.Tk()
window.title('Calculator')
WINDOW_MAX_WIDTH = 200
WINDOW_MAX_HEIGHT = 300
WINDOW_MIN_HEIGHT = 0
WINDOW_MIN_WIDTH = 0
DEFAULT_IMAGE_BUTTON_WIDTH = 20
DEFAULT_IMAGE_BUTTON_HEIGTH = 20
window.geometry(str(WINDOW_MAX_WIDTH)+"x"+str(WINDOW_MAX_HEIGHT))
window.resizable(0, 0)
mtrx_of_symb = [['one_resized.png', 'two_resized.png', 'three_resized.png', 'plus_sign.png'],
               ['four_resized.png', 'five_resized.png','six_resized.png','minus_sign.png'],
               ['seven_resized.png', 'eight_resized.png','nine_resized.png','multiplication_sign.png'],
               ['nothing.png', 'zero_resized.png', 'nothing.png', 'devision_sign.png']]
# mtrx_of_symb = [['1', '2', '3', '+'],
#                ['4', '5','6','-'],
#                ['7', '8','9','*'],
#                [' ', '0', ' ', ':']]

# canva.create_rectangle(WINDOW_MIN_WIDTH+10,WINDOW_MIN_HEIGHT+100, WINDOW_MAX_WIDTH-10, WINDOW_MAX_HEIGHT-10, outline="black", width=5)
# canva.create_rectangle(10,10,190,90, outline='gold', width=5)
button_frame = tk.Frame(window, width=200, height=200, highlightbackground="gold", bg="cyan4", highlightthickness=3)
# button_frame.pack(side='bottom')
button_frame.place(x=0,y=100)
new_value = ""
string = tk.StringVar()
string.set(None)
def update_entry(symb):
    print(symb)
    global new_value
    new_value = string.get() + symb
    string.set(new_value)
entry = tk.Entry(window, textvariable=string, width=20, bg = "cyan4", justify='right')
entry.place(x=5, y=65)
# entry.pack()
def btn_clck(symb):
    print("Button works!", symb)
# entry.place(x=25, y=25)
# height=4
# entry.place(x=15, y=15)
def create_button(symb):
    image_file_path = "/Users/pavtim127/Desktop/MyCalculatorNotJava228/symbols/"
    x_pos = 15 
    y_pos = 60
    for i in range(len(mtrx_of_symb)):
        x_pos = 15
        y_pos+=i+48
        for j in range(len(mtrx_of_symb[i])):     
            # btn_img=tk.PhotoImage(file = image_file_path+mtrx_of_symb[i][j]) 
            # print(image_file_path+mtrx_of_symb[i][j]) 
            img = tk.PhotoImage(file = image_file_path+mtrx_of_symb[i][j])
            symb = mtrx_of_symb[i][j]
            # print(symb)
            btn = tk.Button(window, image = img, width=DEFAULT_IMAGE_BUTTON_WIDTH, 
            height=DEFAULT_IMAGE_BUTTON_HEIGTH,
            command=lambda: update_entry(symb))
            
            # btn.pack() 
            btn.place(x=x_pos, y=y_pos)
            x_pos += 46+j
            btn.bind('<Button-1>', btn_clck)
create_button(mtrx_of_symb)
window.mainloop()