import streamlit as st

def show_intro():
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('bb_logo.png')
        # video_file = open('ODYSSEY.mp4', 'rb')
        # video_bytes = video_file.read()
        # st.video(video_bytes)

    st.title("$Black Box$ $by$  $AstroAlgo$")
    st.subheader('_Detect Black Hole Subsystems in Globular Clusters_')

    st.markdown('----')

    st.write('Provide feedback [here](https://forms.gle/5hKrGPJGqs2aeHUC8)')
    st.write('[Linkedin](https://www.linkedin.com/company/astroalgo)')

    st.markdown("---")

    st.info('''$Black$ $Box$ is an innovative product developed by AstroAlgo, designed to predict 
    black hole subsystems in globular clusters using advanced algorithms and machine learning 
    techniques. Black Box has the capability to revolutionize the field of astrophysics by 
    providing accurate predictions and insights into the existence of black holes in the 
    universe. ''')

    st.error('_Black Box uses the following properties of the Globular Clusters:_')
    # Define the list of items to display
    items = [
        'Observational Half-Light Radius',
        'Central Surface Brightness',
        'Central Velocity Dispersion',
        'Total V-band luminosity',
        'Observational Core Radius',
        'Half-Mass Relaxation Time',
        'Median Relaxation Time',
    ]

    # Calculate the number of rows required to display all the items
    num_rows = len(items) // 3 + 1

    # Use a for loop to display each item in a separate column
    for i in range(num_rows):
        col1, col2, col3 = st.columns(3)
        if i*3 < len(items):
            col1.info(items[i*3])
        if i*3+1 < len(items):
            col2.info(items[i*3+1])
        if i*3+2 < len(items):
            col3.info(items[i*3+2])

    st.markdown("---")

    st.write('''
    MIT License

Copyright (c) 2018 Ammar Askar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
    ''')

    st.markdown("---")



