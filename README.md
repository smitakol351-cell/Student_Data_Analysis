📊 Student Performance Analysis Dashboard

This project is an interactive dashboard built with Streamlit
 to analyze student performance data.
It allows users to filter, explore, and visualize student scores in Math, Reading, and Writing, with simple insights and visual analytics.

🚀 Features

✅ Interactive Filters – Filter students by Gender and Race/Ethnicity.

✅ Quick Statistics – View average Math, Reading, and Writing scores.

✅ Data Overview – Explore the filtered dataset in a scrollable table.

✅ Analytics Dashboard – Generate interactive charts and visualizations.

✅ User-Friendly UI – Clean layout with tabs for better navigation.

📂 Project Structure
├── data/
│   └── raw.csv              # Raw dataset (student scores)
├── src/
│   ├── data_loader2.py      # Data loading logic
│   ├── dashboard.py         # Dashboard (charts & plots)
├── main.py                  # Streamlit app entry point

🛠️ Tech Stack

Python 🐍

Streamlit – UI & Dashboard
Pandas – Data handling

Matplotlib / Seaborn (optional) – Visualizations

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/student-performance-dashboard.git
cd student-performance-dashboard


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run main.py
