import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score

def run_pipeline():
    print("="*60)
    print("DECODELABS AI INTERNSHIP: PROJECT 2 - DATA CLASSIFICATION")
    print("="*60)
    
    # -----------------------------------------------------------------
    # [1] INPUT STAGE: Load and Understand Dataset
    # -----------------------------------------------------------------
    print("\n[1/3] INPUT STAGE: Fetching Raw Iris Benchmark Data...")
    iris = load_iris()
    
    # 150 Balanced Samples, 3 Classes, 4 Dimensions
    X = iris.data  
    y = iris.target
    
    print(f" -> Total Samples: {X.shape[0]} (Balanced)")
    print(f" -> Distinct Target Classes: {len(np.unique(y))} {list(iris.target_names)}")
    print(f" -> Data Dimensions/Features: {X.shape[1]}")
    print(f"    Features tracked: {iris.feature_names}")

    # -----------------------------------------------------------------
    # [2] PROCESS STAGE: Prepare, Split, Scale, and Train Model
    # -----------------------------------------------------------------
    print("\n[2/3] PROCESS STAGE: Executing Data Operations...")
    
    # Structural Integrity: Shuffle and Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, shuffle=True
    )
    print(f" -> Structural Integrity Check: Training Samples ({len(X_train)}), Test Samples ({len(X_test)})")
    
    # The Gatekeeper Rule: Scaling features to Mean=0, Variance=1
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print(" -> Feature Scaling complete via StandardScaler.")
    
    # Algorithmic Training: K-Nearest Neighbors 
    k_neighbors = 3
    print(f" -> Initializing KNN Model with K={k_neighbors}...")
    model = KNeighborsClassifier(n_neighbors=k_neighbors)
    model.fit(X_train_scaled, y_train)
    print(" -> Model training complete. Pure algorithmic logic established.")

    # -----------------------------------------------------------------
    # [3] OUTPUT STAGE: Validate Performance & Generate Metrics
    # -----------------------------------------------------------------
    print("\n[3/3] OUTPUT STAGE: Validating Model Performance...")
    
    # Model predictions
    y_pred = model.predict(X_test_scaled)
    
    # Generate Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    # Calculate Macro F1 Score
    macro_f1 = f1_score(y_test, y_pred, average='macro')
    
    print("\n--- PERFORMANCE METRICS ---")
    print("\n💡 Confusion Matrix:")
    print(cm)
    
    print(f"\n🎯 Macro F1 Score: {macro_f1:.4f}")
    
    print("\n📝 Detailed Classification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    
    # -----------------------------------------------------------------
    # EXTRA EXPERIMENTATION: Testing with completely new data
    # -----------------------------------------------------------------
    print("\n--- EXPERIMENTATION: PREDICTING UNSEEN DATA ---")
    # Simulating raw features: Sepal Length, Sepal Width, Petal Length, Petal Width
    custom_raw_data = np.array([[5.1, 3.5, 1.4, 0.2]]) 
    
    # The unseen data must pass through the exact same scaling gatekeeper
    custom_scaled_data = scaler.transform(custom_raw_data)
    custom_prediction = model.predict(custom_scaled_data)
    predicted_class_name = iris.target_names[custom_prediction[0]]
    
    print(f" Raw Unseen Measurements input: {custom_raw_data[0]}")
    print(f" Machine Derived Decision/Classification: [ {predicted_class_name.upper()} ]")
    print("="*60)

if __name__ == "__main__":
    run_pipeline()