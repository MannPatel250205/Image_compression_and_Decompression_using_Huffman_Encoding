# Huffman Image Compression Tool

This project is a GUI-based image compression and decompression tool using Huffman Coding. It is implemented in Python and uses Tkinter for the GUI.

## Features

- Compresses and decompresses image files using Huffman Coding.
- Supports formats like `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.bin`.
- Saves compressed images as `.bin` files and restores them to their original format.

## Project Structure

- **main.py**: Contains the GUI implementation for the compression tool.
- **huffman_coding.py**: Handles Huffman Coding for compression and decompression.
- **binary_data_handler.py**: Provides utility functions for reading, saving, and managing binary data.

## Installation

1. Clone the repository:
   ```bash
   gh repo clone MannPatel250205/Image_compression_and_Decompression_using_Huffman_Encoding
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application by running `main.py`.
2. Use the "Browse Image" button to select an image file.
3. Click "Compress Image" to compress the selected file.
4. To decompress, click "Decompress Image". The decompressed file will be saved in the `IO/Outputs` folder.

## Requirements

- Python 3.7 or later
- Required Python libraries (install using `pip`):
  - `tkinter`
  - `ttkthemes`
  - `json`
  - `os`

## File Details

- **main.py**:
  - Implements the GUI for user interactions.
  - Integrates the compression and decompression functionality.

- **huffman_coding.py**:
  - Builds Huffman trees based on byte frequencies.
  - Encodes and decodes binary data using Huffman Coding.

- **binary_data_handler.py**:
  - Handles reading binary data from files.
  - Saves and loads Huffman codes for reuse.
  - Writes compressed and decompressed images.

## Output

- Compressed images are stored as `compressed_image.bin` in the `IO/Outputs` folder.
- Decompressed images are saved as `decompressed_image.jpg` in the same folder.

## Future Improvements

- Add support for batch image processing.
- Provide real-time compression statistics.
- Extend file format support.

## Contributing

Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.