import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio

# Define a custom Plotly template
pio.templates["custom"] = {
    "layout": {
        "font": {"color": "black"},
        "legend": {
            "font": {"color": "black"},
            "bordercolor": "black",
            "borderwidth": 1
        },
        "xaxis": {
            "title_font": {"color": "black"},
            "tickfont": {"color": "black"}
        },
        "yaxis": {
            "title_font": {"color": "black"},
            "tickfont": {"color": "black"}
        }
    }
}

# Page configuration
st.set_page_config(
    page_title="Health Insurance Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for design adjustments
st.markdown("""
    <style>
    .main {background-color: #2F3035; padding: 20px;}
    .sidebar .sidebar-content {background-color: #2d2d2d; color: white;}
    .stTextInput, .stSelectbox, .stSlider {font-size: 18px;}
    .metric-container {display: flex; justify-content: space-around; margin-bottom: 20px;}
    .metric {background-color: rgba(128, 128, 128, 0.5); color: white; padding: 10px; border-radius: 10px; text-align: center;}
    .metric h3 {margin: 0; font-size: 18px; color: white;}
    .metric p {margin: 0; font-size: 24px; color: white;}
    header { visibility: hidden; }
    section { background-image: url('https://upload.wikimedia.org/wikipedia/commons/8/80/Backgorund.gif'); background-size: cover; }
    h1, h2 { text-align: center; color: white; }
    .stPlotlyChart {height: 400px; margin-bottom: 40px;} /* Increased margin-bottom for charts */
    </style>
    """, unsafe_allow_html=True)

# Load data from the CSV file
df = pd.read_csv('insurance.csv')

# Ensure numeric values are converted correctly
df['charges'] = pd.to_numeric(df['charges'], errors='coerce')
df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Remove non-numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])

# Dashboard title
st.title("Health Insurance Analysis")

# Key metrics
st.header("Key Metrics")
st.markdown("""
    <div class="metric-container">
        <div class="metric">
            <h3>Average Cost</h3>
            <p>${:,.2f}</p>
        </div>
        <div class="metric">
            <h3>Average BMI</h3>
            <p>{:.2f}</p>
        </div>
        <div class="metric">
            <h3>Average Age</h3>
            <p>{:.2f}</p>
        </div>
    </div>
    """.format(df['charges'].mean(), df['bmi'].mean(), df['age'].mean()), unsafe_allow_html=True)

# Grid layout for charts with extra space
col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="large")  # Adjust the gap parameter to increase spacing

with col1:
    # Correlation heatmap
    if not numeric_df.empty:
        correlation = numeric_df.corr()
        fig_corr = px.imshow(correlation, text_auto=True, color_continuous_scale='RdBu', origin='lower')
        fig_corr.update_layout(
            plot_bgcolor='white', 
            paper_bgcolor='white', 
            font=dict(color='black'),
            xaxis_title=None,
            yaxis_title=None,
            coloraxis_colorbar=dict(title="Correlation", tickfont=dict(color='black')),
            legend=dict(
                font=dict(color='black'),
                bordercolor='black',
                borderwidth=1
            ),
            title_text="Correlation Between Variables",
            title_x=0.5,
            title_xanchor='center',
            title_y=0.95,
            title_yanchor='top',
            margin=dict(t=50, b=0, l=0, r=0)  # Adjust margins to avoid external title
        )
        st.plotly_chart(fig_corr, use_container_width=True)

with col2:
    fig = px.scatter(df, x="age", y="charges", color="smoker", size="bmi", hover_name="region",
                     title="Insurance Cost by Age, BMI, and Smoking Status",
                     labels={"charges": "Costs", "age": "Age"},
                     template="custom", color_discrete_map={'yes': '#FF4B4B', 'no': '#4CAF50'})
    fig.update_layout(
        plot_bgcolor='white', 
        paper_bgcolor='white', 
        font=dict(color='black'),
        xaxis_title="Age",
        yaxis_title="Costs",
        legend_title_text="Smoking Status",
        legend=dict(
            font=dict(color='black'),
            bordercolor='black',
            borderwidth=1
        )
    )
    st.plotly_chart(fig, use_container_width=True)

with col3:
    smoker_mean = df[df['smoker'] == 'yes']['charges'].mean()
    non_smoker_mean = df[df['smoker'] == 'no']['charges'].mean()
    fig3 = go.Figure(data=[
        go.Bar(name='Smokers', x=['Smokers'], y=[smoker_mean], marker_color='#FF4B4B'),
        go.Bar(name='Non-Smokers', x=['Non-Smokers'], y=[non_smoker_mean], marker_color='#4CAF50')
    ])
    fig3.update_layout(
        barmode='group',
        title="Average Insurance Cost: Smokers vs Non-Smokers",
        xaxis_title="Category",
        yaxis_title="Average Cost",
        plot_bgcolor='white', 
        paper_bgcolor='white', 
        font=dict(color='black'),
        legend=dict(
            font=dict(color='black'),
            bordercolor='black',
            borderwidth=1
        )
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    region_filter = st.selectbox("Region", df['region'].unique())

    # Filter data only by region
    filtered_df = df[df['region'] == region_filter]

    fig2 = px.box(filtered_df, x="region", y="charges", color="smoker",
                  title=f"Insurance Cost by Region and Smoking Status ({region_filter})",
                  labels={"charges": "Costs", "region": "Region"}, template="custom",
                  color_discrete_map={'yes': '#FF4B4B', 'no': '#4CAF50'})
    fig2.update_layout(
        plot_bgcolor='white', 
        paper_bgcolor='white', 
        font=dict(color='black'),
        xaxis_title="Region",
        yaxis_title="Costs",
        legend_title_text="Smoking Status",
        legend=dict(
            font=dict(color='black'),
            bordercolor='black',
            borderwidth=1
        )
    )
    st.plotly_chart(fig2, use_container_width=True)

# Additional charts with extra spacing
st.write("")  # Add a blank line for spacing

fig4 = px.scatter(df, x="bmi", y="charges", color="age", size="age", hover_name="region",
                 title="BMI Distribution by Age Group", labels={"bmi": "BMI", "charges": "Costs"},
                 template="custom", color_continuous_scale='Viridis')
fig4.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white', 
    font=dict(color='black'),
    xaxis_title="BMI",
    yaxis_title="Costs",
    coloraxis_colorbar=dict(title="Age", tickfont=dict(color='black')),
    legend=dict(
        font=dict(color='black'),
        bordercolor='black',
        borderwidth=1
    )
)
st.plotly_chart(fig4, use_container_width=True)

st.write("")  # Add a blank line for spacing

high_cost_df = df[df['charges'] > df['charges'].quantile(0.75)]
fig5 = px.scatter_matrix(high_cost_df, dimensions=["age", "bmi", "children", "charges"], color="smoker",
                         title="Profile of Beneficiaries with Highest Costs",
                         labels={"charges": "Costs", "age": "Age", "bmi": "BMI", "children": "Children"},
                         template="custom", color_discrete_map={'yes': '#FF4B4B', 'no': '#4CAF50'})
fig5.update_layout(
    plot_bgcolor='white', 
    paper_bgcolor='white', 
    font=dict(color='black'),
    legend=dict(
        font=dict(color='black'),
        bordercolor='black',
        borderwidth=1
    )
)
st.plotly_chart(fig5, use_container_width=True)
