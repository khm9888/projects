import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report


df2=pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/test.csv",index_col=0)
print("df2")
print(df2)

def get_clf_eval(y_test, pred,target_names):
    confusion = confusion_matrix(y_test, pred)
    print('confusion matrix')
    print(confusion)
    accuracy = accuracy_score(y_test, pred)
    # precision = precision_score(y_test, pred)
    # recall = recall_score(y_test, pred)
    # print(f'acc : {accuracy}')
    print(classification_report(y_test, pred, target_names=target_names))

# target_names = ['man', 'cat', 'dog']
target_names = ['0' , '1',  '2', '3', '4', '5']

# y_true = [2, 0, 2, 2, 0, 1]
# y_pred = [0, 0, 2, 2, 0, 2]

# print(confusion_matrix(y_true, y_pred))
# print(classification_report(y_true, y_pred, target_names=target_names))

# get_clf_eval(y_true,y_pred,target_names)

# get_clf_eval(df2["true"],df2["predict"],target_names)