import math
import tkinter as tk
window = tk.Tk()
window.title('Calculator')
WINDOW_MAX_WIDTH = 450
WINDOW_MAX_HEIGHT = 450
DEFAULT_IMAGE_BUTTON_WIDTH = 10
DEFAULT_IMAGE_BUTTON_HEIGTH = 10
window.geometry(str(WINDOW_MAX_WIDTH)+"x"+str(WINDOW_MAX_HEIGHT))
mtrx_of_symb = [['1', '2', '3', '+'],
               ['4', '5','6','-'],
               ['7', '8','9','*'],
               [' ', '0', ' ', ':']]

canva = tk.Canvas(window, height=WINDOW_MAX_WIDTH, width=WINDOW_MAX_HEIGHT, bg='light blue')
canva.pack()
canva.create_rectangle(10,100, 290, 390, outline="black")
img= tk.PhotoImage(file='/Users/pavtim127/Desktop/MyCalculatorNotJava228/one_resized.png')
def create_button(symbol):
    x_pos = 10
    y_pos = 100
    for i in range(len(mtrx_of_symb)):
        x_pos = 10
        y_pos+=30*i
        for j in range(len(mtrx_of_symb[i])):                  
            btn = tk.Button(window, text=mtrx_of_symb[i][j], width=DEFAULT_IMAGE_BUTTON_WIDTH, height=DEFAULT_IMAGE_BUTTON_HEIGTH)
            btn.pack() 
            x_pos += 50*j
            btn.place(x=x_pos, y=y_pos)
btn = tk.Button(window, image=img, width=DEFAULT_IMAGE_BUTTON_WIDTH, height=DEFAULT_IMAGE_BUTTON_HEIGTH)
btn.pack()
btn.place(x=150,y=150)
window.mainloop()