import pandas as PDF 
import numpy as np
import matplotlib.pyplot as plt

print("CyberGuard AI 🚀")
print("Libraries loaded successfully!")

import os

for root, dirs, files in os.walk("/kaggle/input"):
    for file in files:
        print(os.path.join(root, file))

import os

csv_files = []

for root, dirs, files in os.walk("/kaggle/input"):
    for file in files:
        if file.lower().endswith(".csv"):
            csv_files.append(os.path.join(root, file))

if csv_files:
    print("CSV files found:", len(csv_files))
    for i, file in enumerate(csv_files):
        print(i, "->", file)
else:
    print("❌ No CSV dataset found.")
    print("Please add the CICIDS2017 DATASET using Add Input → Datasets.")

import os
import pandas as pd

csv_files = []

for root, dirs, files in os.walk("/kaggle/input"):
    for file in files:
        if file.lower().endswith(".csv"):
            csv_files.append(os.path.join(root, file))

print("CSV files found:", len(csv_files))

for i, file in enumerate(csv_files):
    print(i, "->", file)

df = pd.read_csv(csv_files[0])

print("Dataset loaded successfully ✅")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

display(df.head())

print("Dataset Shape:", df.shape)

print("\nColumn Names:")
for i, col in enumerate(df.columns):
    print(i, "→", col)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

before = len(df)

df = df.drop_duplicates()

after = len(df)

print("Duplicates removed:", before - after)
print("Rows remaining:", after)

df.columns = df.columns.str.strip()

print("Column names cleaned successfully ✅")
print(df.columns.tolist())

import numpy as np
import pandas as pd

missing = df.isnull().sum()

print("Missing values before cleaning:")
print(missing[missing > 0])

df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

print("\nMissing values after cleaning:")
print(df.isnull().sum().sum())

print("Remaining rows:", len(df))

label_cols = [col for col in df.columns if "label" in col.lower()]

print("Label columns:", label_cols)

label_col = label_cols[0]

print("\nLabel column:", label_col)
print("\nAttack distribution:")
print(df[label_col].value_counts())

import matplotlib.pyplot as plt

label_col = [col for col in df.columns if "label" in col.lower()][0]

label_counts = df[label_col].value_counts()

plt.figure(figsize=(12, 6))
label_counts.plot(kind="bar")

plt.title("CICIDS2017 Attack Distribution")
plt.xlabel("Traffic Type")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

df["Traffic_Type"] = df[label_col].apply(
    lambda x: "Normal" if x.upper() == "BENIGN" else "Attack"
)

traffic_counts = df["Traffic_Type"].value_counts()

print(traffic_counts)

plt.figure(figsize=(8, 5))

traffic_counts.plot(kind="bar")

plt.title("Normal vs Attack Traffic")
plt.xlabel("Traffic Type")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

df[label_col] = df[label_col].astype(str).str.strip()

label_counts = df[label_col].value_counts()

print("Total records:", len(df))
print("Total classes:", len(label_counts))

display(label_counts)

attack_counts = df[df["Traffic_Type"] == "Attack"][label_col].value_counts()

print("Top 10 Attack Types:")
print(attack_counts.head(10))

top_attacks = attack_counts.head(10)

plt.figure(figsize=(12, 6))

top_attacks.sort_values().plot(kind="barh")

plt.title("Top 10 Attack Types in CICIDS2017")
plt.xlabel("Number of Records")
plt.ylabel("Attack Type")
plt.tight_layout()
plt.show()

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing:", df.isnull().sum().sum())

print("\nTraffic:")
print(df["Traffic_Type"].value_counts())

numeric_cols = df.select_dtypes(include="number").columns

print("Numeric columns:", len(numeric_cols))

for col in numeric_cols:
    if df[col].nunique() > 1:
        print(col, "->", round(abs(df[col].corr(
            df["Traffic_Type"].map({"Normal": 0, "Attack": 1})
        )), 4))

target = df["Traffic_Type"].map({"Normal": 0, "Attack": 1})

numeric_cols = df.select_dtypes(include=np.number).columns

scores = {}

for col in numeric_cols:
    if df[col].nunique() > 1:
        scores[col] = abs(df[col].corr(target))

top_features = pd.Series(scores).sort_values(ascending=False).head(10)

print("Top 10 features:")
print(top_features)

plt.figure(figsize=(10, 6))

top_features.sort_values().plot(kind="barh")

plt.title("Top 10 Features Related to Attack Traffic")
plt.xlabel("Absolute Correlation")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()

features = [c for c in top_features.index if c in df.columns]

ml_df = df[features + ["Traffic_Type"]].replace([np.inf, -np.inf], np.nan).dropna()

normal = ml_df[ml_df["Traffic_Type"] == "Normal"]
attack = ml_df[ml_df["Traffic_Type"] == "Attack"]

n = min(len(normal), len(attack), 10000)

normal = normal.sample(n=n, random_state=42)
attack = attack.sample(n=n, random_state=42)

ml_df = pd.concat([normal, attack]).sample(frac=1, random_state=42)

print("ML dataset:", ml_df.shape)
print(ml_df["Traffic_Type"].value_counts())

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X = ml_df[features]
y = ml_df["Traffic_Type"].map({"Normal": 0, "Attack": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=50,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Model trained successfully ✅")
print("Accuracy:", round(accuracy_score(y_test, pred), 4))

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(
    y_test,
    pred,
    target_names=["Normal", "Attack"]
))

cm = confusion_matrix(y_test, pred)

print("Confusion Matrix:")
print(cm)

plt.figure(figsize=(6, 5))

plt.imshow(cm)
plt.title("Intrusion Detection Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks([0, 1], ["Normal", "Attack"])
plt.yticks([0, 1], ["Normal", "Attack"])

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.tight_layout()
plt.show()

importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False).head(10)

print("Top 10 Important Features:")
print(importance)

plt.figure(figsize=(10, 6))

importance.sort_values().plot(kind="barh")

plt.title("Top 10 Features Used by the AI Model")
plt.xlabel("Feature Importance")
plt.ylabel("Network Feature")
plt.tight_layout()
plt.show()

results = X_test.copy()

results["Actual"] = y_test.map({0: "Normal", 1: "Attack"})
results["Predicted"] = pd.Series(pred, index=X_test.index).map({
    0: "Normal",
    1: "Attack"
})

display(results.head(10))

correct = (results["Actual"] == results["Predicted"]).sum()
total = len(results)

print("Total Test Records:", total)
print("Correct Predictions:", correct)
print("Incorrect Predictions:", total - correct)
print("Detection Accuracy:", round(correct / total * 100, 2), "%")

import joblib

joblib.dump(model, "cyberguard_ai_model.pkl")

print("Model saved successfully ✅")
def detect_traffic(data):
    data = pd.DataFrame([data])
    data = data[features]
    prediction = model.predict(data)[0]
    
    return "Attack 🚨" if prediction == 1 else "Normal ✅"

print("CyberGuard AI detector is ready ✅")

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1 = f1_score(y_test, pred)

metrics = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Score": [accuracy, precision, recall, f1]
})

metrics["Score"] = metrics["Score"].round(4)

display(metrics)

plt.figure(figsize=(8, 5))

plt.bar(metrics["Metric"], metrics["Score"])

plt.title("CyberGuard AI Model Performance")
plt.xlabel("Metric")
plt.ylabel("Score")
plt.ylim(0, 1)

for i, value in enumerate(metrics["Score"]):
    plt.text(i, value + 0.02, f"{value:.2f}", ha="center")

plt.tight_layout()
plt.show()

print("CYBERGUARD AI — INTRUSION DETECTION")
print("=" * 45)
print("Dataset:", len(df), "records")
print("Features used:", len(features))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Accuracy:", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall:", round(recall * 100, 2), "%")
print("F1 Score:", round(f1 * 100, 2), "%")
print("Model: Random Forest")
print("Status: AI detector ready ✅")

