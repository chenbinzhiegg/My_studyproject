
import numpy as np

a=np.array([-2,2])
b=np.array([2,2])

#内积
ab_1=np.inner(a,b)
#根据夹角余弦计算
ab_2=np.linalg.norm(a)*np.linalg.norm(b)*np.cos(np.pi/2)

print(ab_1,ab_2)