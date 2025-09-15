import streamlit as st
from src.data_loader2 import data_load
from src.dashboard import create_dashboard
# Page Configuration
st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="📊",
    layout="wide"
)
# Load Data
df = data_load("data/raw.csv")
# Sidebar Filters
st.sidebar.header("⚙️ Filters")

# Gender filter
gender_options = df["gender"].unique()
selected_gender = st.sidebar.multiselect(
    "Filter by Gender",
    options=gender_options,
    default=gender_options
)

# Race/Ethnicity filter (if available)
if "race_ethnicity" in df.columns:
    race_options = df["race_ethnicity"].unique()
    selected_race = st.sidebar.multiselect("Filter by Race/Ethnicity",options=race_options,default=race_options)
else:
    selected_race = None
 # Apply filters
df_filtered = df[df["gender"].isin(selected_gender)]

if selected_race is not None:
    df_filtered = df_filtered[df_filtered["race_ethnicity"].isin(selected_race)]
# Main Title
st.title("📊 Student Performance Analysis Dashboard")
st.markdown(
    """
    Welcome to the **Student Performance Analysis Dashboard**.  
    Use the sidebar filters to refine the dataset and explore insights 
    tailored to your selection.
    """
)
# Tabs
tab1, tab2 = st.tabs(["📋 Data Overview", "📈 Analytics Dashboard"])
# Tab 1: Data Overview
with tab1:
    st.header("📋 Student Performance Data")
    st.markdown("Explore the filtered dataset below with summary statistics.")

    # Summary Metrics
    st.subheader("🔍 Quick Statistics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", f"{len(df_filtered):,}")
    col2.metric("Average Math Score", f"{df_filtered['math_score'].mean():.1f}")
    col3.metric("Average Reading Score", f"{df_filtered['reading_score'].mean():.1f}")
    col4.metric("Average Writing Score", f"{df_filtered['writing_score'].mean():.1f}")

    # Data Table
    st.subheader("📊 Data Table")
    st.dataframe(df_filtered, use_container_width=True)
# Tab 2: Analytics Dashboard
with tab2:
    st.header("📈 Analytics Dashboard")
    st.markdown("Interactive visualizations based on your selected filters.")

    # Dashboard builder
    create_dashboard(df_filtered)
