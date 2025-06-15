from models import load_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc
)

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def train_and_evaluate(model, X_train, X_test, y_train, y_test, name):
    print(f"\n ----- {name} -----")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, digits=3))

def plot_feature_importance(model, X, save_path="plots/feature_importance_rf.png"):
    importances = model.feature_importances_
    feature_names = X.columns
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances[indices], y=feature_names[indices])
    plt.title("🔍 Feature Importance — Random Forest")
    plt.xlabel("Importance Score")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved feature importance plot to {save_path}")

def plot_confusion_matrix_heatmap(model, X_test, y_test, save_path="plots/confusion_matrix_rf.png"):
    plt.figure(figsize=(6, 5))
    disp = ConfusionMatrixDisplay.from_estimator(
        model, X_test, y_test,
        display_labels=["Stayed", "Left"],
        cmap="Blues",
        colorbar=False
    )
    disp.ax_.set_title("Confusion Matrix — Random Forest")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Saved confusion matrix heatmap to {save_path}")

def plot_roc_curves(models, X_test, y_test, save_path="plots/roc_curves.png"):
    plt.figure(figsize=(8, 6))
    
    for name, model in models.items():
        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
        else:
            y_prob = model.decision_function(X_test)

        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.3f})")

    plt.plot([0, 1], [0, 1], "k--", label="Chance")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curves — Model Comparison")
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Saved ROC curve plot to {save_path}")

def main():
    # Load and preprocess data
    df = load_data("data/HR_capstone_dataset.csv")
    X = df.drop("left", axis=1)
    y = df["left"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Define models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42),
        "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss", random_state=42)
    }

    # Train and evaluate each
    for name, model in models.items():
        train_and_evaluate(model, X_train, X_test, y_train, y_test, name)

    # Visual outputs for Random Forest
    rf_model = models["Random Forest"]
    plot_feature_importance(rf_model, X)
    plot_confusion_matrix_heatmap(rf_model, X_test, y_test)

    # ROC Curves for all models
    plot_roc_curves(models, X_test, y_test)

if __name__ == "__main__":
    main()
