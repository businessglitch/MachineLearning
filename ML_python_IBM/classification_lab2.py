import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree


my_data = pd.read_csv('drug200.csv', delimiter=',')
print(my_data[0:5])

#X  = Feature Matrix data of my_data
#y = response vector (target)

X = my_data[['Age','Sex','BP','Cholesterol', 'Na_to_K']].values
print(X[0:5])

le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])

X[:,1] = le_sex.transform(X[:,1])

le_BP = preprocessing.LabelEncoder()
le_BP.fit(['LOW', 'NORMAL', 'HIGH'])
X[:,2] = le_BP.transform(X[:,2])

le_Chol = preprocessing .LabelEncoder()
le_Chol.fit(['NORMAL','HIGH'])
X[:,3] = le_Chol.transform(X[:,3])

print(X[0:5])

y = my_data["Drug"]

X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=3)

drugTree = DecisionTreeClassifier(criterion="entropy",max_depth=4)
print(drugTree)
drugTree.fit(X_train,y_train)

predTree = drugTree.predict(X_test)

print(predTree[0:5])
print(y_test[0:5])

print("Decision Tree Accuracy: ", metrics.accuracy_score(y_test,predTree))

dot_data = StringIO()
filename = "drugtree.png"
featureNames = my_data.columns[0:5]
targetNames = my_data["Drug"].unique().tolist()
out=tree.export_graphviz(drugTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_train), filled=True,  special_characters=True,rotate=False)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png(filename)

img = mpimg.imread(filename)
plt.figure(figsize=(100,200))
plt.imshow(img,interpolation='nearest')

                           


