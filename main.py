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
mtrx_of_symb = [['one_resized.png', 'two_resized.png', 'three_resized.png', 'plus_sign.png'],
               ['four_resized.png', 'five_resized.png','six_resized.png','minus_sign.png'],
               ['seven_resized.png', 'eight_resized.png','nine_resized.png','multiplication_sign.png'],
               ['nothing.png', 'zero_resized.png', 'nothing.png', 'devision_sign.png']]

canva = tk.Canvas(window, height=WINDOW_MAX_HEIGHT, width=WINDOW_MAX_WIDTH, bg='cyan4')
canva.pack()
canva.create_rectangle(WINDOW_MIN_WIDTH+10,WINDOW_MIN_HEIGHT+100, WINDOW_MAX_WIDTH-10, WINDOW_MAX_HEIGHT-10, outline="black", width=5)
canva.create_rectangle(10,10,190,90, outline='orange', width=5)

symb = None
def btn_clck(event):
    # print("Button was clicked")
    label = tk.Label(window, text=f"Button {symb} was clciked!", width=18, height=4, bg="cyan4", fg="azure")
    label.pack()
    label.place(x=15, y=15)  
    
def create_button(symbol):
    image_file_path = "/Users/pavtim127/Desktop/MyCalculatorNotJava228/symbols/"
    x_pos = 15 
    y_pos = 60
    for i in range(len(mtrx_of_symb)):
        x_pos = 15
        y_pos+=i+48
        for j in range(len(mtrx_of_symb[i])):     
            btn_img=tk.PhotoImage(file = image_file_path+mtrx_of_symb[i][j]) 
            symb =  mtrx_of_symb[i][j]           
            btn = tk.Button(window, image=btn_img, width=DEFAULT_IMAGE_BUTTON_WIDTH, height=DEFAULT_IMAGE_BUTTON_HEIGTH, activebackground="green")
            btn.pack() 
            btn.place(x=x_pos, y=y_pos)
            x_pos += 46+j
            btn.bind('<Button-1>', btn_clck)
create_button(mtrx_of_symb)
window.mainloop()