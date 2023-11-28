import tkinter as tk
import re
from constants import *

window = tk.Tk()
window.title('Calculator')

window.geometry(str(WINDOW_MAX_WIDTH) + "x" + str(WINDOW_MAX_HEIGHT))
window.resizable(0, 0)
ALLOWED_IN_BUFFER_REGEX_PATTERN = re.compile(r'[\d\-\+\*/]')

mtrx_of_symb = [['one_resized.png', 'two_resized.png', 'three_resized.png', 'plus_sign.png'],
                ['four_resized.png', 'five_resized.png', 'six_resized.png', 'minus_sign.png'],
                ['seven_resized.png', 'eight_resized.png', 'nine_resized.png', 'multiplication_sign.png'],
                ['AC.png', 'zero_resized.png', 'equal_sign.png', 'devision_sign.png'],
                ["nothing.png", "nothing.png", "nothing.png", "nothing.png"]]

# def create_matrix(matrix_rows, matrix_columns, map):
    


button_frame = tk.Frame(window, width=200, height=300, highlightbackground="gold", bg="cyan4", highlightthickness=3)
button_frame.place(x=0, y=0)

main_window_display_string = tk.StringVar(window)

main_display_entry = tk.Entry(window, textvariable=main_window_display_string, width=20, bg="cyan4", justify='right')
main_display_entry.place(x=4, y=4)

def update_entry(button_sign_text):
    existing_number_buffer = main_window_display_string.get()
    new_buffer = ''
    
    if (button_sign_text == EQUAL_SIGN):
        new_buffer = evaluate_buffer()
    elif (button_sign_text == "AC"):
        clear_entry()
    elif re.search(ALLOWED_IN_BUFFER_REGEX_PATTERN, button_sign_text):
        new_buffer = existing_number_buffer + button_sign_text
    else:
        pass
    
    main_window_display_string.set(new_buffer)

def clear_entry():
    main_window_display_string.set("")

def evaluate_buffer():
    try:
        expression_to_evaluate = main_window_display_string.get()
        result = str(eval(expression_to_evaluate))
        return result
    except Exception as e:
        main_window_display_string.set("Error")

def create_button(symb_matrix):
    # FIXME: use os library to get current directory
    image_file_path = "/Users/pavtim127/Desktop/MyCalculatorNotJava228/symbols/"
    # FIXME: all coordinate positions should be defined as constant variables
    # e.g x_pos -> X_AXIS_OFFSET
    y_pos = 0

    for i in range(len(symb_matrix)):
        x_pos = 15
        y_pos += i + 48
        for j in range(len(symb_matrix[i])):
            button_image = tk.PhotoImage(file=image_file_path + symb_matrix[i][j])
            current_symb = symb_matrix[i][j]

            # FIXME: this string cutting is too complicated, simlify
            sign = current_symb.split('.')[0].replace('_resized', '').replace('_', ' ')

            button_sign_text = getButtonSignText(sign)
            
            btn = tk.Button(window, image=button_image, width=DEFAULT_IMAGE_BUTTON_WIDTH,
                            height=DEFAULT_IMAGE_BUTTON_HEIGHT,
                            text=button_sign_text,
                            compound=tk.TOP,  
                            command=lambda event, button_sign_text=button_sign_text: update_entry(button_sign_text),
                            relief=tk.GROOVE, 
                            font=('Arial', 17))

            btn.place(x=x_pos, y=y_pos)
            x_pos += 46 + j
            btn.bind('<Button-1>', lambda event, button_sign_text=button_sign_text: update_entry(button_sign_text))

def getButtonSignText(signToMatch):
    match(signToMatch):
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case "zero":
            return "0"
        case "plus sign":
            return "+"
        case "minus sign":
            return "-"
        case "multiplication sign":
            return "*"
        case "devision sign":
            return "/"
        case "equal sign":
            return "="
        case "nothing":
            return ""
        case "AC":
            return "AC"


create_button(mtrx_of_symb)
window.mainloop()