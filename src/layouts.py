import pandas as pd
import streamlit as st

from src.charts import (
    plot_corr_hist,
    plot_corr_heat,
    plot_quality_hist,
    plot_corr_bar_plotly,
    plot_corr_heat_plotly,
)

def insights_tab(df: pd.DataFrame) -> None:
    """Key Insights"""
    all_corr = df.select_dtypes(include=['float64', 'int64']).corrwith(df['quality']).drop('quality')

    top_positive = str(all_corr.idxmax())
    top_positive_val = all_corr.max()

    harmful = str(all_corr.idxmin())
    harmful_val = all_corr.min()

    low_impact = (all_corr.abs() < 0.1).sum()

    with st.container(border=True):
        st.subheader("Key Insights")
        c1, c2, c3, c4 = st.columns(4, border=True)

        with c1:
            st.metric("Average Quality", round(df["quality"].mean(), 2), "out of 10")
        with c2:
            st.metric("Top Positive Factor", top_positive.title(), f"{top_positive_val:.1%} correlation")
        with c3:
            st.metric("Most Harmful Factor", harmful.title(), f"{harmful_val:.1%} correlation")
        with c4:
            st.metric("Low Impact Factors", f"{low_impact} properties", "minimal effect on quality")

        st.info(f"""
           **Recommendations for Wine Producers:**
           - Increase **{top_positive.title()}** to improve quality
           - Reduce **{harmful.title()}** - it negatively impacts quality
           """)


def correlation_tab(df_f):
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Bar Graph", "Bar Graph Side-by-Side", "Heatmap", "Table"]
    )

    # 1) Single Bar Graph (uses whatever is filtered)
    with tab1:
        st.subheader("Correlation Distribution")
        plot_corr_bar_plotly(df_f, "Correlation with Wine Quality")

    # 2) Side-by-side bar graphs (red vs white)
    with tab2:
        st.subheader("Property Correlation (Red vs White)")

        if df_f["wine_type"].nunique() > 1:
            c1, c2 = st.columns(2, gap="large")
            with c1:
                plot_corr_bar_plotly(df_f[df_f["wine_type"] == "red"], "Red Wine Correlation")
            with c2:
                plot_corr_bar_plotly(df_f[df_f["wine_type"] == "white"], "White Wine Correlation")
        else:
            st.info("Select Wine Type = 'All' to view side-by-side comparisons.")

    # 3) Heatmap
    with tab3:
        st.subheader("Correlation Heatmap")
        plot_corr_heat_plotly(df_f)

    # 4) Table
    with tab4:
        st.subheader("Filtered Rows")
        st.dataframe(df_f, use_container_width=True, height=520)


    st.download_button(label="Download Filtered Data", data=df_f.to_csv(index=False), file_name="filtered_wine.csv",
                   mime="text/csv")