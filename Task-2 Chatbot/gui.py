import tkinter as tk
from chatbot import Function_forInput

def To_send(event=None):
    Input_user = entry.get()
    
    entry.delete(0, tk.END)
    
    # user input in text widget
    text.insert(tk.END, f'User: {Input_user}\n')
    
    # response from chatbot
    response = Function_forInput(Input_user)
    
    # displaying the response
    text.insert(tk.END, f'Chatbot: {response}\n')
    
    text.see(tk.END)

root = tk.Tk()
root.title('Chatbot')

# set the window background color
root.configure(bg='#F0F0F0')

frame = tk.Frame(root, bg='#F0F0F0')
frame.pack(pady=20)

#  label for chatbot's name
label = tk.Label(frame, text='CHATBOT', font=('Times', 18, 'bold'), bg='Gray94', fg='#333333')
label.pack()

text_frame = tk.Frame(frame, bg='#F0F0F0')
text_frame.pack(pady=10)

# creating a scrollbar 
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(text_frame, width=80, height=15, font=('Roboto', 14), bg='#FFFFFF', fg='#333333', yscrollcommand=scrollbar.set)
text.pack(side=tk.LEFT)

# scrollbar to scroll
scrollbar.config(command=text.yview)

# entry widget to input
entry = tk.Entry(frame, font=('Roboto', 14), bg='#FFFFFF', fg='#333333')
entry.pack(pady=10)

# Enter key for sending input
entry.bind('<Return>', To_send)

# Button to send Input
button = tk.Button(frame, text='Send', font=('Times', 14), bg='#333333', fg='#FFFFFF', command=To_send)
button.pack(pady=10)

root.mainloop()
