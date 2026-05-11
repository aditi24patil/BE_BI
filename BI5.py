#Perform the data classification algorithm using any Classification algorithm.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df=pd.read_csv(r"C:\\Users\\Public\\Iris.csv")

x=df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=df['Species']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression(max_iter=200)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print('Accuracy Score :',accuracy_score(y_test,y_pred))

sample=[[5.2,3.4,1.5,0.2]]
prediction=model.predict(sample)
print('Predicted Species :',prediction[0])
