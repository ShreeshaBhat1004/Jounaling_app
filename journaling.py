import datetime
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(f"{datetime.datetime.now()}: {entry}")

    def view_entries(self):
        return self.entries

    def save_entries(self):
        with open("journal.txt", "w") as file:
            for entry in self.entries:
                file.write(f"{entry}\n")

class JournalApp:
    def __init__(self, root):
        self.journal = Journal()
        self.root = root
        self.entry_text = tk.StringVar()
        self.entry_box = tk.Entry(root, textvariable=self.entry_text)
        self.entry_box.pack()
        self.entry_list = tk.Listbox(root)
        self.entry_list.pack()
        self.add_button = tk.Button(root, text="Add Entry", command=self.add_entry)
        self.add_button.pack()
        self.view_button = tk.Button(root, text="View Entries", command=self.view_entries)
        self.view_button.pack()
        self.save_button = tk.Button(root, text="Save Entries", command=self.save_entries)
        self.save_button.pack()
        self.draw_pie_chart()

    def add_entry(self):
        entry = self.entry_text.get()
        self.journal.add_entry(entry)
        self.entry_list.insert(tk.END, entry)
        self.entry_text.set("")

    def view_entries(self):
        self.entry_list.delete(0, tk.END)
        for entry in self.journal.view_entries():
            self.entry_list.insert(tk.END, entry)

    def save_entries(self):
        self.journal.save_entries()
        messagebox.showinfo("Journal", "Entries saved successfully!")

    def draw_pie_chart(self):
        labels = ['Social life', 'Studies', 'Personal projects', 'Personal fun']
        sizes = [25, 25, 25, 25]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        chart = FigureCanvasTkAgg(fig, master=self.root)
        chart.get_tk_widget().pack()

def main():
    root = tk.Tk()
    root.configure(background='#D8BFD8')
    app = JournalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
