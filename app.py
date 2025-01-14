import streamlit as st
import os
import tempfile
import requests
from docling.document_converter import DocumentConverter
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Function to handle the document conversion
def convert_to_md(source):
    try:
        # Initialize DocumentConverter and convert to Markdown
        converter = DocumentConverter()
        result = converter.convert(source)
        return result.document.export_to_markdown()
    except Exception as e:
        st.error(f"An error occurred during conversion: {e}")
        logging.error(f"Error during conversion: {e}")
        return None

# Function to download a file from a URL
def download_file_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Save the content as a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, mode='wb')
            temp_file.write(response.content)
            temp_file.close()
            logging.info(f"File downloaded successfully: {url}")
            return temp_file.name
        else:
            st.error("Failed to download the file. Please check the URL.")
            logging.error(f"Failed to download file from URL: {url}")
            return None
    except Exception as e:
        st.error(f"Error while downloading the file from URL: {e}")
        logging.error(f"Error while downloading file from URL: {e}")
        return None

def main():
    st.title("File to Markdown Converter")

    # Centered placeholder text in grey color (2 lines)
    st.markdown("""
        <style>
            .placeholder {
                color: #888;
                font-size: 1.2em;
                text-align: center;
                margin-top: 40px;
            }
        </style>
        <div class="placeholder">
            Upload a file or enter a URL <br> to convert it into Markdown format.
        </div>
    """, unsafe_allow_html=True)

    st.sidebar.title("File Upload Options")
    st.sidebar.write("Upload a file or provide a URL to convert it to Markdown format using Docling.")

    # File uploader section
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["docx", "pdf", "txt", "html"])

    # URL input section
    url_input = st.sidebar.text_input("Or enter a URL to download and convert a document")

    if uploaded_file is not None:
        # Show progress bar
        with st.spinner("Converting your file..."):
            # Save the uploaded file temporarily using tempfile
            with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_name = temp_file.name

            # Convert the file to Markdown
            markdown_content = convert_to_md(temp_file_name)

            if markdown_content:
                st.success("File converted successfully!")
                st.code(markdown_content, language="markdown")

                # Provide a download button
                st.download_button(
                    label="Download Markdown File",
                    data=markdown_content,
                    file_name=f"{uploaded_file.name}.md",
                    mime="text/markdown"
                )

            os.remove(temp_file_name)  # Clean up the temporary file

    elif url_input:
        # Show progress bar
        with st.spinner("Downloading and converting document from URL..."):
            temp_file_name = download_file_from_url(url_input)
            if temp_file_name:
                markdown_content = convert_to_md(temp_file_name)
                if markdown_content:
                    st.success("File converted successfully!")
                    st.code(markdown_content, language="markdown")
                    st.download_button(
                        label="Download Markdown File",
                        data=markdown_content,
                        file_name=f"converted_from_url.md",
                        mime="text/markdown"
                    )
                os.remove(temp_file_name)  # Clean up the downloaded file

if __name__ == "__main__":
    main()
