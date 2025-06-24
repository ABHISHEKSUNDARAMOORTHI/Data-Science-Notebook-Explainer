import os
from dotenv import load_dotenv
import google.generativeai as genai
import nbformat

# Load environment variables from .env file
load_dotenv()

# --- Configuration from .env ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-1.5-flash") # Default to gemini-1.5-flash

# --- LLM Client Initialization ---
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    raise ValueError("GOOGLE_API_KEY not found in .env. Please set your Gemini API key.")

# --- Core AI Logic Functions ---

def get_gemini_response(prompt: str, model_name: str = LLM_MODEL) -> str:
    """
    Sends a prompt to the Google Gemini LLM and returns the response.

    Args:
        prompt (str): The text prompt to send to the LLM.
        model_name (str): The name of the Gemini model to use (defaults to LLM_MODEL from .env).

    Returns:
        str: The generated text response from the LLM.
    """
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        
        # Check if the response contains parts and extract text
        if response.parts:
            return "".join([part.text for part in response.parts if hasattr(part, 'text')])
        elif hasattr(response, 'text'): # Fallback for simpler responses
            return response.text
        else:
            return "Error: Unexpected Gemini response structure or empty response."
    except Exception as e:
        # It's good practice to log the error for debugging in a real application
        print(f"Error communicating with Gemini LLM ({model_name}): {e}")
        return f"An error occurred while generating AI response: {e}"

def parse_notebook_content(notebook_file_path: str) -> list[dict]:
    """
    Reads a Jupyter or Colab notebook file and extracts cell content.

    Args:
        notebook_file_path (str): The path to the .ipynb notebook file.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary represents a cell
                    and contains 'type' (e.g., 'code', 'markdown') and 'content'.
                    Returns an empty list if the file is not found or parsing fails.
    """
    try:
        with open(notebook_file_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        cells = []
        for cell in nb.cells:
            if cell.cell_type == 'code':
                cells.append({'type': 'code', 'content': cell.source})
            elif cell.cell_type == 'markdown':
                cells.append({'type': 'markdown', 'content': cell.source})
            # You could extend this to handle other cell types like 'raw' if needed
        return cells
    except FileNotFoundError:
        print(f"Error: Notebook file not found at '{notebook_file_path}'")
        return []
    except Exception as e:
        print(f"Error parsing notebook '{notebook_file_path}': {e}")
        return []

def generate_notebook_summary(notebook_cells: list[dict]) -> str:
    """
    Iterates through parsed notebook cells, prompts the LLM for explanations,
    and constructs a structured summary including an overall workflow overview.

    Args:
        notebook_cells (list[dict]): A list of cell dictionaries obtained from parse_notebook_content.

    Returns:
        str: A comprehensive markdown string summarizing the notebook.
    """
    if not notebook_cells:
        return "No content found in the notebook to summarize."

    cell_summaries = []
    
    # Generate summary for each cell
    for i, cell in enumerate(notebook_cells):
        cell_number = i + 1
        if cell['type'] == 'code':
            prompt = f"""As a data science assistant, explain the following Python code block from a Jupyter/Colab notebook.
            Focus on its purpose, what it accomplishes within a data science workflow (e.g., data loading, preprocessing, model training, visualization), and any key libraries or functions used.
            Keep the explanation concise and directly relevant to the code provided.

            Code Block {cell_number}:
            ```python
            {cell['content']}
            ```
            """
            explanation = get_gemini_response(prompt)
            cell_summaries.append(f"● **Cell {cell_number} (Code):** {explanation.strip()}")
        elif cell['type'] == 'markdown':
            # For markdown, we can either summarize it with the LLM or just extract the key lines.
            # For simplicity and efficiency, let's extract the first few lines to indicate its content.
            # If markdown cells are very long and complex, you might consider prompting the LLM for a summary.
            first_lines = cell['content'].split('\n')[:2]
            preview = ' '.join(first_lines).strip()
            if len(cell['content'].split('\n')) > 2:
                preview += "..." # Indicate more content
            cell_summaries.append(f"● **Cell {cell_number} (Markdown):** Documentation/Explanation. Preview: \"{preview}\"")

    # Generate overall workflow summary
    overall_workflow_prompt = """
    Based on the following cell-by-cell explanations from a data science notebook,
    provide a high-level overview of the entire notebook's workflow, its primary goal,
    and the main steps involved. Summarize the flow logically.

    Cell Explanations:
    """ + "\n".join(cell_summaries)

    overall_summary_text = get_gemini_response(overall_workflow_prompt)
    
    # Combine into final structured output
    final_output = "## Notebook Overview:\n"
    final_output += overall_summary_text.strip() + "\n\n"
    final_output += "## Cell-by-Cell Summary:\n"
    final_output += "\n".join(cell_summaries)

    return final_output

# Example of how you might use these functions (for testing AI logic in isolation)
if __name__ == "__main__":
    # Create a dummy notebook for testing
    dummy_notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "source": "# Project Introduction\nThis notebook demonstrates a machine learning pipeline from data loading to model evaluation."
            },
            {
                "cell_type": "code",
                "source": "import pandas as pd\nimport numpy as np\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score\n\nprint('Libraries imported successfully.')"
            },
            {
                "cell_type": "code",
                "source": "data = pd.read_csv('dummy_data.csv')\nX = data[['feature1', 'feature2']]\ny = data['target']\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n\nprint('Data loaded and split.')"
            },
            {
                "cell_type": "markdown",
                "source": "## Model Training\nHere, a RandomForestClassifier is trained on the preprocessed data."
            },
            {
                "cell_type": "code",
                "source": "model = RandomForestClassifier(n_estimators=100, random_state=42)\nmodel.fit(X_train, y_train)\n\npredictions = model.predict(X_test)\naccuracy = accuracy_score(y_test, predictions)\nprint(f'Model Accuracy: {accuracy:.2f}')"
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.9.7"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    dummy_notebook_path = "temp_dummy_notebook.ipynb"
    with open(dummy_notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nbformat.from_dict(dummy_notebook_content), f)
    print(f"Created dummy notebook for testing: {dummy_notebook_path}")

    try:
        print(f"\nAnalyzing notebook: {dummy_notebook_path} using Gemini model: {LLM_MODEL}")
        parsed_cells = parse_notebook_content(dummy_notebook_path)
        if parsed_cells:
            full_explanation = generate_notebook_summary(parsed_cells)
            print("\n" + "="*50)
            print("GENERATED NOTEBOOK EXPLANATION:")
            print("="*50)
            print(full_explanation)
            
            # For testing, save the output
            with open("ai_logic_test_output.md", "w", encoding="utf-8") as f:
                f.write(full_explanation)
            print("\nTest output saved to ai_logic_test_output.md")
        else:
            print("No cells parsed from the dummy notebook.")

    finally:
        # Clean up the dummy notebook
        if os.path.exists(dummy_notebook_path):
            os.remove(dummy_notebook_path)
            print(f"\nCleaned up dummy notebook: {dummy_notebook_path}")