import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
import pyvista as pv
import traceback

# --- Generate 3D Text ---
def generate_3d_text(text_input):
    if not text_input:
        messagebox.showerror("Error", "Please enter some text.")
        return

    try:
        # Create the 3D text mesh
        text_mesh = pv.Text3D(text_input)
        plotter = pv.Plotter()
        plotter.add_mesh(text_mesh)
        plotter.show()
        return text_mesh
    except Exception as e:
        traceback.print_exc()  # Print full error traceback
        messagebox.showerror("Error", f"Error while generating 3D text:\n\n{e}")

# --- Save Plot ---
def save_plot(text_mesh):
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".stl", filetypes=[("STL File", ".stl"), ("OBJ File", ".obj")])
        if file_path:
            if file_path.endswith(".stl"):
                text_mesh.save(file_path)
            elif file_path.endswith(".obj"):
                text_mesh.save(file_path)
            messagebox.showinfo("Success", "Plot saved successfully.")
    except Exception as e:
        traceback.print_exc()  # Print full error traceback
        messagebox.showerror("Error", f"Error while saving plot:\n\n{e}")

# --- GUI Setup ---
def create_gui():
    root = tk.Tk()
    root.title("3D Text Generator")
    root.geometry("600x350")

    label = tk.Label(root, text="Enter text below to render it in 3D using PyVista.", wraplength=450, justify="left")
    label.pack(pady=10)

    text_label = tk.Label(root, text="Enter Text for 3D Rendering:")
    text_label.pack(pady=5)

    text_entry = tk.Entry(root, width=40)
    text_entry.pack()

    text_mesh = None

    def on_click():
        nonlocal text_mesh
        text = text_entry.get()
        text_mesh = generate_3d_text(text)

    def on_save():
        nonlocal text_mesh
        if text_mesh:
            save_plot(text_mesh)
        else:
            messagebox.showerror("Error", "No plot to save. Please generate 3D text first.")

    text_btn = tk.Button(root, text="Generate 3D Text", command=on_click, padx=10, pady=5)
    text_btn.pack(pady=5)

    save_btn = tk.Button(root, text="Save Plot", command=on_save, padx=10, pady=5)
    save_btn.pack(pady=5)

    root.mainloop()

# --- Run App ---
if __name__== "__main__":
    create_gui()