import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filepath):
    """Load and preprocess HR dataset"""
    df = pd.read_csv(filepath)
    df.rename(columns={
        'average_montly_hours': 'average_monthly_hours',
        'Department': 'department',
        'Work_accident': 'work_accident'
    }, inplace=True)
    df['salary'] = df['salary'].map({'low': 0, 'medium': 1, 'high': 2})
    df = pd.get_dummies(df, columns=['department'], drop_first=True)
    return df

def plot_feature_distributions(df, features, save_dir="plots/"):
    """Generate KDE plots for each feature split by 'left' and save them"""
    os.makedirs(save_dir, exist_ok=True)
    for col in features:
        plt.figure(figsize=(8, 4))
        sns.kdeplot(data=df, x=col, hue='left', fill=True, common_norm=False, palette='Set2')
        plt.title(f"Distribution of {col} by Turnover")  
        plt.tight_layout()
        save_path = os.path.join(save_dir, f"{col}_by_turnover.png")
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Saved: {save_path}")
        plt.close()
