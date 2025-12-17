import pandas as pd
import numpy as np
import re

def clean_currency_india(x):
    """
    Chuyển đổi tiền tệ Ấn Độ sang số Float (đơn vị Rupee).
    Input: '₹33.8 Lac', '₹5.5 Cr', '₹12,000'
    Output: 3380000.0, 55000000.0
    """
    if pd.isna(x):
        return np.nan
    
    x = str(x).lower().replace(',', '').replace('₹', '').strip()
    
    try:
        if 'lac' in x or 'lakh' in x:
            val = float(re.findall(r"[\d\.]+", x)[0])
            return val * 100000
        elif 'cr' in x or 'crore' in x:
            val = float(re.findall(r"[\d\.]+", x)[0])
            return val * 10000000
        else:
            # Trường hợp chỉ là số hoặc đơn vị lạ
            val = float(re.findall(r"[\d\.]+", x)[0])
            return val
    except (IndexError, ValueError):
        return np.nan

def extract_numbers(x):
    """
    Tách số từ chuỗi. Ví dụ: '644 sqft' -> 644.0
    """
    if pd.isna(x):
        return np.nan
    try:
        return float(re.findall(r"[\d\.]+", str(x).replace(',', ''))[0])
    except (IndexError, ValueError):
        return np.nan

def split_floor_info(x):
    """
    Tách thông tin tầng.
    Input: '5 out of 10', 'Ground out of 1'
    Output: (current_floor, total_floors)
    """
    if pd.isna(x):
        return np.nan, np.nan
    
    x = str(x).lower()
    
    if 'ground' in x:
        current = 0
    elif 'basement' in x:
        current = -1
    else:
        try:
            current = float(re.findall(r"(\d+)\s*out of", x)[0])
        except IndexError:
            current = np.nan

    try:
        total = float(re.findall(r"out of\s*(\d+)", x)[0])
    except IndexError:
        total = np.nan
        
    return current, total

def clean_text_column(x):
    """
    Chuẩn hóa cột text (bỏ khoảng trắng thừa, chữ thường).
    """
    if pd.isna(x) or str(x).strip() == '':
        return 'Unknown'
    return str(x).strip().title()

def process_data(df):
    """
    Hàm tổng hợp để chạy toàn bộ quy trình làm sạch.
    """
    df = df.copy()
    
    # 1. Xử lý Price 
    df['price_cleaned'] = df['price'].apply(clean_currency_india)
    df['price_per_sqft_cleaned'] = df['price_per_sqft'].apply(clean_currency_india)
    
    # 2. Xử lý Area
    df['area_sqft'] = df['square_feet'].apply(extract_numbers)
    
    # 3. Xử lý Floor (Tách thành 2 cột mới)
    floor_data = df['floor'].apply(split_floor_info)
    df['floor_current'] = [item[0] for item in floor_data]
    df['floor_total'] = [item[1] for item in floor_data]
    
    # 4. Xử lý Location từ Property Name (Ví dụ: "2 BHK ... in Dindoli Surat")
    # Giả sử format luôn là "... in [Location] Surat" hoặc lấy từ trước chữ Surat
    def extract_location(name):
        match = re.search(r"in\s+(.*?)\s+Surat", str(name), re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "Surat City"
    
    df['location_extracted'] = df['property_name'].apply(extract_location)
    
    # 5. Xử lý các cột Categorical bị lỗi (ví dụ: '1' trong furnishing)
    valid_furnishing = ['Unfurnished', 'Semi-Furnished', 'Furnished']
    df['furnishing'] = df['furnishing'].apply(lambda x: x if x in valid_furnishing else 'Unknown')
    
    valid_facing = ['East', 'West', 'North', 'South', 'North - East', 'South - East', 'North - West', 'South - West']
    df['facing'] = df['facing'].apply(lambda x: x if x in valid_facing else 'Unknown')

    return df