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

    st.sidebar.divider()
    st.sidebar.header ('Property Guide')
    st.sidebar.info ("Click a property to see how it influences wine quality.")
    wine_guide = {
        "Alcohol": "The amount of alcohol in the wine. The more alcohol, the more warmth. Higher alcohol levels are often associated with higher quality ratings. Alcohol concentration can be increased or decreased by monitoring the grape sugar concentration prior to the harvest.",
        "Chlorides": "The amount of salt in the wine. High levels can make the wine taste salty and decrease quality.",
        "Citric Acid": "Adds a fresh, citrusy flavor and can act as a preservative.",
        "Density": "Often referred to as the body. This is mouthfeel to determine how heavy or light the wine feels. Very related to alcohol and sugar content. Key indicators include color depth (light/dark), the speed of wine legs/tears, typically indicating higher alcohol or sugar content.",
        "Fixed Acidity": "Essential for freshness; it provides the tartness that balances the wine's sweetness.",
        "Free Sulfur Dioxide": "Prevents microbial growth and oxidation, helping maintain the wine's freshness.",
        "pH": "The measure of acidity. Determines wine stability and shelf life.",
        "Residual Sugar": "Determines sweetness. A balance between acidity and sugar is key for quality perception.",
        "Sulphates": "A wine preservative that contributes to antimicrobial stability and enhances flavor.",
        "Total Sulfur Dioxide": "The total SO2. SO2 is an antioxidant and antimicrobial preservative in wine, preventing spoilage, browning, and unwanted fermentation. If too high, it becomes noticeable to the nose and detracts from quality.",
        "Volatile Acidity": "Volatile acids, such as acetic acid, can cause an unpleasant vinegar taste at higher concentrations. "
    }

    for prop, description in wine_guide.items():
        with st.sidebar.expander(prop):
            st.write(description)

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