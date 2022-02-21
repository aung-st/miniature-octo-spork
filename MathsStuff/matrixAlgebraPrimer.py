import numpy as np 

#column vectors
x =  np.array([[2],[3],[5]])
y = np.array([[3],[0],[4]])

#different ways of doing x^t * y
print(x.T@y)
print(np.dot(x.T,y))
print(np.matmul(x.T,y))


x_1 = np.array([[4,1,0,2],[2,0,1,3]])
x_2 = np.array([[3],[0],[5],[1]])

#get dim
print(x_1.shape,x_2.shape)

print(np.matmul(x_1,x_2))

#column or row form will yield same result
print(np.linalg.norm(np.array([[2],[4],[3],[1]])))
print(np.linalg.norm(np.array([2,4,3,1])))

#find unit vector pointing in same direction
u = np.array([[5],[0],[0]])
u_normalised = u / np.linalg.norm(u)
print(u_normalised)

#slicing to get submatrix
B = np.array([[3,2,0],[0,4,2],[5,0,1],[1,3,4]])

print(B[1:3,1])
print(B[1:3,1].shape)

#naive dot implementation
def dot(v1,v2):
    if len(v1) != len(v2):
        raise ValueError("vectors are not the same length")
    
    return sum(v1_i * v2_i for v1_i,v2_i in zip(v1,v2))
print(dot(x,y))

data = np.array([[17,9],[21,10],[12,17]])
print(data)

#compute sum of data as a column vector by multiplying by a column vector
def transform(data):
    return (np.dot(data,np.array([[1],[1]])))
print(transform(data))

data = np.array([[17,9,1],[21,10,1],[12,17,1]])
thetas = np.array([[4],[5],[-100]])
print(data @ thetas)

