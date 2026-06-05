# Project 2: Data Classification Using AI (K-Nearest Neighbors)

## 📌 Project Overview

This project demonstrates the transition from traditional rule-based programming to Machine Learning using Supervised Learning techniques.

The implementation uses the K-Nearest Neighbors (KNN) algorithm and the Iris Dataset to classify flower species based on their physical characteristics.

The project covers the complete machine learning workflow, including data preprocessing, feature scaling, model training, prediction, and performance evaluation.

---

## 🏗️ System Architecture (IPO Model)

### Input

* Iris Dataset
* 150 Flower Samples
* 4 Numerical Features:

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width

### Process

1. Load the Iris dataset.
2. Split data into training and testing sets.
3. Apply StandardScaler for feature normalization.
4. Train the KNN classifier.
5. Predict classes for unseen data.
6. Evaluate model performance.

### Output

* Predictions
* Confusion Matrix
* Precision Score
* Recall Score
* F1 Score
* Accuracy Score

---

## 🛠️ Technologies Used

* Python 3.x
* NumPy
* Pandas
* Scikit-learn

---

## 🚀 Installation & Setup

### Prerequisites

Install Python 3.8 or higher.

Verify installation:

```bash
python --version
```

### Install Required Libraries

```bash
pip install numpy pandas scikit-learn
```

---

## ▶️ Running the Project

Navigate to the project directory:

```bash
cd project2_data_classification
```

Run the program:

```bash
python classification_project.py
```

---

## 📊 Dataset Information

### Iris Dataset

| Property      | Value    |
| ------------- | -------- |
| Total Samples | 150      |
| Features      | 4        |
| Classes       | 3        |
| Dataset Type  | Balanced |

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## 🔄 Machine Learning Workflow

### Data Preparation

* Dataset Loading
* Feature Extraction
* Label Extraction

### Data Splitting

* Training Data: 80%
* Testing Data: 20%

### Feature Scaling

StandardScaler transforms data so that:

* Mean = 0
* Standard Deviation = 1

### Model Training

K-Nearest Neighbors algorithm learns patterns from training data.

### Evaluation

Performance is measured using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🧪 Verification Test Cases

| Test Case        | Expected Result        |
| ---------------- | ---------------------- |
| Dataset Loading  | Successful             |
| Train-Test Split | 120 Train / 30 Test    |
| Scaling          | Features normalized    |
| Model Training   | Successful             |
| Prediction       | Class labels generated |
| Evaluation       | Metrics displayed      |

---

## 📈 Expected Output

```text
Dataset Shape: (150, 4)

Training Samples: 120
Testing Samples: 30

Confusion Matrix:
[[10 0 0]
 [0 10 0]
 [0 1 9]]

Accuracy: 96.67%
F1 Score: 0.96
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Supervised Learning
* Classification Algorithms
* Data Preprocessing
* Feature Scaling
* Model Training
* Model Testing
* Performance Evaluation

---

## ✅ Requirements Achieved

* [x] Supervised Learning Implementation
* [x] KNN Classification Model
* [x] Dataset Handling
* [x] Feature Scaling
* [x] Train-Test Split
* [x] Performance Evaluation
* [x] Prediction on Unseen Data

---

Developed for DecodeLabs Industrial Training Program (Batch 2026)

Project Milestone 2: Data Classification Using AI
