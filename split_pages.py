import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

def split_pdf(input_file):
    try:
        # Create a directory for the split files
        base_dir = os.path.dirname(input_file)
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        output_dir = os.path.join(base_dir, file_name)
        os.makedirs(output_dir, exist_ok=True)  # Create folder if it doesn't exist
        
        with open(input_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[page_num])
                
                output_file = os.path.join(output_dir, f'{file_name}_page_{page_num + 1}.pdf')
                with open(output_file, 'wb') as output:
                    writer.write(output)
        
        messagebox.showinfo("Success", f"PDF has been split into individual pages and saved in:\n{output_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        split_pdf(file_path)

# Set up the GUI
root = tk.Tk()
root.title("PDF Splitter")
# Center the window
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Create a button to select the PDF file
select_button = tk.Button(root, text="Select PDF File", command=select_pdf_file)
select_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
