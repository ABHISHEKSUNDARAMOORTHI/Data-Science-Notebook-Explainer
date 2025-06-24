import streamlit as st
from ai_logic import GOOGLE_API_KEY # Just to check if API key is loaded
from styling import apply_custom_styles
from features import save_and_get_summary
import os

def main():
    """
    Main function to run the Streamlit application for the Data Science Notebook Explainer.
    """
    # 1. Set Streamlit Page Configuration
    st.set_page_config(
        page_title="Data Science Notebook Explainer",
        page_icon="📚",
        layout="wide", # Use a wide layout for better content display
        initial_sidebar_state="expanded" # Keep sidebar expanded by default
    )

    # 2. Apply Custom Styles (from styling.py)
    apply_custom_styles()

    # --- Header Section ---
    st.title("Data Science Notebook Explainer 📝")
    st.markdown("""
        Unlock the secrets of your Jupyter or Colab notebooks! This AI-powered assistant
        analyzes your `.ipynb` files and generates clear, structured explanations of each
        code block, its purpose, and the overall workflow.
        
        **Simply upload your notebook and let the AI do the heavy lifting!**
    """)

    # --- API Key Check (Optional but good for debugging) ---
    if not GOOGLE_API_KEY:
        st.error("🚨 Google Gemini API Key is not set! Please add `GOOGLE_API_KEY=\"YOUR_API_KEY\"` to your `.env` file.")
        st.stop() # Stop the app if API key is missing

    # --- Sidebar for File Upload and Options ---
    st.sidebar.header("Upload Your Notebook")
    uploaded_file = st.sidebar.file_uploader(
        "Choose a `.ipynb` file",
        type="ipynb",
        help="Upload your Jupyter or Google Colab notebook file here."
    )

    st.sidebar.header("Output Options")
    output_format = st.sidebar.radio(
        "Select Output Format:",
        ("Markdown", "HTML"),
        help="Choose the format for the downloadable explanation."
    ).lower() # Convert to lowercase for internal use

    process_button = st.sidebar.button("Generate Explanation", use_container_width=True)

    # --- Main Content Area ---
    st.markdown("---") # Visual separator

    if uploaded_file is not None and process_button:
        with st.spinner("Analyzing your notebook and generating explanation... This might take a moment."):
            # Call the main feature function to process the file and get summary/link
            summary_text, download_link, success, error_message = save_and_get_summary(uploaded_file, output_format)

            if success:
                st.success("Explanation Generated Successfully!")
                
                # Display the explanation
                st.subheader("Generated Notebook Explanation")
                # Using st.markdown to render the generated Markdown text
                st.markdown(summary_text)

                st.markdown("---")
                st.subheader("Download Your Explanation")
                # Create a download button based on the generated link and format
                st.download_button(
                    label=f"Download {output_format.upper()} Explanation",
                    data=download_link,
                    file_name=uploaded_file.name.replace(".ipynb", f"_explanation.{output_format}"),
                    mime=f"text/{output_format}",
                    key="download_button",
                    help=f"Click to download the notebook explanation as a .{output_format} file."
                )
                
            else:
                st.error(f"Failed to generate explanation: {error_message}")
                if "API key" in error_message or "authentication" in error_message: # More robust check for API errors
                    st.warning("Ensure your Google Gemini API key is correctly set in the `.env` file and has sufficient permissions.")

    elif uploaded_file is None and process_button:
        st.warning("Please upload a `.ipynb` file first before clicking 'Generate Explanation'.")
        
    elif uploaded_file is None:
        st.info("Upload a notebook file on the left sidebar and click 'Generate Explanation' to begin.")
        # Use the Unsplash image (ensure URL is valid or replace with a local asset)
        st.image("https://images.unsplash.com/photo-1596495632007-9b43d3b7f141?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w1NjY1OTR8MHwxfHNlYXJjaHw0OXx8ZGF0YSUyMHNjaWVuY2V8ZW58MHx8fHwxNzE5MTUyNDQ2fDA&ixlib=rb-4.0.3&q=80&w=1080",
                 caption="Visualize your data science journey with AI explanations",
                 use_column_width=True)


    # --- Footer ---
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; font-size: small; color: var(--text-medium);">
            Developed with ❤️ by Your Name/Organization. Powered by Google Gemini and Streamlit.
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()