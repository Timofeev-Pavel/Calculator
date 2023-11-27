
import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
window.title("Test")
btn_img=tk.PhotoImage(file = "/Users/pavtim127/Desktop/MyCalculatorNotJava228/symbols/one_resized.png") 
btn = tk.Button(window, image=btn_img, width=100, height=100)
btn.pack()
window.mainloop()