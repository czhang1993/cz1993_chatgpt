# =================
# package importing
# =================
import as tk
import tkinter.ttk as ttk
import openai

# ==========================
# root window configurations
# ==========================
# root window
root = tk.Tk(screenName=None, baseName=None, className="Tk", useTk=True, sync=False, use=None)

# root window configurations
root.title("CZ1993 ChatGPT")
root.geometry("1280x720")

# =========================
widget style configurations
# =========================
# style = ttk.Style()

# style.theme_names()
# style.theme_use("default")

# style.configure("TLabel", font=("Calibri", 11))
# style.configure("TEntry", font=("Calibri", 11))
# style.configure("TButton", font=("Calibri", 11))

# ========================
# OpenAI API key inputting
# ========================
# OpenAI API key label
label_key = ttk.Label(root, text="Key")
label_key.pack(pady=5)

# OpenAI API key entry
entry_key = ttk.Entry(root, width=60)
entry_key.pack(pady=5)

# chat started function
label_chat_started = ttk.Label(root, text="Key Entered" + "\n" + "Chat Started")

messages = []
dialogue = ""

def chat_started():
    # assign OpenAI API key
    openai.api_key = entry_key.get()
    
    # pack chat started label
    label_chat_started.pack(pady=5)
    
    while True:
        inquiry = input()
        messages.append({"role": "user", "content": inquiry})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": response})
        dialogue = dialogue + "You: " + inquiry + "\n"
        dialogue = dialogue + "ChatGPT: " + response + "\n"

# OpenAI API key enter button
button_key = ttk.Button(root, text="Enter Key", command=lambda: chat_started())
button_key.pack(pady=5)

# =========================================
# inquiry inputting and response outputting
# =========================================
# dialogue label
text_label_dialogue = ""

label_dialogue = ttk.Label(root, text=text_label_dialogue)
label_dialogue.pack(pady=5)

# inquiry entry
entry_inquiry = ttk.Entry(root, width=60)
entry_inquiry.pack(side=tk.BOTTOM, pady=5)

# inquiry entered function
def inquiry_entered():
    inquiry = entry_inquiry.get()
    label_dialogue.config(text=dialogue)

# inquiry enter button
button_inquiry = ttk.Button(root, text="Enter Inquiry", command=lambda: inquiry_entered())
button_inquiry.pack(side=tk.BOTTOM, pady=5)
