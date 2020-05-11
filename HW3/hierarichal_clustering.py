import matplotlib.pyplot as plt
import numpy as np
def generate_n_primes(N):
    primes  = []
    chkthis = 2
    while len(primes) < N:
        ptest    = [chkthis for i in primes if chkthis%i == 0]
        primes  += [] if ptest else [chkthis]
        chkthis += 1
    return primes

prime_numbers = generate_n_primes(20)
done_set = []

for i in range(0, len(prime_numbers)):
    if prime_numbers[i] in done_set:
        continue
    if len(done_set) < 1:
        points = np.array([[prime_numbers[i], prime_numbers[i+1]]])
    else :
        # b = np.array([[prime_numbers[i], prime_numbers[i + 1]]])
        points = np.concatenate((points, [[prime_numbers[i], prime_numbers[i + 1]]]))
    plt.scatter(prime_numbers[i], prime_numbers[i+1])

    plt.ylabel('some numbers')
    done_set.append(prime_numbers[i])
    done_set.append(prime_numbers[i+1])

first_centroid = np.array([points[0], points[1]])
print(first_centroid)
plt.show()

first_last_centroid = np.array([points[0], points[len(points)-1]])
print(first_last_centroid)
from sklearn.cluster import KMeans

# For first and second points as centroid :
for i in range(1, 5):

    kmeans = KMeans(n_clusters=2, random_state=0, init=first_centroid, max_iter=i).fit(points)
    plt.scatter(points[:, 0], points[:, 1], c=kmeans.labels_, cmap='rainbow')
    plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color="black")
    print("Centroid for iteration no.", i, ":\n" , kmeans.cluster_centers_)
    plt.show()

# For first and last points as centroid :
for i in range(1, 5):

    kmeans = KMeans(n_clusters=2, random_state=0, init=first_last_centroid, max_iter=i).fit(points)
    plt.scatter(points[:, 0], points[:, 1], c=kmeans.labels_, cmap='rainbow')
    plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color="black")
    print("Centroid for iteration no.", i, ":\n" , kmeans.cluster_centers_)
    plt.show()