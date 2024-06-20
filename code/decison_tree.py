import pyshark
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score

def extract_features(pcap_file):
    try:
        capture = pyshark.FileCapture(pcap_file)
    except FileNotFoundError:
        print(f"File not found: {pcap_file}")
        return None

    features = []
    
    for packet in capture:
        feature = []
        # Example features: length, protocol type, etc.
        feature.append(int(packet.length))
        if hasattr(packet, 'ip'):
            feature.append(int(packet.ip.proto))
        else:
            feature.append(0)
        
        # Add more features as required
        features.append(feature)
    
    capture.close()
    return np.array(features)

# Example usage
pcap_file = 'C://Users//Asus//Desktop//fyp_azfar//attack//sqli//sqli.pcapng'
features = extract_features(pcap_file)

if features is not None:
    # Example labels (this should be derived from your data)
    labels = np.random.randint(0, 2, len(features))  # Binary classification: 0 or 1

    # Prepare DataFrame
    df = pd.DataFrame(features, columns=["Length", "Protocol"])
    df["Label"] = labels

    # Split dataset into training and testing sets
    X = df[["Length", "Protocol"]]
    y = df["Label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Decision Tree model
    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, y_train)

    # Predict on the test set
    y_pred = dt.predict(X_test)

    # Calculate accuracy, F1 score, and recall
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"F1 Score: {f1}")
    print(f"Recall: {recall}")
else:
    print("Feature extraction failed due to file not found.")
