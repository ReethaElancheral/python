# text_editor.py

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import time
from functools import wraps

RECENT_FILES_PATH = "recent_files.txt"

def autosave(func):
    """Decorator to autosave file before critical actions."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.current_file and self.text.get("1.0", tk.END).strip():
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END))
        return func(self, *args, **kwargs)
    return wrapper

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python CLI Text Editor")
        self.root.geometry("800x600")

        self.text = tk.Text(root, undo=True, wrap="word")
        self.text.pack(expand=True, fill="both")

        self.current_file = None
        self.recent_files = self.load_recent_files()

        self.setup_menu()

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Search", command=self.search_text)
        edit_menu.add_command(label="Replace", command=self.replace_text)

        recent_menu = tk.Menu(menubar, tearoff=0)
        for file in self.recent_files:
            recent_menu.add_command(label=file, command=lambda f=file: self.open_recent(f))

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        menubar.add_cascade(label="Recent", menu=recent_menu)

        self.root.config(menu=menubar)

    def load_recent_files(self):
        if os.path.exists(RECENT_FILES_PATH):
            with open(RECENT_FILES_PATH, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines() if os.path.exists(line.strip())]
        return []

    def update_recent_files(self, path):
        if path in self.recent_files:
            self.recent_files.remove(path)
        self.recent_files.insert(0, path)
        self.recent_files = self.recent_files[:5]  # Keep only last 5
        with open(RECENT_FILES_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(self.recent_files))

    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.current_file = None
        self.root.title("Untitled - Text Editor")

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)
                self.current_file = path
                self.root.title(f"{os.path.basename(path)} - Text Editor")
                self.update_recent_files(path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def open_recent(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, content)
            self.current_file = path
            self.root.title(f"{os.path.basename(path)} - Text Editor")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

    @autosave
    def save_file(self):
        if not self.current_file:
            self.save_file_as()
        else:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(self.text.get("1.0", tk.END))
                messagebox.showinfo("Saved", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save: {e}")

    def save_file_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.text.get("1.0", tk.END))
                self.current_file = path
                self.root.title(f"{os.path.basename(path)} - Text Editor")
                self.update_recent_files(path)
            except Exception as e:
                messagebox.showerror("Error", f"Could not save: {e}")

    def search_text(self):
        keyword = tk.simpledialog.askstring("Search", "Enter text to search:")
        if keyword:
            start = "1.0"
            self.text.tag_remove("highlight", "1.0", tk.END)
            while True:
                start = self.text.search(keyword, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(keyword)}c"
                self.text.tag_add("highlight", start, end)
                start = end
            self.text.tag_config("highlight", background="yellow")

    def replace_text(self):
        search = tk.simpledialog.askstring("Replace", "Text to replace:")
        replace = tk.simpledialog.askstring("Replace", "Replace with:")
        if search and replace:
            content = self.text.get("1.0", tk.END)
            new_content = content.replace(search, replace)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, new_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

