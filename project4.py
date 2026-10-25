# PASS OR FAIL PREDICTOR

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

lgr_X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]]) # hours studied
lgr_y = np.array([0,0,0,0,1,1,1,1]) #0-fail, 1-pass

lgr_model = LogisticRegression()
lgr_model.fit(lgr_X,lgr_y)
# print(lgr_model.predict([[4.5]])) # will student with 4.5h pass?

kX, _ = make_blobs(n_samples=100, centers=3, random_state=3)
kmeans_model = KMeans(n_clusters=3).fit(kX)

plt.subplot(1, 2, 1)
plt.scatter(lgr_X, lgr_y, color="red")
plt.plot(lgr_X, lgr_model.predict(lgr_X), color="blue")
plt.xlabel("Hours studied")
plt.ylabel("Pass or fail score")

plt.subplot(1,2,2)
sns.scatterplot(x=kX[:,0], y=kX[:,1], hue=kmeans_model.labels_)
plt.tight_layout()
plt.show()

