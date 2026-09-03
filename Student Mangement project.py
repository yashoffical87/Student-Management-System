import tkinter as tk
from tkinter import messagebox

students = {}

def add_student():
    roll = roll_entry.get()
    name = name_entry.get()
    course = course_entry.get()

    if roll in students:
        messagebox.showerror("Error", "Roll number already exists!")
    else:
        students[roll] = {"Name": name, "Course": course}
        messagebox.showinfo("Success", f"Student {name} added successfully!")
        clear_entries()

def view_students():
    if not students:
        messagebox.showinfo("Info", "No student records found.")
    else:
        records = "\n".join([f"Roll: {r}, Name: {d['Name']}, Course: {d['Course']}" 
                             for r, d in students.items()])
        messagebox.showinfo("Student Records", records)

def search_student():
    roll = roll_entry.get()
    if roll in students:
        d = students[roll]
        messagebox.showinfo("Found", f"Roll: {roll}, Name: {d['Name']}, Course: {d['Course']}")
    else:
        messagebox.showerror("Error", "Student not found.")

def update_student():
    roll = roll_entry.get()
    if roll in students:
        students[roll] = {"Name": name_entry.get(), "Course": course_entry.get()}
        messagebox.showinfo("Success", "Student record updated successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Student not found.")

def delete_student():
    roll = roll_entry.get()
    if roll in students:
        del students[roll]
        messagebox.showinfo("Deleted", "Student deleted successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Student not found.")

def clear_entries():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Student Management System")
root.geometry("400x400")

# Labels and Entries
tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()


tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Search Student", command=search_student).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()
