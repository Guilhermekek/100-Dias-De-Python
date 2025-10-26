import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

print(iris)

x = iris.data
y = iris.target

print(f"Dados da variavel x:\n{x}")
print(f"Dados da variavel y:\n{y}")

x_train, x_test,y_train,y_test = train_test_split(x,y, test_size=0.33, random_state=42)

teste = KNeighborsClassifier(n_neighbors=3)

teste.fit(x_train,y_train)

y_saida = teste.predict(x_test)
print(f"O score da saida do modelo de iris foi: {accuracy_score(y_test, y_saida)}")