import streamlit as st
import pandas as pd
import re
import os
import zipfile

st.set_page_config(layout="centered")

# Synchronous function for loading data
@st.cache_data(show_spinner=True)
def load_data():
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
    combined_df = combined_df[combined_df['status_title'] == 'ได้รับการรับรอง']
    combined_df['garden_province'] = combined_df['garden_address'].apply(extract_province)
    combined_df['farmer_province'] = combined_df['farmer_address'].apply(extract_province)
    combined_df = combined_df[(combined_df['mobile'].notna()) | (combined_df['email'].notna())]

    combined_df = combined_df[['fullname', 'name', 'type_name', 'mobile', 'email', 'garden_address', 'garden_province', 
                               'farmer_address', 'farmer_province', 'area_size', 'plant_qty', 'cycle_qty', 
                               'output_qty', 'garden_code', 'status_title']]
    
    combined_df.rename(columns={
        'fullname': 'ชื่อ-นามสกุล',
        'garden_code': 'รหัสแปลง',
        'garden_address': 'ที่อยู่แปลง', 
        'garden_province': 'จังหวัด (แปลง)',
        'farmer_address': 'ที่อยู่เกษตรกร', 
        'farmer_province': 'จังหวัด (เกษตรกร)', 
        'area_size': 'พื้นที่ปลูก(ไร่)', 
        'plant_qty': 'จำนวน(ต้น)',
        'cycle_qty': 'รอบการผลิต', 
        'output_qty': 'ปริมาณการผลิต(กิโลกรัม)', 
        'name': 'ชื่อพืช', 
        'type_name': 'มาตรฐานการผลิต', 
        'status_title': 'สถานะ'
    }, inplace=True)
    
    return combined_df

# Helper function for extracting province
def extract_province(address):
    match = re.search(r"จ\.(\S+)", address)
    if match:
        return match.group(1)
    return None

# Cache the function to split the dataframe into pages
# @st.cache_data(show_spinner=False)
def split_frame(input_df, rows):
    df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
    return df

# Load dataset
dataset = load_data()

# Filter section
with st.expander("Filter Data"):
    filters = {}
    col_filters = ['ชื่อพืช', 'ชื่อ-นามสกุล', 'จังหวัด (แปลง)', 'จังหวัด (เกษตรกร)']
    for col in col_filters:
        if pd.api.types.is_numeric_dtype(dataset[col]):
            min_val, max_val = st.slider(
                f"Filter by {col}", 
                min_value=float(dataset[col].min()), 
                max_value=float(dataset[col].max()), 
                value=(float(dataset[col].min()), float(dataset[col].max()))
            )
            filters[col] = (min_val, max_val)
        else:
            unique_vals = dataset[col].unique()
            selected_vals = st.multiselect(f"Filter by {col}", options=unique_vals)
            filters[col] = selected_vals
    
    # Apply filters
    for col, filter_vals in filters.items():
        if isinstance(filter_vals, tuple):  # Numeric filter
            dataset = dataset[dataset[col].between(*filter_vals)]
        else:  # Categorical filter
            if filter_vals:  # Only apply if there are selected values
                dataset = dataset[dataset[col].isin(filter_vals)].reset_index(drop=True)
                st.write(f"Result: {len(dataset)} records.")

# Sorting section
top_menu = st.columns(3)
with top_menu[0]:
    sort = st.radio("Sort Data", options=["Yes", "No"], horizontal=1, index=1)
if sort == "Yes":
    with top_menu[1]:
        sort_field = st.selectbox("Sort By", options=dataset.columns)
    with top_menu[2]:
        sort_direction = st.radio(
            "Direction", options=["⬆️", "⬇️"], horizontal=True
        )
    dataset = dataset.sort_values(
        by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True
    )
    
st.download_button(
    label="Export File",
    data=dataset.to_csv(index=False).encode('utf-8'),
    file_name='farm.csv',
    mime='text/csv'
)

# Pagination section
pagination = st.container()
bottom_menu = st.columns((4, 1, 1))
with bottom_menu[2]:
    batch_size = st.selectbox("Page Size", options=[50, 100, 150])
with bottom_menu[1]:
    total_pages = (
        int(len(dataset) / batch_size) if int(len(dataset) / batch_size) > 0 else 1
    )
    current_page = st.number_input(
        "Page", min_value=1, max_value=total_pages, step=1
    )
with bottom_menu[0]:
    st.markdown(f"Page **{current_page}** of **{total_pages}** ")

# Split the dataframe into pages
pages = split_frame(dataset, batch_size)

# Display the dataframe with custom height and filtering options
pagination.dataframe(data=pages[current_page - 1], use_container_width=True, height=600, hide_index=True)
