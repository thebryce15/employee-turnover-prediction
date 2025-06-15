from models import load_data, plot_feature_distributions

def main():
    # Load and clean data
    df = load_data("data/HR_capstone_dataset.csv")
    
    # Define features to analyze
    features = [
        'satisfaction_level',
        'last_evaluation',
        'average_monthly_hours',
        'time_spend_company'
    ]
    
    # Generate and save distribution plots
    plot_feature_distributions(df, features, save_dir="plots/")

if __name__ == "__main__":
    main()
