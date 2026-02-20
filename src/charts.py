import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns


def plot_quality_hist(df: pd.DataFrame) -> None:
    """Plotting a distribution of quality."""
    if df.empty:
        st.info("No rows match your filters.")
        return

    fig = px.histogram(
        df,
        x="quality",
        nbins=10,
        title='Distribution of Wine Quality Ratings',
        color_discrete_sequence=['#580F41']
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
    ax.set_title('Correlation of Features with Wine Quality (All Wines)', fontsize=14, fontweight='bold')
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