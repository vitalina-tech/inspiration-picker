import tkinter as tk
import random

inspirations=[
             'No plan? Perfect. Do it freestyle.',
             'Time is fake. You\'re not late.',
             'Today\'s effort is tomorrow\'s strength',
             'If something scares you, make it your curiosity project',
             'To build something new, you must first break something old',
             'Great victories come from brave decisions',
             'Take three deep breaths',
             'Look up at the sky for 20 seconds',
             'Send someone a kind message',
             'Trust your journey - it\'s uniquely yours']

def get_inspirations():
    selected=random.choice(inspirations)
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