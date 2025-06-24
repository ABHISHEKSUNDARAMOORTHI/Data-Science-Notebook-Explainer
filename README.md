
# 📚 Data Science Notebook Explainer

The **Data Science Notebook Explainer** is an innovative AI-powered web application built with Streamlit that demystifies Jupyter and Google Colab notebooks. Have you ever inherited a notebook filled with complex code and undocumented steps? This tool is designed to solve exactly that problem\!

Simply upload your `.ipynb` file, and our intelligent system will analyze its content, providing a clear, structured, and cell-by-cell explanation of the code, its purpose, and the overall data science workflow. Get instant insights into data loading, preprocessing, model training, visualization, and more, all without manually sifting through lines of code.

This project is perfect for data scientists, analysts, students, and anyone who needs to quickly understand or onboard onto new data science projects.

-----

## 🚀 Features

  * **Intelligent Notebook Analysis:** Leverages Google Gemini's AI capabilities to understand the context and purpose of each notebook cell.
  * **Cell-by-Cell Explanations:** Provides detailed breakdowns of both **code** and **markdown** cells.
  * **Workflow Summaries:** Generates an overall summary of the notebook's objectives and the steps it performs.
  * **Multiple Output Formats:** Download explanations as **Markdown** (`.md`) or formatted **HTML** (`.html`) files.
  * **User-Friendly Interface:** Built with Streamlit for a clean, intuitive, and interactive web experience.
  * **Drag-and-Drop Support:** Easily upload your `.ipynb` files by dragging them directly into the app.
  * **Responsive Design:** Optimized for a seamless experience across various devices (desktops, tablets, mobiles) with a modern, dark-themed UI.

-----

## 🛠️ Technologies Used

  * **Streamlit:** For building the interactive web application.
  * **Google Gemini API:** The core AI model providing intelligent explanations.
  * **`nbformat`:** For parsing and understanding Jupyter Notebook structure.
  * **`python-dotenv`:** For securely managing API keys.
  * **`markdown`:** For converting markdown to HTML output.
  * **Custom CSS:** For a sleek, professional, and dark-themed user interface with custom fonts (Inter) and icons (Font Awesome).

-----

## 💻 Project Structure

The project is modularized into several Python files for better organization and maintainability:

```
.
├── .env                  # Environment variables (e.g., GOOGLE_API_KEY)
├── .streamlit/           # Streamlit configuration (optional, for global settings)
│   └── config.toml       # Streamlit specific configurations
├── ai_logic.py           # Handles interactions with the Google Gemini API and core AI logic.
├── features.py           # Contains functions for file handling, output generation, and integration with AI logic.
├── styling.py            # Manages all custom CSS for the Streamlit application's look and feel.
├── main.py               # The main Streamlit application file, bringing all components together.
├── generate_fake_notebook.py # Utility script to create a dummy notebook for testing.
└── README.md             # This file.
```

-----

## ⚡ Getting Started

Follow these steps to set up and run the Data Science Notebook Explainer locally.

### Prerequisites

  * Python 3.9+ installed
  * `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/data-science-notebook-explainer.git
    cd data-science-notebook-explainer
    ```

    *(Replace `yourusername` with your actual GitHub username if you fork it.)*

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

      * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
      * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *(If `requirements.txt` doesn't exist, you'll need to create it first by running `pip freeze > requirements.txt` after installing all dependencies, or manually install: `pip install streamlit nbformat google-generativeai python-dotenv markdown`)*

### API Key Setup

1.  **Obtain a Google Gemini API Key:**

      * Go to the [Google AI Studio](https://aistudio.google.com/app/apikey) to generate your API key.

2.  **Create a `.env` file:**

      * In the root directory of the project, create a file named `.env`.
      * Add your API key to this file in the following format:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```
        *(Replace `"YOUR_API_KEY_HERE"` with the actual key you obtained.)*

### Running the Application

1.  **Start the Streamlit app:**
    Make sure your virtual environment is activated.

    ```bash
    streamlit run main.py
    ```

2.  **Access the app:**
    Your web browser should automatically open to the Streamlit application (usually `http://localhost:8501`).

-----

## 🧪 Testing

To test the application without needing a real `.ipynb` file immediately, you can generate a fake one:

1.  **Generate a dummy notebook:**

    ```bash
    python generate_fake_notebook.py
    ```

    This will create a `test_notebook.ipynb` file in your project's root directory.

2.  **Upload and test:**
    Now, run `streamlit run main.py` and upload the `test_notebook.ipynb` file to see the explainer in action.

-----

## 🤝 Contributing

Contributions are welcome\! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them (`git commit -m 'Add new feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

-----

