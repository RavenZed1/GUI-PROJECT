from tkinter import *
from tkinter import messagebox

import customtkinter as ctk

app = ctk.CTk()
app.title('Lamanilao Unit Converter')
app.geometry('500x450')
app.config(bg='#020a24')

font1 = ('Roboto', 30, 'bold')
font2 = ('Arial', 25, 'bold')
font3 = ('Arial', 15, 'bold')

unit_options = ['Length', 'Mass', 'Volume', 'Temperature']  # Added 'Temperature' to unit options
length_options = ['Meter', 'Centimeter', 'Foot']
mass_options = ['Kilogram', 'Gram', 'Pound']
volume_options = ['Liter', 'Milliliter', 'Gallon']
temperature_options = ['Celsius', 'Fahrenheit', 'Kelvin']  # Added temperature options
variable1 = ctk.StringVar()
variable2 = ctk.StringVar()
variable3 = ctk.StringVar()

def convert():
    length_factors = {'Meter': 1, 'Centimeter': 0.01, 'Foot': 0.3048}
    mass_factors = {'Kilogram': 1, 'Gram': 0.0001, 'Pound': 0.453592}
    volume_factors = {'Liter': 1, 'Milliliter': 0.001, 'Gallon': 3.78541}
    temperature_factors = {'Celsius': (lambda x: x), 'Fahrenheit': (lambda x: (x - 32) * 5 / 9), 'Kelvin': (lambda x: x - 273.15)}
    
    try:
        if variable1.get() == 'Length':
            meters = float(value_entry.get()) * length_factors[variable2.get()]
            converted_value = meters / length_factors[variable3.get()]
        elif variable1.get() == 'Mass':
            kilograms = float(value_entry.get()) * mass_factors[variable2.get()]
            converted_value = kilograms / mass_factors[variable3.get()]
        elif variable1.get() == 'Volume':
            liters = float(value_entry.get()) * volume_factors[variable2.get()]
            converted_value = liters / volume_factors[variable3.get()]
        elif variable1.get() == 'Temperature':  # Added condition for temperature conversion
            original_value = float(value_entry.get())
            converted_value = temperature_factors[variable3.get()](original_value)
            converted_value = temperature_factors[variable2.get()](converted_value)
        result_label.configure(text=f'{value_entry.get()}{variable2.get()} = {converted_value:.2f} {variable3.get()}')
    except ValueError:
        messagebox.showerror('Error', 'Enter valid values!')

title_label = ctk.CTkLabel(app, font=font1, text='Unit Converter', text_color='#fff', bg_color='#020a24')
title_label.place(x=150, y=20)

unit_label = ctk.CTkLabel(app, font=font2, text='Unit', text_color='#fff', bg_color='#020a24')
unit_label.place(x=220, y=80)

unit_option = ctk.CTkComboBox(app, font=font3, text_color='#000', fg_color='#fff', dropdown_hover_color='#06911f', values=unit_options, variable=variable1, width=120)
unit_option.place(x=195, y=110)

from_label = ctk.CTkLabel(app, font=font2, text='From', text_color='#fff', bg_color='#020a24')
from_label.place(x=130, y=235)

from_option = ctk.CTkComboBox(app, font=font3, text_color='#000', fg_color='#fff', dropdown_hover_color='#06911f', variable=variable2, width=120)
from_option.place(x=100, y=275)

to_label = ctk.CTkLabel(app, font=font2, text='to', text_color='#fff', bg_color='#020a24')
to_label.place(x=320, y=235)

to_option = ctk.CTkComboBox(app, font=font3, text_color='#000', fg_color='#fff', dropdown_hover_color='#06911f', variable=variable3, width=120)
to_option.place(x=280, y=275)

value_label = ctk.CTkLabel(app, font=font2, text='Value', text_color='#fff', bg_color='#020a24')
value_label.place(x=210, y=150)

value_entry = ctk.CTkEntry(app, font=font3, text_color='#000', fg_color='#fff', border_color='#fff', width=150)
value_entry.place(x=180, y=180)

convert_button = ctk.CTkButton(app, command=convert, font=font2, text_color='#fff', text='Convert', fg_color='#eb05ae', hover_color='#a8057d', bg_color='#020a24', cursor='hand2', corner_radius=10, width=200)
convert_button.place(x=150, y=320)

result_label = ctk.CTkLabel(app, font=font2, text=' ', text_color='#fff', bg_color='#020a24')
result_label.place(x=130, y=380)

def update_options(*args):
    if variable1.get() == 'Length':
        from_option.configure(values=length_options)
        to_option.configure(values=length_options)
        from_option.set('Meter')
        to_option.set('Centimeter')
    elif variable1.get() == 'Mass':
        from_option.configure(values=mass_options)
        to_option.configure(values=mass_options)
        from_option.set('Kilogram')
        to_option.set('Gram')
    elif variable1.get() == 'Volume':
        from_option.configure(values=volume_options)
        to_option.configure(values=volume_options)
        from_option.set('Liter')
        to_option.set('Milliliter')
    elif variable1.get() == 'Temperature':  # Added condition for temperature options
        from_option.configure(values=temperature_options)
        to_option.configure(values=temperature_options)
        from_option.set('Celsius')
        to_option.set('Fahrenheit')

variable1.trace("w", update_options)
app.mainloop()