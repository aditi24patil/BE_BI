import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data={
    'Marks':[90,85,75,60,40,30],
    'StudyHours':[5,4,3,2,1,1],
    'Result':[1,1,1,1,0,0]
}
df=pd.DataFrame(data)

x=df[['Marks','StudyHours']]
y=df['Result']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print('Accuracy :',accuracy_score(y_test,y_pred))

new_data=[[70,3]]
prediction = model.predict(new_data)
if prediction[0] == 1:
    print('Student has passed !')
else:
    print('Student has failed.')
    
