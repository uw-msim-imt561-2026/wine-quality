import pandas as pd
import streamlit as st

def render_filters(df: pd.DataFrame) -> dict:
    """Rendering filter widgets and returning the chosen values."""
    st.sidebar.header("Filters")

    wine_type = ["All"] + sorted(df["wine_type"].unique().tolist())
    wine_types = st.sidebar.selectbox("View by Wine Type", wine_type, index=0)

    min_q, max_q = float(df["quality"].min()), float(df["quality"].max())
    q_range = st.sidebar.slider(
        "Quality Rating",
        min_value=min_q,
        max_value=max_q,
        value=(min_q, max_q),
        step=0.5,
    )

    return {
        "wine_type": wine_types,
        "quality_range": q_range,
    }


def apply_filters(df: pd.DataFrame, selections: dict) -> pd.DataFrame:
    """Applying filter selections to the dataframe."""
    out = df.copy()

    if selections["wine_type"] != "All":
        out = out[out["wine_type"] == selections["wine_type"]]

    q_min, q_max = selections["quality_range"]
    out = out[out["quality"].between(q_min, q_max)]

    return out.reset_index(drop=True)