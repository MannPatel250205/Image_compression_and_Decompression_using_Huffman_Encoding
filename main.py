import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk
import binary_data_handler
import huffman_coding
import os

class ImageCompressionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Compression & Decompression")
        
        # Set full screen mode
        self.root.attributes("-fullscreen", True)
        self.root.config(bg="#2b2d42")

        # Create a frame to organize widgets
        main_frame = tk.Frame(self.root, bg="#2b2d42", padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Header section
        header = tk.Label(
            main_frame, text="Image Compression Tool", 
            font=("Helvetica", 28, "bold"), fg = "#edf2f4", bg = "#2b2d42"
        )
        header.pack(pady=20)

        # Image selection section
        self.image_path_entry = ttk.Entry(main_frame, width=50, font=("Arial", 14))
        self.image_path_entry.pack(pady=10)

        browse_button = ttk.Button(main_frame, text="Browse Image", command=self.browse_image)
        browse_button.pack(pady=10)

        button_frame = tk.Frame(main_frame, bg="#2b2d42")
        button_frame.pack(pady=30)

        self.compress_button = ttk.Button(button_frame, text="Compress Image", command=self.compress_image)
        self.compress_button.grid(row=0, column=0, padx=10)

        self.decompress_button = ttk.Button(button_frame, text="Decompress Image", command=self.decompress_image)
        self.decompress_button.grid(row=0, column=1, padx=10)

        # Status label
        self.status_label = tk.Label(
            main_frame, text="", font=("Arial", 12), fg="#8d99ae", bg="#2b2d42"
        )
        self.status_label.pack(pady=10)

        # Exit Button
        exit_button = ttk.Button(main_frame, text="Exit", command=self.exit_full_screen)
        exit_button.pack(pady=20)

    def browse_image(self):
        
        image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bin *.bmp")]
        )
        self.image_path_entry.delete(0, tk.END)
        self.image_path_entry.insert(0, image_path)

    def compress_image(self):
        try:
            image_path = self.image_path_entry.get()
            if not image_path:
                messagebox.showwarning("Warning", "Please select an image.")
                return

            # Compress the image
            self.status_label.config(text="Compressing image...")
            self.root.update_idletasks()

            bit_string = binary_data_handler.read_image_bit_string(image_path)
            compressed_bit_string = huffman_coding.compress(bit_string)

            save_path = "IO/Outputs/compressed_image.bin"
            binary_data_handler.save_data(compressed_bit_string, save_path, 'image')

            compression_ratio = len(bit_string) / len(compressed_bit_string)
            messagebox.showinfo("Success", f"Image compressed successfully!\n")
            self.status_label.config(text="Compression completed.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to compress image: {str(e)}")

    def decompress_image(self):
        try:
            compressed_path = "IO/Outputs/compressed_image.bin"
            if not os.path.exists(compressed_path):
                messagebox.showwarning("Warning", "No compressed image found!")
                return

            # Decompress the image
            self.status_label.config(text="Decompressing image...")
            self.root.update_idletasks()

            compressed_data = binary_data_handler.read_image_bit_string(compressed_path)
            decompressed_data = huffman_coding.decompress(compressed_data)

            decompressed_path = "IO/Outputs/decompressed_image.jpg"
            binary_data_handler.save_data(decompressed_data, decompressed_path, 'image')

            messagebox.showinfo("Success", "Image decompressed successfully!")
            self.status_label.config(text="Decompression completed.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decompress image: {str(e)}")

    def exit_full_screen(self):
        self.root.attributes("-fullscreen", False)
        self.root.quit()

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = ImageCompressionGUI(root)
    root.mainloop()