# Example of getting neighbors for an instance
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
def K_NN_DS_ALGO(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15,arg16) :
		data = pd.read_excel('divorce.xlsx') 
		#print(data.columns)
		#print(data.head(86))
		#data["Atr1"].hist(bins=15) histtogramme de 	Art1
		correlation_matrix = data.corr()
		#print(correlation_matrix["Class"] ," rayeb")

		#X = data.drop("Class", axis=1)

		X = data[["Atr1","Atr3","Atr5","Atr6","Atr13","Atr17","Atr19","Atr23","Atr29","Atr31","Atr33","Atr41","Atr46","Atr48","Atr51","Atr53"]].values
		Y = data["Class"].values
		new_data_point = np.array([ arg1 , arg2 , arg3 , arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16 ])

		distances = np.linalg.norm(X - new_data_point, axis=1)

		k=3
		nearest_neighbor_ids = distances.argsort()[:k]
		print(nearest_neighbor_ids)
		nearest_neighbor_rings = Y[nearest_neighbor_ids]
		print(nearest_neighbor_rings)
		m,div =0,0
		for i in nearest_neighbor_rings :
			if i == 1 : 
				m += 1
			else :
				div += 1
		return m>div  
#print(m," ",div)

#print(K_NN_DS(3,4,2,1,1))
'''
from sklearn.neighbors import KNeighborsRegressor
knn_model = KNeighborsRegressor(n_neighbors=3)
knn_model.fit(X, Y)

from sklearn.metrics import mean_squared_error
from math import sqrt
train_preds = knn_model.predict(X)
mse = mean_squared_error(Y, train_preds)
rmse = sqrt(mse)
print(rmse)
'''