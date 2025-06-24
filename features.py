import os
import nbformat
import base64 # For generating download links
from io import StringIO, BytesIO
from ai_logic import generate_notebook_summary, parse_notebook_content
import markdown # Will need to 'pip install markdown' for HTML conversion

def save_and_get_summary(uploaded_file, output_format: str = "markdown") -> tuple[str, str | None, bool, str | None]:
    """
    Handles an uploaded .ipynb file, parses it, generates a summary using AI logic,
    and returns the summary text along with a downloadable link, a success status,
    and an error message if applicable.

    Args:
        uploaded_file (streamlit.runtime.uploaded_file_manager.UploadedFile):
            The file object uploaded via Streamlit's st.file_uploader.
        output_format (str): The desired output format ('markdown' or 'html').

    Returns:
        tuple[str, str | None, bool, str | None]: A tuple containing:
            - The generated summary text (Markdown format) if successful, otherwise an empty string.
            - A base64 encoded download link for the generated summary file (str) or None.
            - A boolean indicating if the operation was successful (True/False).
            - An error message (str) if the operation failed, otherwise None.
    """
    if uploaded_file is None:
        return "", None, False, "Please upload a .ipynb file to get started."

    temp_notebook_path = None # Initialize to None for finally block
    try:
        # Read the content of the uploaded .ipynb file
        notebook_content = uploaded_file.read().decode("utf-8")
        
        # Save the uploaded content to a temporary file for nbformat to read
        temp_notebook_path = f"temp_{os.path.basename(uploaded_file.name)}" # Use basename to avoid path issues
        with open(temp_notebook_path, "w", encoding="utf-8") as f:
            f.write(notebook_content)

        # Parse the notebook using the function from ai_logic
        cells = parse_notebook_content(temp_notebook_path)
        
        if not cells:
            return "", None, False, "Could not parse the uploaded notebook. It might be empty or corrupted."

        # Generate the summary using the AI logic
        summary_text = generate_notebook_summary(cells)

        # Prepare the file for download based on output_format
        download_filename_prefix = uploaded_file.name.replace(".ipynb", "")
        download_link = None
        mime_type = None
        output_content = summary_text

        if output_format == "markdown":
            download_filename = f"{download_filename_prefix}_explanation.md"
            encoded_content = base64.b64encode(output_content.encode("utf-8")).decode()
            mime_type = "text/markdown"
            download_link = f'data:{mime_type};base64,{encoded_content}'
        elif output_format == "html":
            # Convert markdown summary to HTML
            html_summary = markdown.markdown(output_content, extensions=['fenced_code', 'tables', 'nl2br'])
            # Add basic HTML structure for a standalone file
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Notebook Explanation - {download_filename_prefix}</title>
                <style>
                    body {{ font-family: 'Inter', sans-serif; line-height: 1.6; margin: 20px; color: #333; }}
                    h1, h2, h3 {{ font-family: 'Inter', sans-serif; color: #2E86C1; }}
                    h2 {{ border-bottom: 1px solid #eee; padding-bottom: 5px; margin-top: 30px; }}
                    pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
                    code {{ background-color: #f9f9f9; padding: 2px 4px; border-radius: 3px; font-family: monospace; }}
                    ul {{ list-style-type: none; padding-left: 0; }}
                    ul li:before {{ content: "• "; color: #2E86C1; font-weight: bold; display: inline-block; width: 1em; margin-left: -1em; }}
                </style>
            </head>
            <body>
                {html_summary}
            </body>
            </html>
            """
            download_filename = f"{download_filename_prefix}_explanation.html"
            encoded_content = base64.b64encode(html_content.encode("utf-8")).decode()
            mime_type = "text/html"
            download_link = f'data:{mime_type};base64,{encoded_content}'
        else:
            return summary_text, None, False, "Unsupported output format. Only Markdown and HTML are supported for download."

        return summary_text, download_link, True, None # Success!

    except Exception as e:
        return "", None, False, f"An unexpected error occurred: {e}"
    finally:
        # Ensure temporary file is removed even if an error occurs
        if temp_notebook_path and os.path.exists(temp_notebook_path):
            os.remove(temp_notebook_path)

# --- Main guard for testing features.py in isolation ---
if __name__ == "__main__":
    print("This file contains features for the Streamlit app. Run main.py to test.")