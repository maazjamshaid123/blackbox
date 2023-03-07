import streamlit as st
import classifier
import pandas as pd

def detect_hole():
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


    st.title('Black Holes in Globular Clusters')
    st.write('Enter the following properties of the Globular Clusters')

    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        hlr = st.number_input('Half-Light Radius ($pc$)', value=2.0)
        csb = st.number_input('Central Surface Brightness ($L_{\odot}\,\mathrm{pc}^{-2}$.)', value=500.0)
        csv = st.number_input('Central Velocity Dispersion ($km/s$)', value=5.0)
    with col2:
        v_band_lum = st.number_input('Total V-Band Luminosity ($L_{\odot}$)', value=5e5)
        core_radius = st.number_input('Observational Core Radius ($pc$)', value=1.0)
        hmrt = st.number_input('Half-Mass Relaxation Time ($Myr$)', value=1000.0)
        estimate_hmrt = st.checkbox('Use approximation for Median Relaxation Time instead of Half-Mass Relaxation Time')

    if st.button('Predict Black Hole Subsystem'):
        bhs, bhs_fallback = predict(hlr, csb, csv, v_band_lum, core_radius, estimate_hmrt, hmrt)
        st.subheader('$Black$ $Hole$ $Subsystem$')
        if bhs == 1:
            bhs = "Present"
            st.success(bhs, icon="✔️")
        else:
            bhs = "Not Present"
            st.error(bhs, icon="❌")

        
        
        # st.write('# Black Hole Subsystem (w/Fallback)\n\n', bhs_fallback)


