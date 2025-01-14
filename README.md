# MDify X - File to Markdown Converter

A simple Streamlit app that allows users to convert various document types into Markdown format. The app supports file uploads and URL inputs, utilizing the Docling library for document conversion.

## Features

- Convert uploaded files (DOCX, PDF, TXT, HTML) to Markdown format.
- Download converted Markdown file directly from the app.
- Option to provide a URL to download and convert documents.
- Displays the converted Markdown content in an expandable section.
- Includes error handling with logging for conversion and download issues.

## Installation

To run the app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/tharunkumarra-mdify-x.git
   cd tharunkumarra-mdify-x
   ```

2. Set up a Python environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

The app should open in your default browser at `http://localhost:8501`.

## Usage

Once the app is running:

1. **Upload a file**: You can upload DOCX, PDF, TXT, or HTML files for conversion to Markdown format.
2. **Enter a URL**: You can provide a URL to download a document and convert it to Markdown.
3. The converted Markdown content will be displayed in an expandable section.
4. You can download the converted Markdown file by clicking the **Download Markdown File** button.

## Libraries Used

- **Streamlit**: Web app framework for building the UI.
- **Requests**: For downloading documents from URLs.
- **Docling**: Converts various document formats to Markdown.

## Error Handling

- The app logs any errors that occur during the conversion or download process. These errors will be displayed in the Streamlit app as error messages.

## Contribution

Feel free to fork the repository and contribute! If you find any issues or have suggestions, open an issue or create a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).
