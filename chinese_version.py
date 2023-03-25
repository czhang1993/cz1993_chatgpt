# =================
# package importing
# =================
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
import openai

# ==========================
# root window configurations
# ==========================
# root window
# root = tk.Tk(screenName=None, baseName=None, className="Tk", useTk=True, sync=False, use=None)
root = ThemedTk(theme="winxpblue")
root.configure(bg="#C4E1B2")

# root window configurations
root.title("CZ1993 ChatGPT")
root.geometry("1280x720")

# ===========================
# widget style configurations
# ===========================
style = ttk.Style()

# style.theme_names()

style.configure("TLabel", font=("Microsoft YaHei", 11))
style.configure("TEntry", font=("Microsoft YaHei", 11))
style.configure("TButton", font=("Microsoft YaHei", 11))

font_text = ("Microsoft YaHei", 11)

# ========================
# OpenAI API key inputting
# ========================
# OpenAI API key label
label_key = ttk.Label(root, text="私钥")
label_key.configure(background="#C4E1B2")
label_key.pack(pady=(10, 5))

# OpenAI API key entry
entry_key = ttk.Entry(root, justify="center", width=60)
entry_key.pack(pady=5)


# OpenAI API key entered function
def key_entered():
    openai.api_key = entry_key.get()


# OpenAI API key enter button
button_key = ttk.Button(root, text="输入私钥", command=lambda: key_entered())
button_key.pack(pady=5)

# =================
# dialogue printing
# =================
text_dialogue = tk.Text(root, width=120, height=16, font=font_text, wrap="word")
# text_dialogue.configure(font=font_text)
text_dialogue.pack(pady=5)


# ===================
# chat class defining
# ===================
class Chat:
    def __init__(self, model="gpt-3.5-turbo", dialogue="", messages=[], inquiry=None, response=None):
        self.model = model
        self.dialogue = dialogue
        self.messages = messages
        self.inquiry = inquiry
        self.response = response

    def get_response(self):
        self.inquiry = text_inquiry.get("1.0", tk.END)
        self.messages.append({"role": "user", "content": self.inquiry})
        completion = openai.ChatCompletion.create(model=self.model, messages=self.messages)
        self.response = completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": self.response})

    def print_dialogue(self):
        text_dialogue.insert(tk.END, "你: " + self.inquiry + "\n")
        text_dialogue.insert(tk.END, "狗屁通: " + self.response + "\n")

    def chat(self):
        self.get_response()
        self.print_dialogue()


# ====================
# chat object creating
# ====================
object_chat = None


# chat created function
def chat_created():
    global object_chat
    object_chat = Chat()


# chat created button
button_key = ttk.Button(root, text="创建聊天", command=lambda: chat_created())
button_key.pack(before=text_dialogue, pady=5)

# ========
# chatting
# ========
# inquiry entry
text_inquiry = tk.Text(root, width=120, height=6, font=font_text, wrap="word")
text_inquiry.pack(side=tk.BOTTOM, pady=(5, 10))

# inquiry enter button
button_inquiry = ttk.Button(root, text="输入询问", command=lambda: object_chat.chat())
button_inquiry.pack(side=tk.BOTTOM, pady=5)

# =====================
# root loop circulation
# =====================
root.mainloop()
