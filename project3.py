from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

X = [[2], [3], [5], [7], [10], [12], [15], [20]] # distance
y = [4,5,7,9,12,14,17,22] # fare

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=3)
model =LinearRegression()
model.fit(X_train, y_train)
print(f"Predict fare for 30km: {model.predict([[30]])[0]:.2f} GHc") # in this code, the prediction will be printed inside a numpy array and so the [0] is used to get the value from the array. The prediction will be printed with 2 decimal places.
print(f"Score: {model.score(X_test, y_test)}")

# plot the result
plt.scatter(X, y, color="orange")
plt.plot(X, model.predict(X), color="blue")
plt.xlabel("Distance (km)")
plt.ylabel("fare ghc")
plt.title("Distance vs Fare")
plt.show()