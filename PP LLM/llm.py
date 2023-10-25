import pandas as pd
import numpy as np
import pickle
from gpt import MultiLabelGPTClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("./test_set_2023.csv")
df = df.replace(np.nan, '')

df["All Labels"] = df["labels"].astype(str) + "," + df["labels.1"].astype(str) + "," + df["labels.2"].astype(str) + "," + df["labels.3"].astype(str)

df = df.drop(columns=["labels", "labels.1", "labels.2", "labels.3"])

X = [sentence for sentence in df["sentence"].tolist()]
y = [[label for label in labels.split(",") if label] for labels in df["All Labels"].tolist()]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# # --- Fine tune model and pickle it --- USE IF FIRST TIME
'''
clf = MultiLabelGPTClassifier(
    base_model = "gpt-3.5-turbo-0613",
    n_epochs = None,
    max_labels = 4,
    openai_key="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"
)

clf.fit(X_train, y_train)
with open('model.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)
'''
# # --- --- --- --- --- --- --- --- ---

# # --- Unpickle model --- USE IF ALREADY PICKLED
# '''
with open('model.pkl', 'rb') as model_file:
    clf = pickle.load(model_file)
# '''
# # --- --- --- --- --- --- --- --- ---

total = 0
correct = 0
additional = 0
labels = clf.predict(X_test)
for i in range(len(y_test)):
    for label in labels[i]:
        total += 1
        if label in y_test[i]:
            correct += 1
        elif len(y_test[i]) != len(labels[i]):
            additional += abs(len(y_test[i]) - len(labels[i]))

print(total, correct, additional)
print((correct / total) * 100)