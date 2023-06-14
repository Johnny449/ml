from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import random

data_iris = load_iris()
label_target = data_iris.target_names

label_target = data_iris.target_names
print("\n Sample Data from Iris Dataset")
print("*" * 30)
for i in range(5):
    rn = random.randint(0, 120)
    print(data_iris.data[rn], "===>", label_target[data_iris.target[rn]])
   
x = data_iris.data
y = data_iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=1)

print("The Training dataset length : ", len(x_train))
print("The Testing dataset length : ", len(x_test))

try:
    nn = int(input("Enter number of neighbours : "))
    knn = KNeighborsClassifier(nn)
    knn.fit(x_train, y_train)
    print("The Score is : ", knn.score(x_test, y_test))
    test_data = input("Ente Test Data :").split(",")
    for i in range(len(test_data)):
        test_data[i] = float(test_data[i])
    print()
    v = knn.predict([test_data])
    print("Predicted outputis :", label_target[v][0])
except Exception as e:
    print("Enter Valid Input...")
    print(e)
