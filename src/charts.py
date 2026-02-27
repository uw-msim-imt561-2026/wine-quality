import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from src.filters import render_filters, apply_filters

def plot_quality_hist(df: pd.DataFrame, side_by_side:bool) -> None:
    """Plotting a distribution of quality."""

    if df.empty:
        st.info("No rows match your filters.")
        return

    if side_by_side:
        fig = px.histogram(
            df,
            x="quality",
            color="wine_type",
            barmode="group",
            title="Quality Distribution by Wine Type",
            color_discrete_map={"red": "#580F41", "white": "#F0E68C"},
            labels={"quality": "Quality Rating", "count": "Count", "wine_type": "Wine Type"},
        )
    else:
        fig = px.histogram(
            df,
            x="quality",
            nbins=10,
            title="Distribution of Wine Quality Ratings",
            color_discrete_sequence=["#580F41"],
        )

    st.plotly_chart(fig, use_container_width=True)


def plot_corr_hist(df: pd.DataFrame) -> None:
    """Bar graph for correlations"""
    if df.empty:
        st.info("No rows match your filters.")
        return

    corr_with_quality = df.select_dtypes(include=['float64', 'int64']).corrwith(df['quality']).drop(
        'quality').sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(corr_with_quality.index, corr_with_quality.values, color='#580F41')
    ax.set_title('Correlation of Features with Wine Quality', fontsize=14, fontweight='bold')
    ax.set_xlabel('Correlation')
    st.pyplot(fig)


def plot_corr_heat(df: pd.DataFrame) -> None:
    """Heatmap for correlations"""
    if df.empty:
        st.info("No rows match your filters.")
        return

    custom_cmap = LinearSegmentedColormap.from_list('custom', ['#580F41', 'white', '#D0E68C'])
    corr_matrix = df.select_dtypes(include=['float64', 'int64']).corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap=custom_cmap, center=0, fmt='.2f', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

    st.plotly_chart(fig, use_container_width=True)


def plot_scatter_quality(df: pd.DataFrame) -> None:
    """Scatter plot for quality distribution."""

    wine_type = df['wine_type'].unique()

    if len(wine_type) == 1 and wine_type[0] == "red":
        st.info("Red Wines: **Alcohol** is the strongest positive correlation. **Volatile Acidity** is the biggest negative factor in reds.")
    elif len(wine_type) == 1 and wine_type[0] == "white":
        st.info("White Wines: **Alcohol** is the strongest positive correlation. **Density** is the biggest negative factor in whites.")
    else:
        st.info("All Wines: **Alcohol** has a strong positive correlation. **Volatile acidity** and **density** are the largest negative factors.")

    property_options = ['alcohol', 'fixed acidity', 'free sulfur dioxide', 'total sulfur dioxide',
                        'volatile acidity', 'citric acid', 'sulphates',
                        'density', 'chlorides', 'pH', 'residual sugar']

    prop = st.selectbox(
        "Select a Property to See Correlation with Quality",
        options=property_options,
        index=0
    )

    mean_df = df.groupby('quality')[prop].mean().reset_index()

    fig = px.scatter(
        df,
        x=prop,
        y='quality',
        opacity=0.3,
        title=f'{prop.title()} vs Quality',
        labels={'quality': 'Quality', prop: prop.title()},
        color_discrete_sequence=['#580F41']
    )

    fig.add_scatter(
        x=mean_df[prop],
        y=mean_df['quality'],
        mode='lines+markers',
        line=dict(color='darkviolet', width=2, dash='dash'),
        marker=dict(size=8),
        name='Mean'
    )

    st.plotly_chart(fig, use_container_width=True)



