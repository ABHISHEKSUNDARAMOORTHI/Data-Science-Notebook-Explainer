import nbformat
import os

def create_fake_notebook(filename="test_notebook.ipynb"):
    """
    Generates a fake Jupyter notebook (.ipynb) file for testing purposes.
    The notebook simulates a basic data science workflow.

    Args:
        filename (str): The name of the .ipynb file to create.
    """
    # Create a new notebook object
    nb = nbformat.v4.new_notebook()

    # --- Cells for the Notebook ---

    # Cell 1: Markdown - Introduction
    nb.cells.append(nbformat.v4.new_markdown_cell(
        "# Data Analysis Project: Customer Churn Prediction\n\n"
        "This notebook outlines a simple machine learning pipeline to predict "
        "customer churn based on a hypothetical dataset. "
        "We'll cover data loading, preprocessing, model training, and evaluation."
    ))

    # Cell 2: Code - Data Loading & Initial Inspection
    nb.cells.append(nbformat.v4.new_code_cell(
        "import pandas as pd\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "import seaborn as sns\n\n"
        "print('Libraries imported successfully!')\n\n"
        "try:\n"
        "    # Simulate loading data\n"
        "    data = pd.DataFrame({\n"
        "        'CustomerID': range(1, 101),\n"
        "        'Age': np.random.randint(18, 65, 100),\n"
        "        'MonthlyCharges': np.random.uniform(20, 100, 100).round(2),\n"
        "        'TotalCharges': np.random.uniform(100, 5000, 100).round(2),\n"
        "        'Tenure': np.random.randint(1, 72, 100),\n"
        "        'Churn': np.random.choice([0, 1], 100, p=[0.7, 0.3])\n"
        "    })\n"
        "    print('Dummy data created.')\n"
        "    print(data.head())\n"
        "    print(data.info())\n"
        "except Exception as e:\n"
        "    print(f'Error loading data: {e}')"
    ))

    # Cell 3: Markdown - Data Preprocessing
    nb.cells.append(nbformat.v4.new_markdown_cell(
        "## Data Preprocessing and Feature Engineering\n\n"
        "We'll handle missing values, encode categorical features, "
        "and scale numerical features to prepare the data for modeling."
    ))

    # Cell 4: Code - Preprocessing Steps
    nb.cells.append(nbformat.v4.new_code_cell(
        "from sklearn.model_selection import train_test_split\n"
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n"
        "from sklearn.compose import ColumnTransformer\n"
        "from sklearn.pipeline import Pipeline\n\n"
        "numerical_features = ['Age', 'MonthlyCharges', 'TotalCharges', 'Tenure']\n"
        "categorical_features = [] # No explicit categorical features in dummy data for now\n\n"
        "preprocessor = ColumnTransformer(\n"
        "    transformers=[\n"
        "        ('num', StandardScaler(), numerical_features),\n"
        "        # ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)\n"
        "    ])\n\n"
        "X = data.drop('Churn', axis=1)._get_numeric_data() # Simplified for dummy data\n"
        "y = data['Churn']\n\n"
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\n"
        "X_train_processed = preprocessor.fit_transform(X_train)\n"
        "X_test_processed = preprocessor.transform(X_test)\n\n"
        "print('Data preprocessed and split into training and testing sets.')"
    ))

    # Cell 5: Markdown - Model Training
    nb.cells.append(nbformat.v4.new_markdown_cell(
        "## Model Training and Evaluation\n\n"
        "A RandomForestClassifier will be trained on the preprocessed data, "
        "and its performance will be evaluated using accuracy and a confusion matrix."
    ))

    # Cell 6: Code - Model Training and Evaluation
    nb.cells.append(nbformat.v4.new_code_cell(
        "from sklearn.ensemble import RandomForestClassifier\n"
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n\n"
        "model = RandomForestClassifier(n_estimators=100, random_state=42)\n"
        "model.fit(X_train_processed, y_train)\n\n"
        "y_pred = model.predict(X_test_processed)\n\n"
        "accuracy = accuracy_score(y_test, y_pred)\n"
        "report = classification_report(y_test, y_pred)\n"
        "conf_matrix = confusion_matrix(y_test, y_pred)\n\n"
        "print(f'Model Accuracy: {accuracy:.4f}')\n"
        "print('\\nClassification Report:\\n', report)\n"
        "print('\\nConfusion Matrix:\\n', conf_matrix)\n\n"
        "plt.figure(figsize=(6,4))\n"
        "sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')\n"
        "plt.title('Confusion Matrix')\n"
        "plt.ylabel('True Label')\n"
        "plt.xlabel('Predicted Label')\n"
        "plt.show()"
    ))

    # Cell 7: Markdown - Conclusion
    nb.cells.append(nbformat.v4.new_markdown_cell(
        "## Conclusion\n\n"
        "This notebook successfully demonstrated a basic churn prediction pipeline. "
        "Further improvements could include more advanced feature engineering, "
        "hyperparameter tuning, and exploring different model architectures."
    ))

    # Write the notebook to a file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"Successfully created fake notebook: {filename}")
        print("You can now upload this file to your Streamlit app for testing.")
    except Exception as e:
        print(f"Error creating notebook file: {e}")

if __name__ == "__main__":
    create_fake_notebook()