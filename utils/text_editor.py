from streamlit_quill import st_quill
import streamlit as st
import os

def display_html_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        st.html(html_content)
    else:
        pass

def generate(filename):
    file = f"text/{filename}.html"
    # display_html_from_file(file)

    if 'quill_content' not in st.session_state:
        st.session_state.quill_content = ""

    content = st_quill(
        placeholder="Write your text here",
        html=True,
        key="quill_content",
        value=st.session_state.quill_content
    )

    if content:

        # st.subheader("Content")
        # st.text(content)

        # st.subheader("Example")
        # st.html(content)
        if st.button("Save"):
            with open(file, "w") as file:
                file.write(content)
            st.success("Content saved successfully!")

import plotly.graph_objects as go

def get_color_template():
    # List of colors
    colors = [
        "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black",
        "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse",
        "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan",
        "darkgoldenrod", "darkgray", "darkgrey", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen",
        "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray",
        "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue",
        "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray",
        "grey", "green", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender",
        "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow",
        "lightgray", "lightgrey", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray",
        "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine",
        "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise",
        "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive",
        "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip",
        "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "rebeccapurple", "saddlebrown",
        "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow",
        "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"
    ]

    # Create a bar chart
    fig = go.Figure()

    for color in colors:
        fig.add_trace(go.Bar(
            x=[color],
            y=[1],
            marker=dict(color=color),
            showlegend=False
        ))

    # Update layout to fit all bars
    fig.update_layout(
        title="Color Samples",
        xaxis=dict(tickangle=-45, showticklabels=False),
        yaxis=dict(showticklabels=False),
        height=2000,  # Adjust the height if needed
        margin=dict(l=10, r=10, t=30, b=10)
    )
    st.plotly_chart(fig, theme="streamlit")