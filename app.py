import streamlit as st
import classifier
import pandas as pd


def predict(hlr, csb, csv, v_band_lum, core_radius, estimate_hmrt, hmrt):
    data = pd.DataFrame({
        'Observational Half-Light Radius': [hlr],
        'Central Surface Brightness':      [csb],
        'Central Velocity Dispersion':     [csv],
        'Total V-band luminosity':         [v_band_lum],
        'Observational Core Radius':       [core_radius],
        'Half-Mass Relaxation Time':       [hmrt]
    })
    
    clf = classifier.make_classifier(
        use_relaxation_time_estimate=estimate_hmrt,
        fallback_enabled=False
    )
    clf_with_fallback = classifier.make_classifier(
        use_relaxation_time_estimate=estimate_hmrt,
        fallback_enabled=True
    )
    
    bhs = classifier.predict(clf, data)[0]
    bhs_fallback = classifier.predict(clf_with_fallback, data)[0]
    
    return bhs, bhs_fallback


st.title('Black Hole Subsystem Prediction')

hlr = st.slider('Half-Light Radius (pc)', min_value=0.0, max_value=10.0, step=0.1, value=2.0)
csb = st.slider('Central Surface Brightness (Lsun/pc^2)', min_value=0.0, max_value=1e10, step=10.0, value=500.0)
csv = st.slider('Central Velocity Dispersion (km/s)', min_value=0.0, max_value=1000.0, step=0.5, value=5.0)
v_band_lum = st.slider('Total V-Band Luminosity (Lsun)', min_value=0.0, max_value=1e10, step=1000.0, value=5e5)
core_radius = st.slider('Observational Core Radius (pc)', min_value=0.0, max_value=10.0, step=0.1, value=1.0)
estimate_hmrt = st.checkbox('Use approximation for Median Relaxation Time instead of HMRT')
hmrt = st.slider('Half-Mass Relaxation Time (Myr)', min_value=0.0, max_value=1e100, step=100.0, value=1000.0)

if st.sidebar.button('Predict'):
    bhs, bhs_fallback = predict(hlr, csb, csv, v_band_lum, core_radius, estimate_hmrt, hmrt)
    st.write('# Black Hole Subsystem\n\n', bhs)
    st.write('# Black Hole Subsystem (w/Fallback)\n\n', bhs_fallback)
