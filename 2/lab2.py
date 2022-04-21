import random,time, numpy as np

N = 300
M = 300
eps = 1e-7

  # A_ROWS, B_ROWS, B_COLUMNS
def func(matrix_A,matrix_B,A_rows,B_columns,sum_of):
    result = []
    for x in range(0,A_rows):
        row = []
        for y in range(0,B_columns):
            element = 0
            for z in range(0,sum_of):
                element+=matrix_A[x][z]*matrix_B[z][y]
            row.append(element)
        result.append(row)
    return result

PY_vector_N = []
PY_vector_M = []
for i in range(0,N):
    PY_vector_N.append([round(random.random(),7)])             
print("PY_vector_N:\n",PY_vector_N,"\n")            
temp = []
for i in range(0,M):
    temp.append(round(random.random(),7))
PY_vector_M.append(temp)                                                 
print("PY_vector_M:\n",PY_vector_M,"\n")
NumPY_vector_N = np.array(PY_vector_N)
NumPY_vector_M = np.array(PY_vector_M)   
print("NumPY_vector_N:\n",NumPY_vector_N,"\n")
print("NumPY_vector_M:\n",NumPY_vector_M,"\n")

start = time.time()                                          
PY_N_M = func(PY_vector_N,PY_vector_M,N,M,1)                      
end = time.time()
time11 = round(end-start,7)
start = time.time()
NumPY_N_M = np.matmul(NumPY_vector_N,NumPY_vector_M)
end = time.time()
time12 = round(end-start,7)

start = time.time()
PY_N_M_N = func(PY_N_M,PY_vector_N,N,1,M)         
end = time.time()
time21 = round(end-start,7)
start = time.time()
NumPY_N_M_N = np.matmul(NumPY_N_M,NumPY_vector_N)
end = time.time()
time22 = round(end-start,7)

start = time.time()
PY_M_N_M = func(PY_vector_M,PY_N_M,1,M,N)         
end = time.time()
time31 = round(end-start,7)
start = time.time()
NumPY_M_N_M = np.matmul(NumPY_vector_M,NumPY_N_M)
end = time.time()
time32 = round(end-start,7)

start = time.time()
PY_N_M_N_M = func(PY_N_M,PY_N_M,N,M,N)  
end = time.time()
time41 = round(end-start,7)
start = time.time()
NumPY_N_M_N_M = np.matmul(NumPY_N_M,NumPY_N_M)
end = time.time()
time42 = round(end-start,7)

print("Test1:\nPy_N_M[0][0]",PY_N_M[0][0]," NumPY_N_M[0][0]",NumPY_N_M[0][0])
assert PY_N_M[0][0] - NumPY_N_M[0][0] < eps
print("Passed")
print("Test2:\nPy_N_M_N[0][0]",PY_N_M[0][0]," NumPY_N_M_N[0][0]",NumPY_N_M[0][0])
assert PY_N_M_N[0][0] - NumPY_N_M_N[0][0] < eps
print("Passed")
print("Test3:\nPy_M_N_M[0][0]",PY_N_M[0][0]," NumPY_M_N_M[0][0]",NumPY_N_M[0][0])
assert PY_M_N_M[0][0] - NumPY_M_N_M[0][0] < eps
print("Passed")
print("Test4:\nPy_N_M_N_M[0][0]",PY_N_M[0][0]," NumPY_N_M_N_M[0][0]",NumPY_N_M[0][0])
assert PY_N_M_N_M[0][0] - NumPY_N_M_N_M[0][0] < eps
print("Passed")

print("PY N_M time: ",time11, " NumPy N_M time: ",time12)
print("PY (N_M)_N time: ",time21, " NumPy (N_M)_N time: ",time22)
print("PY M_(N_M) time: ",time31, " NumPy M_(N_M) time: ",time32)
print("PY (N_M)_(N_M) time: ",time41, " NumPy (N_M)_(N_M) time: ",time42)