# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:11:01 2023

@author: BRGUBO
"""

import tkinter as tk
from tkinter import ttk
from two_proportion import *
from tkinter import messagebox
#import pyperclip
app_name = 'TRIAL FIT'
code_version = '0.9'

def copy_clipboard_sample(text):
    #a = f'test de clipboard {s_prop1}'
    frame1.clipboard_clear()
    frame1.clipboard_append(text)
    frame1.update()

def copy_clipboard_power(text):
    #a = f'test de clipboard {s_prop1}'
    frame1.clipboard_clear()
    frame1.clipboard_append(text)
    frame1.update()


def msg_error(text):
    tk.messagebox.showerror(title=None, message=text )
    

def validade_prop(p1,p2):
    
    if p1 == p2:
       msg_error('Proportion 1 & proportion 2 should be different') 
    if p1>1 or p1<0:
       msg_error('Proportion 1 should be between 0 and 100') 
    if p2>1 or p2<0:
       msg_error('Proportion 1 should be between 0 and 100') 

def calc_sample_size():
    
    s_prop1 = float(s_prop1_entry_str.get())/100
    s_prop2 = float(s_prop2_entry_str.get())/100
    p_value= s_p_value_str.get()
    pwr= s_power_value_str.get()
    hypo_bool= s_hypo_status.get() # false = 1 side
    
    validade_prop(s_prop1, s_prop2)
    
    
    if hypo_bool: # 2 sides
        side=2
    else:
        side=1
    diff_p = s_prop2-s_prop1
    
    #print(s_prop1, s_prop2, p_value,pwr, hypo_bool, side )
    
    value_sample_size = Two_proportion(s_prop1, s_prop2, p_value, pwr, side)
    ss_value = int(round(value_sample_size.sample_size(),0))
    s_result_sample_strvar.set(str(ss_value))
    
    #copy_clipboard_sample()
    sample_text = f'\n{app_name} - Sample Size for Two Independent Proportions\n\nProportion 1: {s_prop1 * 100} %\nProportion 2: {s_prop2 * 100} %\nDelta: {round(diff_p*100,1)}% - ({round(diff_p/s_prop1*100,1)}%)\nP value: {p_value}\nPower: {pwr * 100}%\nHa different?: {hypo_bool}\n\nSample size needed: {ss_value} / group\n\n'
    btn_clipboard1_str = tk.StringVar()
    btn_clipboard1_str.set(sample_text)
    
    
    btn_clipboard1 = ttk.Button(widgets_frame, text='Results to Clipboard', command=copy_clipboard_sample(sample_text))
    btn_clipboard1.grid(row=11, column=0, sticky='news', padx=5, pady=5)
    
    
def power_calc():
    p_prop1 = float(p_prop1_entry_str.get())/100
    p_prop2 = float(p_prop2_entry_str.get())/100
    p_value2 = p_value_str.get()
    sample_size2= int(p_sample_size_entry_str.get())
    ha_bollean2=p_hypo_status.get()
    
    validade_prop(p_prop1, p_prop2)
    
    if sample_size2 <=0:
        msg_error('Sample size cannot be less or egual than ZERO')
    
    if ha_bollean2: # 2 sides
        side=2
    else:
        side=1
    diff_p2 = p_prop2-p_prop1   
    #print(p_prop1, p_prop2, p_value2,sample_size2,ha_bollean2)
    pwr_calc_result = power_prop(p_prop1, p_prop2, sample_size2, p_value2, side)*100
    #print(pwr_calc_result)
    p_result_sample_strvar.set(f'{str(pwr_calc_result)} %')
    
    #copy_clipboard_sample()
    power_text = f'\n{app_name} - Power Calculation for Two Independent Proportions\n\nProportion 1: {p_prop1 * 100} %\nProportion 2: {p_prop2 * 100} %\nDelta: {round(diff_p2*100,1)}% - ({round(diff_p2/p_prop1*100,1)}%)\nP value: {p_value2}\nSample size: {sample_size2}\nHa different?: {ha_bollean2}\n\nPower (1 - Type II error): {pwr_calc_result}%\n\n'
    btn_clipboard1_str = tk.StringVar()
    btn_clipboard1_str.set(power_text)
    
    
    btn_clipboard2 = ttk.Button(p_widgets_pwr_frame, text='Results to Clipboard', command=copy_clipboard_power(power_text))
    btn_clipboard2.grid(row=11, column=1, sticky='news', padx=5, pady=5)
    
    

    
        

root=tk.Tk()
style=ttk.Style(root)
root.tk.call('source', 'forest-dark.tcl')
#style.theme_create('forest-light')
root.title(f'{app_name} - Two Independent Proportions - code v.{code_version}')
root.resizable(0,0) # does not permit roor to be resized

frame1 = ttk.Frame(root)
frame1.pack()

widgets_frame = ttk.LabelFrame(frame1,text='Sample size Calculation')
widgets_frame.grid(row=0, column=0, padx=30, pady=30)

s_prop1_entry_str = tk.StringVar()
s_prop1_entry = ttk.Entry(widgets_frame,textvariable=s_prop1_entry_str )
s_prop1_entry.insert(0,'Prop. 1 (%)')
s_prop1_entry.grid(row=0, column=0, sticky='we',  padx=5, pady=5)
s_prop1_entry.bind('<FocusIn>', lambda e:s_prop1_entry.delete('0','end'))

s_prop2_entry_str = tk.StringVar()
s_prop2_entry = ttk.Entry(widgets_frame,textvariable=s_prop2_entry_str )
s_prop2_entry.insert(0,'Prop. 2 (%)')
s_prop2_entry.grid(row=1, column=0, sticky='we', padx=5, pady=5)
s_prop2_entry.bind('<FocusIn>', lambda e:s_prop2_entry.delete('0','end'))

s_p_lbl = ttk.Label(widgets_frame, text='P value:')
s_p_lbl.grid(row=2, column=0, sticky='w', padx=5, pady=5)


s_p_value_str = tk.DoubleVar()
s_p_value_spin = ttk.Spinbox(widgets_frame, from_= 0.01, to=0.1, increment=0.01, textvariable=s_p_value_str)
s_p_value_str.set(0.05)
s_p_value_spin.grid(row=3, column=0, sticky='we', padx=5, pady=5)

s_power_lbl = ttk.Label(widgets_frame, text='Power')
s_power_lbl.grid(row=4, column=0, sticky='w', padx=5, pady=5)

s_power_value_str = tk.DoubleVar()
s_power_value_spin = ttk.Spinbox(widgets_frame, from_= 0.7, to=0.95, increment=0.05, textvariable=s_power_value_str)
s_power_value_str.set(0.8)
s_power_value_spin.grid(row=5, column=0, sticky='we', padx=5, pady=5)

s_hypo_status = tk.BooleanVar()
s_hypothesis_checkbtn = ttk.Checkbutton(widgets_frame, text='Ha = Different', variable=s_hypo_status)
s_hypo_status.set(False)
s_hypothesis_checkbtn.grid(row=6, column=0, sticky='news', padx=5, pady=5)

s_run_btn = ttk.Button(widgets_frame, text='Run', command=calc_sample_size)
s_run_btn.grid(row=7, column=0, sticky='news', padx=5, pady=5)


s_separator1 = ttk.Separator(widgets_frame)
s_separator1.grid(row=8, column=0, sticky='news', padx=5, pady=5)

s_result_sample_size_lbl = ttk.Label(widgets_frame, text='Sample size / group')
s_result_sample_size_lbl.grid(row=9, column=0, sticky='we', padx=5, pady=5)

s_result_sample_strvar = tk.StringVar()
s_result_sample_size_entry = ttk.Entry(widgets_frame, text='', textvariable=s_result_sample_strvar)
s_result_sample_strvar.set('')
s_result_sample_size_entry.grid(row=10, column=0, sticky='we', padx=5, pady=5)
s_result_sample_size_entry.configure(state='disable', font=('Helvetica', 14), foreground="#000080")


btn_clipboard1_str = tk.StringVar()
btn_clipboard1 = ttk.Button(widgets_frame, text='Results to Clipboard', command=copy_clipboard_sample)
btn_clipboard1.grid(row=11, column=0, sticky='news', padx=5, pady=5)


# -------------------------------------------------------------



p_widgets_pwr_frame = ttk.LabelFrame(frame1,text='Power Calculation')
p_widgets_pwr_frame.grid(row=0, column=1, padx=30, pady=30)

p_prop1_entry_str = tk.StringVar()
p_prop1_entry = ttk.Entry(p_widgets_pwr_frame,textvariable=p_prop1_entry_str )
p_prop1_entry.insert(0,'Prop. 1 (%)')
p_prop1_entry.grid(row=0, column=1, sticky='we', padx=5, pady=5)
p_prop1_entry.bind('<FocusIn>', lambda e:p_prop1_entry.delete('0','end'))

p_prop2_entry_str = tk.StringVar()
p_prop2_entry = ttk.Entry(p_widgets_pwr_frame, textvariable=p_prop2_entry_str )
p_prop2_entry.insert(0,'Prop. 2 (%)')
p_prop2_entry.grid(row=1, column=1, sticky='we', padx=5, pady=5)
p_prop2_entry.bind('<FocusIn>', lambda e:p_prop2_entry.delete('0','end'))

p_lbl = ttk.Label(p_widgets_pwr_frame, text='P value:')
p_lbl.grid(row=2, column=1, sticky='w', padx=5, pady=5)


p_value_str = tk.DoubleVar()
p_value_spin = ttk.Spinbox(p_widgets_pwr_frame, from_= 0.01, to=0.1, increment=0.01, textvariable=p_value_str)
p_value_str.set(0.05)
p_value_spin.grid(row=3, column=1, sticky='we', padx=5, pady=5)

p_power_lbl = ttk.Label(p_widgets_pwr_frame, text='Sample Size')
p_power_lbl.grid(row=4, column=1, sticky='w', padx=5, pady=5)


p_sample_size_entry_str = tk.StringVar()
p_sample_size_entry = ttk.Entry(p_widgets_pwr_frame, textvariable=p_sample_size_entry_str )
p_sample_size_entry.insert(0,'Sample size / group')
p_sample_size_entry.grid(row=5, column=1, sticky='we', padx=5, pady=5)
p_sample_size_entry.bind('<FocusIn>', lambda e:p_sample_size_entry.delete('0','end'))
  


p_hypo_status = tk.BooleanVar()
p_hypothesis_checkbtn = ttk.Checkbutton(p_widgets_pwr_frame, text='Ha = Different', variable=p_hypo_status)
p_hypo_status.set(False)
p_hypothesis_checkbtn.grid(row=6, column=1, sticky='news', padx=5, pady=5)

p_run_btn = ttk.Button(p_widgets_pwr_frame, text='Run', command=power_calc)
p_run_btn.grid(row=7, column=1, sticky='news', padx=5, pady=5)


p_separator1 = ttk.Separator(p_widgets_pwr_frame)
p_separator1.grid(row=8, column=1, sticky='news', padx=5, pady=5)

p_result_sample_size_lbl = ttk.Label(p_widgets_pwr_frame, text='Power (1 - type II error)')
p_result_sample_size_lbl.grid(row=9, column=1, sticky='we', padx=5, pady=5)

p_result_sample_strvar = tk.StringVar()
p_result_sample_size_entry = ttk.Entry(p_widgets_pwr_frame, text='', textvariable=p_result_sample_strvar)
p_result_sample_strvar.set('  %')
p_result_sample_size_entry.grid(row=10, column=1, sticky='we', padx=5, pady=5)
p_result_sample_size_entry.configure(state='disable',font=('Helvetica', 14),foreground="#000080")

btn_clipboard2_str = tk.StringVar()
btn_clipboard2 = ttk.Button(p_widgets_pwr_frame, text='Results to Clipboard', command=copy_clipboard_power)
btn_clipboard2.grid(row=11, column=1, sticky='news', padx=5, pady=5)


# -------------------------------------------------------------


root.mainloop()
