# -*- coding: utf-8 -*-
"""Phosphate_streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gpQPxAXqKR0uCvPBKdeBaMuLDEH_cNOH
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Title of the application
st.title("Phosphorus Sampling Visualization")

st.write("""
This enhanced application visualizes phosphorus sampling points on a dish with measurements.
Each sample point includes information such as tube number, cuvette number, and the phosphorus reading.
""")

# Load the data
data = {
    'Sample Point': [1, 2, 3, 4, 5, 6, 7, 8],
    'Tube Number': [1, 1, 2, 2, 3, 3, 4, 4],
    'Cuvette Number': [1, 2, 3, 4, 5, 6, 7, 8],
    'Reading': [0.782, 1.015, 0.191, 0.482, 0.122, 0.292, 0.837, 1.160]
}
df = pd.DataFrame(data)

# Display the raw data table
st.subheader("Phosphorus Measurement Data")
st.dataframe(df)

# Load the background image
image_path = "image.png"  # Replace with the path to your image file
img = mpimg.imread(image_path)

# Coordinates for sampling points
sample_coordinates = [
    (4, 5), (6, 5), (4, 6), (6, 6), (4, 7), (6, 7), (4, 8), (6, 8)
]

# Plot the image with sample points and readings
st.subheader("Sampling Points Visualization")
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(img, extent=[0, 10, 0, 10])  # Adjust image dimensions

# Overlay sampling points with annotations
for i, (x, y) in enumerate(sample_coordinates):
    sample_info = df.iloc[i]
    ax.plot(x, y, 'wo', markersize=15)  # White circle for sample point
    ax.text(x, y, f"T{sample_info['Tube Number']}\nC{sample_info['Cuvette Number']}\n{sample_info['Reading']}",
            color='black', ha='center', va='center', fontsize=8)

# Remove axes for cleaner display
ax.axis('off')
st.pyplot(fig)

# Quick summary statistics
st.subheader("Quick Statistics")
mean_reading = df['Reading'].mean()
max_reading = df['Reading'].max()
st.write(f"**Average Reading:** {mean_reading:.3f}")
st.write(f"**Maximum Reading:** {max_reading:.3f}")


