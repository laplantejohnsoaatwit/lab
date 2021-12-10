from joblib import dump, load
from sklearn.naive_bayes import GaussianNB
import pandas as pd
#read in csv
csv= pd.read_csv('pong_data_cp.csv')

#train x with ball
train_x = csv[['ball_x','ball_y']]
print(train_x.shape)

#train y
train_y = csv['paddle_y']
print(train_y.shape)
#fit it to a model and save
model = GaussianNB()
model.fit(train_x, train_y)
dump(model, 'mymodel.joblib')