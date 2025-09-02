import tkinter as tk
import random
import json



def load_quotes():
    try:
        with open('quotes.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [quote['text'] for quote in data['quotes']]
    except FileNotFoundError:
        return ["Quote file not found. Please check quotes.json exists."]
    except json.JSONDecodeError:
        return ["Error reading quotes file. Please check JSON format."]
    

def get_inspirations():
    selected = random.choice(quotes)
    inspirations_label.config(text=selected)



def save_data():
    text = text_entry.get(1.0, tk.END).strip()
    
    if not text or text.isspace():
        status_label.config(text="Please enter a quote")
        return
    if len(text) < 3:
        status_label.config(text="Quote is too short (minimum 3 characters)")
        return
    if len(text) > 200:
        status_label.config(text="Quote is too long (maximum 200 characters)")
        return
    
    try:
        with open('quotes.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        new_quote = {"text": text, "source": "user"}
        data['quotes'].append(new_quote)
        
        with open('quotes.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        
        global quotes
        quotes = load_quotes()
        text_entry.delete(1.0, tk.END)
        status_label.config(text="Quote saved!")
        
    except Exception as e:
        status_label.config(text=f"Error: {e}")

def validate_quote(text):
    if not text or text.isspace():
        return False, "Please enter a quote"



quotes = load_quotes()

window = tk.Tk()
window.title("Inspiration Picker")
window.geometry("500x700")
window.config(bg='#768258')

title_label = tk.Label(window,
                      text="Your inspiration for today:",
                      font=('Courier', 16, 'normal'),
                      bg='#768258',
                      fg='black')
title_label.pack(padx=30, pady=30)

inspiration_button = tk.Button(window,
                              text='Get inspiration',
                              font=('Courier', 14, 'normal'),
                              bg="#C5B93F",
                              fg='black',
                              padx=10,
                              pady=10,
                              command=get_inspirations,
                              cursor='hand2',
                              activebackground="#C78015")
inspiration_button.pack(pady=30)

inspirations_label = tk.Label(window,
                             text='',
                             font=('Courier', 14, 'normal'),
                             bg='#768258',
                             fg='black',
                             wraplength=350)
inspirations_label.pack(pady=30, padx=30, fill='x')

text_label = tk.Label(window, text="Enter your quote:",
                      font=('Courier', 16, 'normal'),
                      bg='#768258',
                      fg='black')
text_label.pack(pady=30)

text_entry = tk.Text(window,
                      width=40,
                      height=3,
                      font=('Courier', 12, 'normal'),
                      wrap=tk.WORD)
text_entry.pack(pady=30)

save_button = tk.Button(window, text="Save", command=save_data,
                        font=('Courier', 14, 'normal'),
                        bg="#C5B93F",
                        fg='black',
                        padx=10,
                        pady=10,
                        cursor='hand2',
                        activebackground="#C78015")
save_button.pack(pady=30)

status_label = tk.Label(window, text="",
                        font=('Courier', 14, 'normal'),
                        bg='#768258',
                        fg='black',
                        wraplength=350)
status_label.pack(pady=30)

window.mainloop()