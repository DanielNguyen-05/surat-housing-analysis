import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os

# --- CẤU HÌNH CHUNG (THEME) ---
# Thiết lập style chuyên nghiệp cho báo cáo khoa học
sns.set_theme(style="whitegrid", context="notebook", font_scale=1.1)
PALETTE = "viridis"  # Hoặc 'mako', 'rocket', 'deep'

def save_plot(fig, filename, folder="../assets"):
    """Hàm hỗ trợ lưu ảnh vào thư mục assets"""
    if filename:
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, filename)
        fig.savefig(path, dpi=300, bbox_inches='tight')
        print(f"Saved plot to {path}")

def plot_distribution(df, col, title, xlabel, log_scale=False, filename=None):
    """
    Vẽ phân phối (Histogram + KDE) cho biến số (Giá, Diện tích).
    Hỗ trợ chuyển đổi Logarit để xử lý dữ liệu bị lệch (Skewed).
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    data = df[col]
    if log_scale:
        data = np.log1p(data)
        xlabel = f"Log({xlabel})"
        title = f"{title} (Log Transformed)"

    sns.histplot(data, kde=True, color="#2E86AB", edgecolor="white", alpha=0.7, ax=ax)
    
    # Kẻ đường trung bình
    mean_val = data.mean()
    ax.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=15)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.legend()
    
    if filename: save_plot(fig, filename)
    plt.show()

def plot_count_top_n(df, col, title, n=10, filename=None):
    """
    Vẽ biểu đồ cột đếm số lượng (cho Categorical Data).
    Chỉ lấy Top N giá trị phổ biến nhất (Ví dụ: Top 10 Location).
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Lấy top N
    top_counts = df[col].value_counts().head(n)
    
    sns.barplot(x=top_counts.values, y=top_counts.index, palette=PALETTE, ax=ax)
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=15)
    ax.set_xlabel("Count", fontsize=12)
    ax.set_ylabel(col, fontsize=12)
    
    # Hiển thị số liệu trên thanh
    for i, v in enumerate(top_counts.values):
        ax.text(v + (v*0.01), i, str(v), va='center', fontsize=10)
        
    if filename: save_plot(fig, filename)
    plt.show()

def plot_scatter_price_area(df, x_col, y_col, title, hue=None, filename=None):
    """
    Vẽ biểu đồ phân tán (Scatter) để xem tương quan Giá vs Diện tích.
    """
    fig, ax = plt.subplots(figsize=(10, 7))
    
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, 
                    alpha=0.6, palette="deep", s=60, ax=ax)
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=15)
    
    # Format trục số (tránh hiển thị 1e7)
    ax.ticklabel_format(style='plain', axis='both')
    
    if filename: save_plot(fig, filename)
    plt.show()

def plot_box_comparison(df, numeric_col, category_col, title, filename=None):
    """
    Vẽ Boxplot để so sánh giá trị số giữa các nhóm (Ví dụ: Giá theo Số phòng ngủ).
    Giúp phát hiện Outliers.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    sns.boxplot(data=df, x=category_col, y=numeric_col, palette="Set2", showfliers=False, ax=ax)
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=15)
    ax.ticklabel_format(style='plain', axis='y')
    ax.grid(True, linestyle='--', alpha=0.3)
    
    if filename: save_plot(fig, filename)
    plt.show()

def plot_correlation_heatmap(df, title="Correlation Matrix", filename=None):
    """
    Vẽ Heatmap tương quan cho các biến số.
    """
    # Chỉ lấy các cột số
    numeric_df = df.select_dtypes(include=[np.number])
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    corr = numeric_df.corr()
    
    # Mask để che nửa trên (tam giác trên) cho đỡ rối
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", 
                linewidths=0.5, square=True, cbar_kws={"shrink": .8}, ax=ax)
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=15)
    
    if filename: save_plot(fig, filename)
    plt.show()

def plot_top_expensive_locations(df, loc_col, price_col, n=10, filename=None):
    """
    Vẽ Top N khu vực đắt đỏ nhất (theo trung bình giá/sqft).
    """
    # Gom nhóm và tính trung bình
    loc_stats = df.groupby(loc_col)[price_col].agg(['mean', 'count'])
    # Lọc khu vực có ít nhất 5 tin đăng để tránh nhiễu
    loc_stats = loc_stats[loc_stats['count'] >= 5]
    
    top_locs = loc_stats.sort_values(by='mean', ascending=False).head(n)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_locs['mean'], y=top_locs.index, palette="magma", ax=ax)
    
    ax.set_title(f"Top {n} Most Expensive Localities", fontsize=16, fontweight='bold')
    ax.set_xlabel(f"Average {price_col}", fontsize=12)
    
    if filename: save_plot(fig, filename)
    plt.show()