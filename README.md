# wine-quality

##To Open Up Our Environment
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app.py
```

# IMT 561 Streamlit Wine Quality Dashboard
SOMM is consulting for the Viticulture Commission of the Vinho Verde Region (CVRVV) in Portugal, the regulatory body responsible for certifying and promoting Vinho Verde wines from Northern Portugal. It controls, certifies, and promotes Vinho Verde wines, ensuring quality through laboratory analysis and granting the official seal of guarantee on bottles (Verde, n.d.). Our stakeholders are wondering what physicochemical qualities impact the quality of the wine and want to help wine companies produce high quality wine by understanding which properties affect quality.

To help CVRVV with this R&D and dissemination task, SOMM’s goal is to translate chemical wine data into practical, easy-to-understand guidance that CVRVV can share with local wineries. Therefore, SOMM’s primary stakeholder is CVRVV as well as the vineyards and wine producers in this region, looking to improve the quality of their wines. A secondary stakeholder would be other wine producers and companies in different regions, who may still find the insights valuable.

The dataset utilized contains 6,497 Portuguese Vinho Verde wine samples (4,898 white, 1,599 red) with 11 physicochemical properties and quality ratings from human tasters on a 0-10 scale. The data was collected by researchers Cortez et al. (2009) from the Viticulture Commission of the Vinho Verde Region (CVRVV). The data was collected for the intended purpose of “‘predicting’ human wine taste preferences that is based on easily available analytical tests at the certification step” (Cortez et al., 2009).

### Ethical Considerations
However,there are some limitations in the application of the insights, as there is no data about grape types, wine brand, or wine selling price. Additionally, there are many more normal wines rather than excellent or poor ones, and human tasters are subjective, as they are based on the experience and knowledge of the wine experts (Cortez et al., 2009).

## Questions We Are Answering
- What factors most influence Vinho Verde wine quality?
- How can we predict quality? 
- Which properties do not affect quality?
- Do physiochemical properties affect the quality of white versus red wines differently?

## Submission
- Streamlit Community Cloud Link: https://appapppy-zw78qomwpzfqrhzuhpu2gl.streamlit.app/