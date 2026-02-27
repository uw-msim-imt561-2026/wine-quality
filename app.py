import streamlit as st

import src.filters
from src.data import load_data
from src.filters import render_filters, apply_filters

from src.charts import (
    plot_quality_hist,
    plot_corr_hist,
    plot_corr_heat,
    plot_scatter_quality,
    plot_corr_bar_plotly,
    plot_corr_heat_plotly,
)

from src.layouts import correlation_tab, insights_tab
# -----------------------------
# IMT 561 SOMM Group Dashboard: Wine Quality
# -----------------------------

def main() -> None:
    st.set_page_config(
        page_title="Group SOMM Wine Quality Dashboard",
        layout="wide",

    )


    with st.container(border=True):
        st.title("Vinho Verde Quality Dashboard")
        st.caption("Understanding How Physiochemical Properties Impact Wine Quality")



    #Data loading (cached)
    df = load_data("data/wine_data.csv")

#Add a quick 'data sanity' check and show row count
    # st.write(f"Row count: {df.shape[0]}")
    # # - show first 5 rows (optional)
    # st.dataframe(df.head(5))

 # -------------------------
    # Filters (sidebar by default)
    # -------------------------
    # render_filters returns a dictionary of user selections
    selections = render_filters(df)

 # apply_filters returns a filtered dataframe based on selections
    df_f = apply_filters(df, selections)
    insights_tab(df_f)
    st.divider()

    # -------------------------
    # Main body
    # -------------------------

    if selections["wine_type"] == "All":
        side_by_side = st.checkbox("View side-by-side", value=False)
    else:
        side_by_side = False

    with st.container(border=True):
        plot_quality_hist(df_f, side_by_side)

    st.divider()

    # Tabs layout by default (3 tabs)
    tab_choice = st.radio(
        "Choose a layout for the body:",
        ["Tabs (3)", "Two Columns"],
        horizontal=True,
    )
    if tab_choice == "Tabs (3)":
        with st.container(border=True):
           correlation_tab(df_f)
    else:
            # -------------------------
            # 2 columns
            # - left column: a chart
            # - right column: a table
            col1, col2 = st.columns(2, border =True)
            with col1:
                st.subheader("Property Correlation")
                plot_corr_bar_plotly(df_f)
                st.divider()
                plot_corr_heat_plotly(df_f)

            with col2:
                st.subheader("Filtered Rows")
                st.dataframe(df_f, use_container_width=True, height=420)

    st.divider()
    with st.container(border=True):
        plot_scatter_quality(df_f)


#Still need heatmaps and correlation graphs (idk how to differ those by page)
#Do we want to find a plotly graph for bar chart correlation?
#Could figure out how to do a side by side page
#Also need to figure out how to do property guide in streamlit






if __name__ == "__main__":
    main()


