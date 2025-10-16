import streamlit as st

st.set_page_config(
    page_title="Genetic Algorithm"
)

st.header("Genetic Algorithm", divider="gray")

import streamlit as st
import pandas as pd
import plotly.express as px

# Set the URL for the CSV file
csv_url = 'https://raw.githubusercontent.com/ainagif/aina44/refs/heads/main/arts_faculty_data.csv'

# --- Data Loading ---
st.header("Arts Faculty Data Analysis")

try:
    # Load the data into a Pandas DataFrame
    arts_df = pd.read_csv(csv_url)
    st.success("Data loaded successfully!")

    import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np # Used here to create a dummy DataFrame for the example

# --- Dummy Data Creation (Replace this with your actual DataFrame loading) ---
# This part simulates loading your 'arts_df' with a 'Timestamp' column
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-03-31')
date_range = pd.date_range(start=start_date, end=end_date, periods=1000)
arts_df = pd.DataFrame({'Timestamp': date_range})
# ----------------------------------------------------------------------------


st.title('Response Count Analysis')

# 1. Convert 'Timestamp' to datetime objects (Good practice, even if data is already datetime)
arts_df['Timestamp'] = pd.to_datetime(arts_df['Timestamp'])

# 2. Set 'Timestamp' as index and resample to count responses per day
daily_counts = arts_df.set_index('Timestamp').resample('D').size()

# 3. Create the Matplotlib plot
# Use 'plt.figure()' to create a fresh figure, which is recommended for Streamlit
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the daily counts onto the figure's axes (ax)
daily_counts.plot(kind='line', ax=ax)

# Set title and labels using the axes object
ax.set_title('Number of Responses Over Time (Daily)')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Responses')
ax.grid(True)

# 4. Display the plot using Streamlit's pyplot function
st.pyplot(fig)

    # Display the head of the DataFrame in Streamlit
    st.subheader("Data Preview (First 5 Rows)")
    st.dataframe(arts_df.head())

    # --- Plotly Pie Chart Generation ---
    st.subheader("Distribution of Gender in Arts Faculty (Plotly)")

    # Calculate the value counts for the 'Gender' column
    gender_counts = arts_df['Gender'].value_counts().reset_index()
    # Rename columns for clarity in Plotly
    gender_counts.columns = ['Gender', 'Count']

    # Create the Plotly Pie Chart
    # plotly.express is often the simplest way to create common charts
    fig = px.pie(
        gender_counts,
        values='Count',
        names='Gender',
        title='Distribution of Gender in Arts Faculty',
        hole=0.3, # Optional: makes it a donut chart
        color_discrete_sequence=px.colors.qualitative.Set1 # Optional: sets a color scheme
    )

    # Optional: Update layout for better appearance
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"An error occurred while loading or processing data: {e}")

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
# Assuming 'arts_df' and the 'Arts Program' column are already loaded/defined

# 1. Get the value counts
# Replace 'arts_df' with your actual DataFrame variable if different
# Example placeholder for 'arts_df' - YOU MUST replace this with your actual data loading
data = {'Arts Program': ['Music', 'Visual Arts', 'Theater', 'Music', 'Visual Arts', 'Dance', 'Music', 'Theater']}
arts_df = pd.DataFrame(data) 

program_counts = arts_df['Arts Program'].value_counts()

# 2. Create the matplotlib figure
fig, ax = plt.subplots(figsize=(10, 6)) # Create figure and axes explicitly
program_counts.plot(kind='bar', ax=ax) # Plot onto the defined axes

# 3. Add labels and titles using the axes object
ax.set_title('Distribution of Arts Programs')
ax.set_xlabel('Arts Program')
ax.set_ylabel('Count')
plt.xticks(rotation=45, ha='right') # Rotate labels for readability
plt.tight_layout() # Adjust layout to prevent labels overlapping

# 4. Display the figure in Streamlit
st.pyplot(fig)
