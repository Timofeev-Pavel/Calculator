import tkinter as tk

window = tk.Tk()
window.title('Calculator')
WINDOW_MAX_WIDTH = 200
WINDOW_MAX_HEIGHT = 300
DEFAULT_IMAGE_BUTTON_WIDTH = 20
DEFAULT_IMAGE_BUTTON_HEIGHT = 20
window.geometry(str(WINDOW_MAX_WIDTH) + "x" + str(WINDOW_MAX_HEIGHT))
window.resizable(0, 0)

mtrx_of_symb = [['one_resized.png', 'two_resized.png', 'three_resized.png', 'plus_sign.png'],
                ['four_resized.png', 'five_resized.png', 'six_resized.png', 'minus_sign.png'],
                ['seven_resized.png', 'eight_resized.png', 'nine_resized.png', 'multiplication_sign.png'],
                ['AC.png', 'zero_resized.png', 'equal_sign.png', 'devision_sign.png']]

button_frame = tk.Frame(window, width=200, height=300, highlightbackground="gold", bg="cyan4", highlightthickness=3)
button_frame.place(x=0, y=0)

string = tk.StringVar(window)

entry = tk.Entry(window, textvariable=string, width=20, bg="cyan4", justify='right')
entry.place(x=4, y=50)

def update_entry(symb):
    current_value = string.get()
    new_value = current_value + symb
    string.set(new_value)

def clear_entry():
    string.set("")

def counting():
    try:
        expression = string.get()
        result = str(eval(expression))
        string.set(result)
    except Exception as e:
        string.set("Error")

def btn_clck(c_symb):
    match(c_symb):
        case "zero.resized.png":
            c_symb="0"
            update_entry(c_symb)
        case "one_resized.png":
            c_symb = "1"
            update_entry(c_symb)
        case "two_resized.png":
            c_symb = "2"
            update_entry(c_symb)
        case "three_resized.png":
            c_symb = "3"
            update_entry(c_symb)
        case "four_resized.png":
            c_symb = "4"
            update_entry(c_symb)
        case "five_resized.png":
            c_symb = "5"
            update_entry(c_symb)
        case "six_resized.png":
            c_symb = "6"
            update_entry(c_symb)
        case "seven_resized.png":
            c_symb = "7"
            update_entry(c_symb)
        case "eight_resized.png":
            c_symb = "8"
            update_entry(c_symb)
        case "nine_resized.png":
            c_symb = "9"
            update_entry(c_symb)
        case "plus_sign.png":
            c_symb = "+"
            update_entry(c_symb)
        case "minus_sign.png":
            c_symb = "-"
            update_entry(c_symb)
        case "multiplication_sign.png":
            c_symb = "*"
            update_entry(c_symb)
        case "devision_sign.png":
            c_symb = "/"
            update_entry(c_symb)
        case "equal_sign.png":
            counting()

        case "AC.png":
            clear_entry()

    print("Button works!", c_symb)

def create_button(symb_matrix):
    image_file_path = "/Users/pavtim127/Desktop/MyCalculatorNotJava228/symbols/"
    x_pos = 15
    y_pos = 60

    for i in range(len(symb_matrix)):
        x_pos = 15
        y_pos += i + 48
        for j in range(len(symb_matrix[i])):
            img = tk.PhotoImage(file=image_file_path + symb_matrix[i][j])
            current_symb = symb_matrix[i][j]            
            sign = current_symb.split('.')[0].replace('_resized', '').replace('_', ' ')
            match(sign):
                case "one":
                    sign = "1"
                case "two":
                    sign = "2"
                case "three":
                    sign = "3"
                case "four":
                    sign = "4"
                case "five":
                    sign = "5"
                case "six":
                    sign = "6"
                case "seven":
                    sign = "7"
                case "eight":
                    sign = "8"
                case "nine":
                    sign = "9"
                case "zero":
                    sign = "0"
                case "plus sign":
                    sign = "+"
                case "minus sign":
                    sign = "-"
                case "multiplication sign":
                    sign = "*"
                case "devision sign":
                    sign = ":"
                case "equal sign":
                    sign = "="
            
            btn = tk.Button(window, image=img, width=DEFAULT_IMAGE_BUTTON_WIDTH,
                            height=DEFAULT_IMAGE_BUTTON_HEIGHT,
                            text=sign,
                            compound=tk.TOP,  
                            command=lambda c_symb=current_symb: btn_clck(c_symb),
                            relief=tk.GROOVE, 
                            bd=2,
                            font=('Arial', 15))

            btn.place(x=x_pos, y=y_pos)
            x_pos += 46 + j
            btn.bind('<Button-1>', lambda event, current_symb=current_symb: btn_clck(current_symb))

create_button(mtrx_of_symb)
window.mainloop()
