import pandas as pd
import numpy as np
import pickle
from gpt_few_shot_clf import MultiLabelFewShotGPTClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("./test_set_2023.csv")
df = df.replace(np.nan, '')

df["All Labels"] = df["labels"].astype(str) + "," + df["labels.1"].astype(str) + "," + df["labels.2"].astype(str) + "," + df["labels.3"].astype(str)

df = df.drop(columns=["labels", "labels.1", "labels.2", "labels.3"])
# print(len(df))

df = df[:(int(len(df) / 1.85714285714))]
extra_test = df[(int(len(df) / 1.85714285714)):]
ExtraXTest = [sentence for sentence in extra_test["sentence"].tolist()]
ExtraYTest = [[label for label in labels.split(",") if label] for labels in extra_test["All Labels"].tolist()]

X = [sentence for sentence in df["sentence"].tolist()]
y = [[label for label in labels.split(",") if label] for labels in df["All Labels"].tolist()]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# # --- Fine tune model and pickle it --- USE IF FIRST TIME
# '''
clf = MultiLabelFewShotGPTClassifier(max_labels=4, openai_model="gpt-3.5-turbo", openai_key="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")

clf.fit(X_train, y_train)
with open('mlc.pkl', 'wb') as model_file:
    pickle.dump(clf, model_file)
# '''
# # --- --- --- --- --- --- --- --- ---

# # --- Unpickle model --- USE IF ALREADY PICKLED
'''
with open('mlc.pkl', 'rb') as model_file:
    clf = pickle.load(model_file)
'''
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

total = 0
correct = 0
additional = 0
labels = clf.predict(ExtraXTest)
for i in range(len(ExtraYTest)):
    for label in labels[i]:
        total += 1
        if label in ExtraYTest[i]:
            correct += 1
        elif len(ExtraYTest[i]) != len(labels[i]):
            additional += abs(len(ExtraYTest[i]) - len(labels[i]))

print(total, correct, additional)
print((correct / total) * 100)

