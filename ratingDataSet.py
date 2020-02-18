from scipy import spatial
userDictionary = {'user1': [2, 4, 3, 1, 4], 'user2': [5, 1, 2, 4, 3], 'user3': [3, 2, 3, 5, 4], 'user4': [1, 5, 2, 2, 1], 'user5': [2, 1, 4, 2, 5]
}

# result = 1 - spatial.distance.cosine(user1, user2);
# userDictionary = [user1, user2, user3, user4, user5]
from numpy import dot
from numpy.linalg import norm

usersList = list(userDictionary.keys())
x = dict()
for i in range(len(userDictionary)):
    for j in range(i+1, len(userDictionary)):
        print(usersList[i], usersList[j], end=' ')
        cos_sim = round(dot(userDictionary[usersList[i]], userDictionary[usersList[j]]) / (norm(userDictionary[usersList[i]]) * norm(userDictionary[usersList[j]])), 4)
        x[usersList[i] + ' ' + usersList[j]] = cos_sim
        print(' = ', cos_sim)

print(x)
y = sorted(x, key=x.get, reverse=True)
print(y)
print([x[i] for i in y])