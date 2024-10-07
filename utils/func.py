import pandas as pd
import streamlit as st

from menu import menu_with_redirect

def convert_amount_sold(amount_str):
    if isinstance(amount_str, int):
        return amount_str
    if pd.isna(amount_str):
        return 0
    
    amount_str = amount_str.replace('ขายแล้ว', '').replace('ชิ้น', '').strip()
    if 'K' in amount_str:
        return int(float(amount_str.replace('K', '')) * 1000)
    elif 'k' in amount_str:
        return int(float(amount_str.replace('k', '')) * 1000)
    elif 'พัน' in amount_str:
        return int(float(amount_str.replace('พัน', '')) * 1000)
    else:
        return int(amount_str)
    
def get_head_title(no, sub):
    st.set_page_config(page_title=f"การวิเคราะห์ที่ {no}", page_icon="📈")
    st.header(f":blue[การวิเคราะห์ที่ {no}]", divider=True)
    st.subheader(sub)

    menu_with_redirect()
    hide_header_icons()
    return None

def section_title(text):
    st.html(f"<strong style='font-size: 18px; text-decoration: underline;'>{text}</strong>")
    return None

def hide_header_icons():
    hide_github_icon = """
                    <style>
                    .stActionButton {
                        visibility: hidden;
                    }
                    </style>
                    """
    st.markdown(hide_github_icon, unsafe_allow_html=True)

def get_color_map():
    return {
        'shopee': '#FE6132',  
        'lazada': '#0F0C76', 
    }

def break_page():
    st.markdown(
        """
            <style type="text/css" media="print">
            div.page-break
            {
                page-break-after: always;
                page-break-inside: avoid;
            }
            </style>
            <div class="page-break">
                <!-- Content goes here -->
            </div>
        """,
        unsafe_allow_html=True,
    )

def get_lat_lon():
    province_lat_lon = [
        {'province': 'กรุงเทพมหานคร', 'latitude': 13.7563, 'longitude': 100.5018},
        {'province': 'กรุงเทพฯ', 'latitude': 13.7563, 'longitude': 100.5018},
        {'province': 'กระบี่', 'latitude': 8.0863, 'longitude': 98.9063},
        {'province': 'กาญจนบุรี', 'latitude': 14.0041, 'longitude': 99.5483},
        {'province': 'กาฬสินธุ์', 'latitude': 16.4322, 'longitude': 103.5061},
        {'province': 'กำแพงเพชร', 'latitude': 16.4828, 'longitude': 99.5226},
        {'province': 'ขอนแก่น', 'latitude': 16.4419, 'longitude': 102.8350},
        {'province': 'จันทบุรี', 'latitude': 12.6114, 'longitude': 102.1039},
        {'province': 'ฉะเชิงเทรา', 'latitude': 13.6904, 'longitude': 101.0779},
        {'province': 'ชลบุรี', 'latitude': 13.3611, 'longitude': 100.9847},
        {'province': 'ชัยนาท', 'latitude': 15.1794, 'longitude': 100.1252},
        {'province': 'ชัยภูมิ', 'latitude': 15.8042, 'longitude': 102.0329},
        {'province': 'ชุมพร', 'latitude': 10.4930, 'longitude': 99.1800},
        {'province': 'เชียงใหม่', 'latitude': 18.7883, 'longitude': 98.9853},
        {'province': 'เชียงราย', 'latitude': 19.9106, 'longitude': 99.8406},
        {'province': 'ตรัง', 'latitude': 7.5591, 'longitude': 99.6114},
        {'province': 'ตราด', 'latitude': 12.2458, 'longitude': 102.5170},
        {'province': 'ตาก', 'latitude': 16.8698, 'longitude': 99.1426},
        {'province': 'นครนายก', 'latitude': 14.2068, 'longitude': 101.2131},
        {'province': 'นครปฐม', 'latitude': 13.8199, 'longitude': 100.0443},
        {'province': 'นครพนม', 'latitude': 17.4109, 'longitude': 104.7784},
        {'province': 'นครราชสีมา', 'latitude': 14.9799, 'longitude': 102.0977},
        {'province': 'นครศรีธรรมราช', 'latitude': 8.4324, 'longitude': 99.9631},
        {'province': 'นครสวรรค์', 'latitude': 15.7047, 'longitude': 100.1372},
        {'province': 'นนทบุรี', 'latitude': 13.8621, 'longitude': 100.5144},
        {'province': 'นราธิวาส', 'latitude': 6.4254, 'longitude': 101.8250},
        {'province': 'น่าน', 'latitude': 18.7846, 'longitude': 100.7782},
        {'province': 'บึงกาฬ', 'latitude': 18.3599, 'longitude': 103.6464},
        {'province': 'บุรีรัมย์', 'latitude': 14.9930, 'longitude': 103.1029},
        {'province': 'ปทุมธานี', 'latitude': 14.0209, 'longitude': 100.5250},
        {'province': 'ประจวบคีรีขันธ์', 'latitude': 11.8127, 'longitude': 99.7976},
        {'province': 'ปราจีนบุรี', 'latitude': 14.0498, 'longitude': 101.3689},
        {'province': 'ปัตตานี', 'latitude': 6.8697, 'longitude': 101.2505},
        {'province': 'พระนครศรีอยุธยา', 'latitude': 14.3696, 'longitude': 100.5876},
        {'province': 'พะเยา', 'latitude': 19.1684, 'longitude': 99.9012},
        {'province': 'พังงา', 'latitude': 8.4513, 'longitude': 98.5330},
        {'province': 'พัทลุง', 'latitude': 7.6170, 'longitude': 100.0810},
        {'province': 'พิจิตร', 'latitude': 16.4427, 'longitude': 100.3487},
        {'province': 'พิษณุโลก', 'latitude': 16.8211, 'longitude': 100.2659},
        {'province': 'เพชรบุรี', 'latitude': 13.1111, 'longitude': 99.9398},
        {'province': 'เพชรบูรณ์', 'latitude': 16.4182, 'longitude': 101.1606},
        {'province': 'แพร่', 'latitude': 18.1450, 'longitude': 100.1403},
        {'province': 'ภูเก็ต', 'latitude': 7.8804, 'longitude': 98.3923},
        {'province': 'มหาสารคาม', 'latitude': 16.1867, 'longitude': 103.2980},
        {'province': 'มุกดาหาร', 'latitude': 16.5440, 'longitude': 104.7183},
        {'province': 'แม่ฮ่องสอน', 'latitude': 19.3020, 'longitude': 97.9654},
        {'province': 'ยโสธร', 'latitude': 15.7922, 'longitude': 104.1459},
        {'province': 'ยะลา', 'latitude': 6.5411, 'longitude': 101.2800},
        {'province': 'ร้อยเอ็ด', 'latitude': 16.0538, 'longitude': 103.6531},
        {'province': 'ระนอง', 'latitude': 9.9520, 'longitude': 98.6083},
        {'province': 'ระยอง', 'latitude': 12.6814, 'longitude': 101.2787},
        {'province': 'ราชบุรี', 'latitude': 13.5283, 'longitude': 99.8134},
        {'province': 'ลพบุรี', 'latitude': 14.7995, 'longitude': 100.6534},
        {'province': 'ลำปาง', 'latitude': 18.2888, 'longitude': 99.4909},
        {'province': 'ลำพูน', 'latitude': 18.5736, 'longitude': 99.0087},
        {'province': 'เลย', 'latitude': 17.4860, 'longitude': 101.7223},
        {'province': 'ศรีสะเกษ', 'latitude': 15.1186, 'longitude': 104.3227},
        {'province': 'สกลนคร', 'latitude': 17.1554, 'longitude': 104.1402},
        {'province': 'สงขลา', 'latitude': 7.1756, 'longitude': 100.6144},
        {'province': 'สตูล', 'latitude': 6.6238, 'longitude': 100.0674},
        {'province': 'สมุทรปราการ', 'latitude': 13.5991, 'longitude': 100.5990},
        {'province': 'สมุทรสงคราม', 'latitude': 13.4144, 'longitude': 100.0026},
        {'province': 'สมุทรสาคร', 'latitude': 13.5472, 'longitude': 100.2744},
        {'province': 'สระแก้ว', 'latitude': 13.8240, 'longitude': 102.0644},
        {'province': 'สระบุรี', 'latitude': 14.5289, 'longitude': 100.9103},
        {'province': 'สิงห์บุรี', 'latitude': 14.8870, 'longitude': 100.4010},
        {'province': 'สุโขทัย', 'latitude': 17.0126, 'longitude': 99.8266},
        {'province': 'สุพรรณบุรี', 'latitude': 14.4745, 'longitude': 100.1207},
        {'province': 'สุราษฎร์ธานี', 'latitude': 9.1382, 'longitude': 99.3210},
        {'province': 'สุรินทร์', 'latitude': 14.8817, 'longitude': 103.4934},
        {'province': 'หนองคาย', 'latitude': 17.8783, 'longitude': 102.7426},
        {'province': 'หนองบัวลำภู', 'latitude': 17.2041, 'longitude': 102.4260},
        {'province': 'อ่างทอง', 'latitude': 14.5896, 'longitude': 100.4593},
        {'province': 'อุดรธานี', 'latitude': 17.3647, 'longitude': 102.8158},
        {'province': 'อุตรดิตถ์', 'latitude': 17.6200, 'longitude': 100.0993},
        {'province': 'อุทัยธานี', 'latitude': 15.3870, 'longitude': 100.0277},
        {'province': 'อุบลราชธานี', 'latitude': 15.2446, 'longitude': 104.8471},
        {'province': 'อำนาจเจริญ', 'latitude': 15.8628, 'longitude': 104.6291},
        {'province': 'ต่างประเทศ', 'latitude': 35.8617, 'longitude': 104.1954},
        {'province': 'จีน', 'latitude': 35.8617, 'longitude': 104.1954}
    ]
    return pd.DataFrame(province_lat_lon)
