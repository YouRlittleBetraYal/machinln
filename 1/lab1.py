import random, sklearn.cluster as cl, statistics as st

num_of_elements = 100
range_limit = 50
num_of_clusters = 6

array = []
for i in range(0,num_of_elements):
    array.append([random.randint(0,range_limit),random.randint(0,range_limit)])
print(array,"\n")

array2 = cl.KMeans(n_clusters=num_of_clusters,random_state=0).fit(array)
labels = array2.labels_
centers = array2.cluster_centers_
iter = array2.n_iter_
print("labels:",labels,"\n")
print("center coordinates:",centers,"\n")
print("KMeans iterations:",iter,"\n")

for i in range(0,num_of_clusters):
    temp = []
    temp2 = []
    temp3 = []
    for w in range(0,len(labels)):
        if(labels[w]==i):
            temp.append(array[w])
            temp2.append(array[w][0])
            temp3.append(array[w][1])
    print("\nCluster"+str(i)+":",temp)
    print("Min X:",min(temp2))
    print("Max X:",max(temp2))
    print("Median X:",st.median(temp2))
    print("Min Y:",min(temp3))
    print("Max Y:",max(temp3))
    print("Median Y:",st.median(temp3))
