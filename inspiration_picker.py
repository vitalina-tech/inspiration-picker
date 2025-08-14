import tkinter as tk
import random
import json

def load_quotes():
    try:
        with open('quotes.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data['quotes']
    except FileNotFoundError:
        return ["Quote file not found. Please check quotes.json exists."]
    except json.JSONDecodeError:
        return ["Error reading quotes file. Please check JSON format."]
    
quotes = load_quotes()

def get_inspirations():
    selected=random.choice(quotes)
    inspirations_label.config(text=selected)

window=tk.Tk()
window.title("Inspiration Picker")
window.geometry("500x400")
window.config(bg='#768258')
title_label = tk.Label(window,
                 text="Your inspiration for today:",
                 font=('Courier', 16, 'normal'),
                 bg='#768258',
                 fg='black')
title_label.pack(padx = 30, pady = 30)

inspiration_button = tk.Button(window,
                           text = 'Get inspiration',
                           font = ('Courier', 14, 'normal'),
                           bg = "#C5B93F",
                           fg = 'black',
                           padx = 10,
                           pady = 10,
                           command = get_inspirations,
                           cursor = 'hand2',
                           activebackground = "#C78015"
)
inspiration_button.pack(pady = 30)

inspirations_label = tk.Label(window,
                         text='',
                         font=('Courier', 14, 'normal'),
                         bg = '#768258',
                         fg = 'black',
                         wraplength=350)
inspirations_label.pack(pady=30, padx=30, fill='x')


tk.mainloop()
