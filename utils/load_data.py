import pandas as pd
from utils.func import convert_amount_sold, get_lat_lon
import os
import streamlit as st
import zipfile
import asyncio


# @st.cache_data
async def load_data():
    dataframes = []
    zip_folder = 'data'  # Folder where the zip files are stored
    
    # Iterate over all zip files in the folder
    for filename in os.listdir(zip_folder):
        if filename.endswith('.zip'):
            zip_path = os.path.join(zip_folder, filename)
            
            # Open the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # Iterate over all the files in the zip archive
                for csv_file in zip_ref.namelist():
                    if csv_file.endswith('.csv'):
                        # Open CSV file inside zip
                        with zip_ref.open(csv_file) as file:
                            # Read the CSV file into a DataFrame
                            df = pd.read_csv(file)
                            clean_df = df.drop_duplicates()  # Clean the data
                            dataframes.append(clean_df)
    
    # Combine all DataFrames into one
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df


# @st.cache_data
async def get_data():
    data = await load_data()
    data = data[data['status_title'] == 'ได้รับการรับรอง']
    return data
