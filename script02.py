# =================
# package importing
# =================
import tkinter as tk
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

# ===========================
# widget style configurations
# ===========================
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

# OpenAI API key entered label
label_key_entered = ttk.Label(root, text="Key Entered")

# OpenAI API key entered function
def key_entered():
    openai.api_key = entry_key.get()
    label_key_entered.pack(pady=5)

# OpenAI API key enter button
button_key = ttk.Button(root, text="Enter Key", command=lambda: key_entered())
button_key.pack(pady=5)

# =================
# dialogue printing
# =================
text_dialogue = tk.Text(root, width=800, height=600, wrap="WORD")
text_dialogue.pack(pady=5)

# ===================
# chat class defining
# ===================
class chat:
    def __init__(self, model="gpt-3.5-turbo", dialogue="", messages=[]):
        self.model = model
        self.dialogue = dialogue
        self.messages = messages
    
    def chat():
        inquiry = entry_inquiry.get()
        self.messages.append({"role": "user", "content": inquiry})
        completion = openai.ChatCompletion.create(model=self.model, messages=self.messages)
        response = completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response})

    def print_dialogue():
        text_dialogue.insert("You: " + inquiry + "\n")
        text_dialogue.insert("ChatGPT: " + response + "\n")

# ======================
# ChatGPT model creating
# ======================
