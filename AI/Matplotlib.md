# Matplotlib

---



**Scatter Plot**

```python
import numpy as np
import matplotlib.pyplot as plt

# 주피터 노트북을 사용하는 경우 노트북 내부에 그림 표시
# %matplotlib inline

# x_data, y_data 생성
x_data = np.random.rand(100)
y_data = np.random.rand(100)

plt.title('scatter plot')
plt.grid()
plt.scatter(x_data, y_data, color='b', marker='o')
plt.show()
```



**Line Plot**

```python
import numpy as np
import matplotlib.pyplot as plt

x_data = [ x for x in range(-5, 5) ]
y_data = [ y*y for y in range(-5, 5) ]

plt.title('line plot')
plt.grid()
plt.plot(x_data, y_data, color='b')
plt.show()
```

