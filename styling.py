# styling.py
import streamlit as st

def apply_custom_styles():
    """
    Applies comprehensive custom CSS styles to the Streamlit application
    for a modern, professional, dark-themed look inspired by GitHub's aesthetic.
    """
    st.markdown("""
    <style>
        /* Import Inter font from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
        /* Import Font Awesome for Icons */
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

        /* Color Variables for a Brighter, Professional Palette */
        :root {
            --bg-primary: #0D1117; /* Very Dark Grey/Blue (like GitHub dark) */
            --bg-secondary: #161B22; /* Slightly Lighter Dark Grey/Blue (Card/Header) */
            --text-light: #C9D1D9; /* Light Gray Text */
            --text-medium: #8B949E; /* Medium Gray Text */

            --accent-blue-light: #58A6FF; /* Vibrant Blue */
            --accent-blue-dark: #1F6FD8; /* Darker Blue */

            --success-color: #3FB950; /* Green */
            --danger-color: #F85149; /* Red */
            --warning-color: #DD9F1B; /* Orange/Amber */
            --info-color: #79C0FF; /* Lighter Blue */

            --border-color: #30363D; /* Darker Gray for Borders */
            --shadow-light: rgba(0, 0, 0, 0.2);
            --shadow-medium: rgba(0, 0, 0, 0.4);
            --border-radius-lg: 12px;
            --border-radius-md: 8px;
            --border-radius-sm: 4px;
        }

        /* General Body & Typography */
        html, body {
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: var(--text-light);
            background-color: var(--bg-primary);
        }

        /* Streamlit App Overrides */
        .stApp {
            background-color: var(--bg-primary);
            color: var(--text-light);
        }

        /* Main Content Container */
        .main .block-container {
            max-width: 1200px;
            padding: 2.5rem 3rem;
            background-color: var(--bg-secondary);
            border-radius: var(--border-radius-lg);
            box-shadow: 0 10px 25px var(--shadow-medium);
            margin: 3rem auto;
            border: 1px solid var(--border-color);
        }

        /* Adjust global app padding (prevents stretching to edges) */
        .stApp > header {
            background-color: transparent; /* Makes header transparent */
        }
        .css-1dp5vir { /* Targets the main content wrapper padding (adjust as needed for Streamlit versions) */
            padding-left: 1rem;
            padding-right: 1rem;
        }

        /* Section Headers */
        .stMarkdown h1, .stMarkdown h2 {
            font-size: 2.2rem;
            color: var(--accent-blue-light);
            margin-top: 2.5rem;
            margin-bottom: 1.8rem;
            border-bottom: 2px solid var(--accent-blue-light);
            padding-bottom: 0.8rem;
            font-weight: 700;
            position: relative;
        }
        .stMarkdown h1::after, .stMarkdown h2::after {
            content: '';
            display: block;
            width: 70px;
            height: 5px;
            background: linear-gradient(90deg, var(--accent-blue-light), transparent);
            position: absolute;
            bottom: -2px;
            left: 0;
            border-radius: var(--border-radius-sm);
        }

        .stMarkdown h3 {
            font-size: 1.8rem;
            color: var(--accent-blue-light);
            margin-top: 2rem;
            margin-bottom: 1.2rem;
            border-bottom: 1px dashed var(--border-color);
            padding-bottom: 0.6rem;
            font-weight: 600;
        }
        .stMarkdown h4 {
            font-size: 1.4rem;
            color: var(--accent-blue-dark);
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            font-weight: 600;
        }

        /* Textareas and Input Fields */
        textarea, .stTextInput > div > div > input, .stCodeEditor, .stSelectbox > div > div, .stFileUploader > div > div {
            background-color: var(--bg-primary); /* Darker background for inputs */
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            color: var(--text-light);
            font-size: 1.05rem;
            padding: 12px 18px;
            box-shadow: inset 0 2px 5px var(--shadow-light);
            transition: all 0.3s ease;
        }
        textarea:focus, .stTextInput > div > div > input:focus, .stCodeEditor:focus-within, .stSelectbox > div > div:focus-within, .stFileUploader > div > div:focus-within {
            border-color: var(--accent-blue-light);
            box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.3), inset 0 2px 5px var(--shadow-light); /* Softer blue shadow */
            outline: none;
        }
        textarea::placeholder {
            color: var(--text-medium);
            opacity: 0.6;
        }

        /* Buttons */
        .stButton > button {
            padding: 1rem 2rem;
            border: none;
            border-radius: var(--border-radius-md);
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 1.8rem;
            box-shadow: 0 8px 15px var(--shadow-medium);
            letter-spacing: 0.03em;
            display: inline-flex; /* For icon alignment */
            align-items: center;
            justify-content: center;
        }
        .stButton > button:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 20px var(--shadow-medium);
        }
        .stButton > button:active {
            transform: translateY(0);
            box-shadow: 0 4px 8px var(--shadow-light);
        }

        .stButton > button { /* Default button styling */
            background: linear-gradient(45deg, var(--accent-blue-dark), var(--accent-blue-light));
            color: #ffffff;
            border: 1px solid var(--accent-blue-light);
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, #3182ce, var(--accent-blue-light));
        }

        /* Specific styling for download button if needed (e.g. secondary style) */
        /* You might use st.button(key="download_button", type="secondary") in main.py */
        .stButton > button[kind="secondary"] {
            background-color: var(--bg-primary);
            color: var(--accent-blue-light);
            border: 2px solid var(--accent-blue-dark);
            box-shadow: none; /* Remove shadow for secondary button */
        }
        .stButton > button[kind="secondary"]:hover {
            background-color: var(--accent-blue-dark);
            color: #ffffff;
            border-color: var(--accent-blue-dark);
            box-shadow: 0 4px 8px var(--shadow-light); /* Add subtle shadow on hover */
        }

        .stButton > button i {
            margin-right: 0.7rem;
            font-size: 1.2em;
        }

        /* Markdown output styling (for AI explanations) */
        .stMarkdown p, .stMarkdown ul, .stMarkdown ol, .stMarkdown li {
            color: var(--text-light);
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }
        .stMarkdown ul {
            list-style-type: '👉 '; /* Custom bullet point */
            margin-left: 30px;
            padding-left: 10px;
        }
        .stMarkdown ol {
            margin-left: 30px;
            padding-left: 10px;
        }
        .stMarkdown strong {
            color: var(--accent-blue-light);
            font-weight: 700;
        }
        .stMarkdown em {
            color: var(--text-medium);
            font-style: italic;
        }
        .stMarkdown code {
            background-color: #4a5568; /* Darker background for inline code */
            padding: 0.3em 0.5em;
            border-radius: var(--border-radius-sm);
            font-family: 'Fira Code', 'Cascadia Code', monospace; /* Good monospace fonts */
            font-size: 0.95em;
            color: #FFD700; /* Yellowish color for inline code */
        }
        .stMarkdown pre code {
            background-color: #0d1217; /* Very dark background for code blocks */
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            padding: 1.5em;
            overflow-x: auto;
            margin-bottom: 2rem;
            display: block;
            box-shadow: inset 0 0 10px var(--shadow-light);
            color: #ffffff;
            font-size: 1em;
            line-height: 1.5;
        }

        /* Alerts and Info Boxes */
        /* These classes often change with Streamlit updates. You might need to inspect your app. */
        .stAlert {
            border-radius: var(--border-radius-md);
            margin-top: 1.5rem;
            padding: 1.2rem 1.8rem;
            font-weight: 600;
            font-size: 1.05rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
        }
        .stAlert div[data-testid="stMarkdownContainer"] {
            margin-left: 10px; /* Space for icon */
        }
        /* Specific alert types - class names might vary */
        .stAlert.st-emotion-cache-1fcpknu { /* Success (e.g., st.success) */
            border-left: 8px solid var(--success-color) !important;
            background-color: rgba(63, 185, 80, 0.15) !important;
            color: var(--success-color) !important;
        }
        .stAlert.st-emotion-cache-1wdd6qg { /* Warning (e.g., st.warning) */
            border-left: 8px solid var(--warning-color) !important;
            background-color: rgba(221, 159, 27, 0.15) !important;
            color: var(--warning-color) !important;
        }
        .stAlert.st-emotion-cache-1215i5j { /* Error (e.g., st.error) */
            border-left: 8px solid var(--danger-color) !important;
            background-color: rgba(248, 81, 73, 0.15) !important;
            color: var(--danger-color) !important;
        }
        .stAlert.st-emotion-cache-19t5331 { /* Info (e.g., st.info) */
            border-left: 8px solid var(--info-color) !important;
            background-color: rgba(121, 192, 255, 0.15) !important;
            color: var(--info-color) !important;
        }


        /* Expander Styling */
        .streamlit-expanderHeader {
            background-color: var(--border-color);
            color: var(--text-light);
            font-weight: 600;
            border-radius: var(--border-radius-md);
            padding: 1rem 1.5rem;
            margin-bottom: 1rem;
            transition: background-color 0.3s ease;
            box-shadow: 0 3px 8px var(--shadow-light);
            font-size: 1.1rem;
            display: flex;
            align-items: center;
        }
        .streamlit-expanderHeader:hover {
            background-color: #5b6980; /* Slightly lighter on hover */
        }
        .streamlit-expanderContent {
            background-color: var(--bg-primary); /* Inner content background */
            border: 1px solid var(--border-color);
            border-top: none; /* No top border, connects to header */
            border-radius: 0 0 var(--border-radius-md) var(--border-radius-md);
            padding: 1.8rem;
            box-shadow: inset 0 0 10px var(--shadow-light);
        }

        /* Horizontal rule */
        hr {
            border-top: 1px solid var(--border-color);
            margin: 3.5rem 0;
            opacity: 0.6;
        }

        /* Custom Metric Card (for potential future use, e.g., showing cost KPIs) */
        .custom-metric-card {
            background-color: var(--bg-secondary);
            border-radius: var(--border-radius-md);
            padding: 1.5rem;
            box-shadow: 0 6px 15px var(--shadow-medium);
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 140px;
            border: 1px solid var(--border-color);
            height: 100%;
        }
        .custom-metric-card:hover {
            transform: translateY(-7px);
            box-shadow: 0 10px 25px var(--shadow-medium);
        }

        .custom-metric-value {
            font-size: 3.2em;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 0.3rem;
            color: var(--accent-blue-light);
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }

        .custom-metric-label {
            font-size: 1.1em;
            color: var(--text-medium);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.5rem;
        }
        .custom-metric-label i {
            margin-right: 0.8rem;
            color: var(--accent-blue-dark);
        }

        /* Sidebar specific styling */
        section[data-testid="stSidebar"] {
            background-color: var(--bg-secondary); /* Match main content card background */
            border-right: 1px solid var(--border-color);
            box-shadow: 2px 0px 5px var(--shadow-medium);
            padding-top: 2rem;
            color: var(--text-light);
        }
        section[data-testid="stSidebar"] .st-emotion-cache-vk33gh { /* Target the inner sidebar content */
            padding-top: 0rem; /* Reset default padding if any */
        }
        section[data-testid="stSidebar"] h2 {
            color: var(--accent-blue-light);
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 20px;
            margin-top: 0; /* Align top */
        }
        section[data-testid="stSidebar"] label {
            color: var(--text-light);
            font-weight: 600;
            font-size: 1.05rem;
            margin-bottom: 0.5rem;
        }
        /* Style for the file uploader label in sidebar */
        section[data-testid="stSidebar"] .stFileUploader label {
            font-size: 1.1em;
            font-weight: 600;
            color: var(--text-light);
            margin-bottom: 10px;
        }
        /* Style for the file uploader button in sidebar */
        section[data-testid="stSidebar"] .stFileUploader button {
            background-color: var(--accent-blue-dark);
            color: white;
            border-radius: var(--border-radius-md);
            padding: 8px 15px;
            font-size: 0.95em;
            font-weight: 500;
            transition: background-color 0.3s ease;
            border: none;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        section[data-testid="stSidebar"] .stFileUploader button:hover {
            background-color: var(--accent-blue-light);
        }


        /* Responsive Design */
        @media (max-width: 1024px) {
            .main .block-container {
                padding: 2rem 2.5rem;
            }
            .stMarkdown h1, .stMarkdown h2 {
                font-size: 1.9rem;
            }
            .stMarkdown h3 {
                font-size: 1.6rem;
            }
        }

        @media (max-width: 768px) {
            .main .block-container {
                padding: 1.5rem;
                margin: 1.5rem auto;
                width: 95%;
            }
            .stButton > button {
                display: block;
                width: 100%;
                margin: 0.8rem 0;
            }
            .stMarkdown h1, .stMarkdown h2 {
                font-size: 1.8rem;
            }
            .stMarkdown h3 {
                font-size: 1.4rem;
            }
            .stMarkdown h4 {
                font-size: 1.1rem;
            }
            textarea, .stTextInput > div > div > input, .stSelectbox > div > div {
                padding: 0.6rem 1rem;
                font-size: 0.95rem;
            }
            .stTabs [data-baseweb="tab-list"] button {
                padding: 0.8rem 1rem;
                font-size: 1rem;
            }
            .stMarkdown ul {
                margin-left: 15px;
            }
            /* Adjust sidebar for smaller screens */
            section[data-testid="stSidebar"] {
                padding: 1rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Example of how you might use this function in a test scenario
if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Styling Test Page")
    
    apply_custom_styles() # Apply the new styles

    st.title("Styling Showcase with Inter Font and Dark Theme")

    st.markdown("""
    This page demonstrates the new custom styling applied to the Streamlit application.
    It uses **Inter** as the primary font and implements a **dark theme** with a professional blue accent.
    """)

    st.sidebar.header("Sidebar Demo")
    st.sidebar.text_input("Sidebar Input", "Hello")
    st.sidebar.button("Sidebar Button")
    st.sidebar.file_uploader("Upload File (Sidebar)")


    st.header("Section Header Example")
    st.write("This is a paragraph of text with the new font and dark background.")

    st.subheader("Subheader for Content Organization")
    st.write("This section shows how subheaders are styled.")

    st.markdown("---") # Custom horizontal rule

    st.subheader("Interactive Elements")
    st.text_input("Enter your name:", "John Doe")
    st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])

    col1, col2 = st.columns(2)
    with col1:
        st.button("Primary Button 🚀")
    with col2:
        # To apply secondary button style, you'd use type="secondary" in main.py
        # For this demo, let's just show a normal button for now.
        st.download_button(label="Download Report ⬇️", data="dummy data", file_name="report.txt")
    
    st.markdown("---")

    st.subheader("Markdown Output Styles")
    st.markdown("""
    Here's an example of **markdown text** with `inline code` and a bulleted list:
    * This is the first item.
    * This is the second item.
    * This is the third item.

    And a numbered list:
    1.  First step.
    2.  Second step.
    3.  Third step.
    """)

    st.code("""
# This is a code block
def analyze_data(df):
    # Perform some analysis
    result = df.groupby('category').sum()
    return result

print("Code blocks are now styled with a dark background!")
    """, language="python")

    st.subheader("Alerts and Expanders")
    st.success("Success message! Your operation was completed.")
    st.warning("Warning! Something might need your attention.")
    st.error("Error! An unexpected issue occurred.")
    st.info("Info: Here's some helpful information for you.")

    with st.expander("Click to expand details"):
        st.write("This content is inside an expander, which also has custom styling.")
        st.markdown("You can put **any Streamlit content** here.")

    st.markdown("---")

    st.subheader("Custom Metric Card Example (For future use)")
    st.markdown("""
        <div class="custom-metric-card">
            <div class="custom-metric-value">1,234</div>
            <div class="custom-metric-label"><i class="fas fa-chart-line"></i> Total Explanations</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center; margin-top: 3rem; color: var(--text-medium); font-size: 0.9em;">
            Designed with 💜 using custom CSS and Streamlit.
        </div>
    """, unsafe_allow_html=True)