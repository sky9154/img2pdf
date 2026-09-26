# Image to PDF Converter

A lightweight desktop application built with Python and PySide6 for converting multiple images into a single PDF file.

## About

This project provides a simple graphical interface for converting a folder of images into a PDF document.

Users can select a folder containing images, choose where to save the output file, and convert the images into a PDF without using command-line tools.

The application is built with PySide6 for the graphical interface and uses Pillow and PyPDF2 for image and PDF processing.

## Screenshots

![Demo](/assets/docs/demo.png)

## Features

- **Graphical User Interface**: Provides a simple desktop interface built with PySide6.
- **Folder Selection**: Allows users to select a folder containing the images to be converted.
- **Image to PDF Conversion**: Converts multiple images into a single PDF document.
- **PDF Export**: Allows users to choose the location where the generated PDF file will be saved.
- **Simple Workflow**: Select an image folder and start the conversion without additional configuration.

## Getting Started

### Prerequisites

To run the source code, you need:

- Python 3.x
- pip (Python package installer)

### Installation

**1. Clone repo**

```bash
git clone https://github.com/sky9154/img2pdf.git
cd img2pdf
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

This command will install the required packages, including:

- `PySide6`
- `PyPDF2`
- `Pillow`

**3. Run application**

```bash
python app.py
```

## Usage

1. Launch the application.
2. Select the folder containing the images you want to convert.
3. Choose the location where the PDF file should be saved.
4. Start the conversion process.
5. The selected images will be converted into a PDF file.

## Folder Structure

```text
img2pdf/
├── assets/
│   └── images/         # Application resources and icons
├── dist/               # Distribution/build files
├── functions/          # Image processing and PDF conversion logic
├── widgets/            # Custom PySide6 UI components
├── app.py              # Main application entry point
├── requirements.txt    # Python dependencies
└── LICENSE             # Project license
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
