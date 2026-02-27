import pandas as pd
import streamlit as st

from src.charts import plot_corr_hist, plot_corr_heat, plot_quality_hist

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


def correlation_tab(df: pd.DataFrame) -> None:
    """Tabs layout with 3 default tabs."""
    t1, t2, t3 = st.tabs(["Bar Graph", "Heatmap", "Table"])

    with t1:
        st.subheader("Correlation Distribution")
        plot_corr_hist(df)
        st.caption("PUT INFO HERE")

    with t2:
        st.subheader("Correlation Heatmap")
        plot_corr_heat(df)

    with t3:
        st.subheader("Filtered Rows")
        st.dataframe(df, use_container_width=True, height=480)


    st.download_button(label="Download Filtered Data", data=df.to_csv(index=False), file_name="filtered_wine.csv",
                   mime="text/csv")