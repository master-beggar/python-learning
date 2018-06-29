import numpy as np

height = np.round(np.random.normal(1.75,0.20,6000),2)
weight = np.round(np.random.normal(60,14,6000),2)

np_height = np.array(height)
np_weight = np.array(weight)

# bmi = weight/(height^2)

bmi = np_weight / np_height ** 2

print(bmi)

bmi_2 = bmi[bmi > 30]
print(bmi_2)

np_2d = np.array([weight,height,bmi])
print(np_2d.shape)

mean_height = np.mean(np_2d[0,:])
height_weight_cor = np.corrcoef(np_2d[0,:],np_2d[1,:])
std_height = np.std(np_2d[1,:])

np_2d1 = np.column_stack((height,weight))
print(np_2d1.shape)

list1 = np.round(np.random.normal(20,0.5,20),2)
list2 = np.round(np.random.normal(5,0.5,20),2)
list3 = list1 + list2

print(list1)
print(list2)
print(list3)
print("the fib is:",fibo(5))
