# Numpy

---

### Index

- **vector / matrix 생성**
- **행렬 곱 (dot product)**
- **broadcast**
- **index / slice / iterator**
- **concatenate**
- **useful function. (loadtxt(), rand(), argmax(), ...)**



---

### 라이브러리 - Numpy

- Numpy는 머신러닝 코드 개발을 할 경우 자주 사용되는 벡터, 행렬 등을 표현하고 연산할 때 반드시 필요한 라이브러리

**numpy** vs **list**

- 머신러닝에서 숫자, 사람, 동물 등의 인식을 하기 위해서는 이미지(image) 데이터를 행렬(matrix)로 변환하는 것이 중요함
- 행렬(matrix)을 나타내기 위해서는 리스트(list)를 사용할 수도 있지만, 행렬 연산이 직관적이지 않고 오류 가능성이 높기 때문에, **행렬 연산을 위해서는 numpy 사용이 필수임**



**Numpy Vector (1차원 배열)**

- 벡터(vector) 생성
  - vector는 `np.array([...])`를 사용하여 생성함 (`import numpy as np`)
  - 머신러닝 코드 구현 시, **연산을 위해서 vector, matrix 등의 형상(shape), 차원(dimension)을 확인하는 것이 필요함**
- 벡터(vector) 산술연산
  - Vector 간 산술연산( +, -, x, / )은 벡터의 각각의 원소에 대해서 행해짐

```python
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# vector A, B 출력
print("A == ", A, ", B == ", B)			# A == [1 2 3], B == [4 5 6]

# vector A, B 형상 출력 => shape
print("A.shape == ", A.shape, ", B.shape == ", B.shape)		# A.shape == (3,), B.shape == (3,)

# vector A, B 차원 출력 => ndim
print("A.ndim == ", A.ndim, ", B.ndim == ", B.ndim)		# A.ndim == 1, B.ndim == 1
```

```python
# vector 산술연산
print(A + B)	# [5 7 9]
print(A - B)	# [-3 -3 -3]
print(A * B)	# [4 10 18]
print(A / B)	# [5 7 9]
```



**Numpy Matrix (행렬)**

- 행렬(matrix) 생성
  - matrix는 vector와 마찬가지로 `np.array([ [...], [...], [...], ...])`를 사용하여 생성함 (`import numpy as np`)
- **형 변환(reshape)**
  - vector를 matrix로 변경하거나 matrix를 다른 형상의 matrix로 변경하기 위해서는 `reshape()`을 사용하여 행렬의 shape을 변경하여야 함

```python
A = np.array([[1, 2, 3], [4, 5, 6]])

print(A.shape)		# (2, 3)
print(A.ndim)			# 2
```

```python
C = np.array([1, 2, 3])

print(C.shape)		# (3,)

C = C.reshape(1, 3)

print(C.shape)		# (1, 3)
```

```python
D = np.array([[1, 2, 3], [4, 5, 6]])
D = D.reshape(3, 2)
print(D)					# [[1 2] 
									#	 [3 4] 
  								#  [5 6]]
```



**행렬 곱(dot product, `•`)**

- A 행렬과 B 행렬의 행렬 곱(dot product)는 `np.dot(A, B)`로 나타내며, 행렬 A의 열 벡터와 B 행렬의 행 벡터가 같아야 함.
- 만약 같지 않다면 **reshape 또는 전치행렬(transpose) 등을 사용하여 형 변환을 한 후에 행렬 곱을 실행해야 함**

```python
A = np.array([ [1, 2, 3], [4, 5, 6] ])							# 2X3 행렬
B = np.array([ [-1, -2], [-3, -4], [-5, -6] ])			# 3X2 행렬

# (2X3) dot product (3X2) == (2X2) 행렬
C = np.dot(A, B)		# 행렬 곱 수행

# matrix A, B 형상 출력 => shape
print(A.shape, B.shape, C.shape)										# (2, 3), (3, 2), (2, 2)
print(C)																						# [[-22 -28]
																										#  [-49 -64]]
```

- 행렬 곱은 행렬의 원소 개수가 같아야만 계산할 수 있는 사칙연산의 한계를 벗어나게 해주기 때문에 중요함!!
  1. 행렬 곱 조건을 만족하는 다양한 크기의 행렬을 연속으로 만들고
  2. 행렬 곱을 연속으로 계산하면서
  3. 결과값을 만들 수 있기 때문에 머신러닝과 이미지 프로세싱 분야에서 자주 사용됨
- ex) `(64 x 64) • (64 x 256) • (256 x 512) • (512 x 64) • (64 x 10) = (64 x 10)`



**Broadcast**

- 행렬의 사칙연산은 기본적으로 두 개의 행렬 크기가 같은 경우에만 수행할 수 있음
- **numpy에서는 크기가 다른 두 행렬간에도 사칙연산( +, -, x, / )을 할 수 있는데 이를 브로드캐스트(broadcast)라고 지칭함**
  - **즉, 차원이 작은 쪽이 큰 쪽의 행 단위로 반복적으로 크기를 맞춘 후 계산**

```python
A = np.array([ [1, 2], [3, 4] ])
b = 5		# broadcast -> [ [5, 5], [5, 5] ]

print(A+b)		# [[6 7]
							#	 [8 9]]
```

```python
C = np.array([ [1, 2], [3, 4] ])
D = np.array([4, 5])		# broadcast -> [ [4, 5], [4, 5] ]

print(C+D)		# [[5 7]
							#  [7 9]]
```



**전치행렬 (Transpose)**

- 어떤 행렬의 전치행렬(transposed matrix)은 원본 행렬의 열은 행으로, 행은 열로 바꾼 것으로서, 원본 행렬을 A라고 하면 전치행렬은 A^T로 나타냄

```python
A = np.array([ [1, 2], [3, 4], [5, 6] ])		# 3X2 행렬
B = A.T																			# A의 전치행렬, 2X3 행렬

print(A.shape, B.shape)											# (3, 2), (2, 3)
print(A)		# [[1 2]
						#  [3 4]
  					#  [5 6]]
    
print(B)		# [[1 3 5]
						#  [2 4 6]]
```

```python
# vector 전치행렬
C = np.array([1, 2, 3, 4, 5])		# vector
D = C.T		# C는 vector이므로 transpose 안됨

E = C.reshape(1, 5)		# 1X5 matrix
F = E.T		# E의 전치행렬

print(C.shape, D.shape)		# (5,), (5,)
print(E.shape, F.shape)		# (1, 5), (5, 1)
print(F)		# [[1]
						#  [2]
  					#  [3]
    				#  [4]
      			#  [5]]
```



**행렬 indexing / slicing**

- 행렬 원소를 명시적(explicit)으로 접근하기 위해서는 리스트(list)에서처럼, 인덱싱 / 슬라이싱 모두 사용가능 함

```python
A = np.array([10, 20, 30, 40, 50, 60]).reshape(3, 2)

print("A.shape == ", A.shape)
print(A)
'''
  A.shape ==  (3, 2)
  [[10 20]
   [30 40]
   [50 60]]
'''

print("A[0, 0] == ", A[0, 0], ", A[0][0] == ", A[0][0])
print("A[2, 1] == ", A[2, 1], ", A[2][1] == ", A[2][1])
'''
  A[0, 0] ==  10 , A[0][0] ==  10
  A[2, 1] ==  60 , A[2][1] ==  60
'''

print("A[0:-1, 1:2] == ", A[0:-1, 1:2])
'''
  A[0:-1, 1:2] == [[20]
                  [40]]
'''

print("A[:, 0] == ", A[:, 0])
'''
	A[:, 0] ==  [10 30 50]
'''
```



**행렬 iterator**

- 명시적(explicit) 인덱싱 / 슬라이싱 이외에, **행렬 모든 원소를 access하는 경우에는 iterator 사용 가능**

```python
A = np.array([ [10, 20, 30], [40, 50, 60] ])

# 행렬 A의 iterator 생성
it = np.nditer(A, flags=['multi_index'], op_flags=['readwrite'])

while not it.finished:
    idx = it.multi_index
    print("current value => ", A[idx])
    it.iternext()
   
'''
  current value =>  10
  current value =>  20
  current value =>  30
  current value =>  40
  current value =>  50
  current value =>  60
'''
```



**Concatenate**

- 행렬에 행(row) 또는 열(column)을 추가하기 위한 `numpy.concatenate(...)`
- **머신러닝의 회귀(regression) 코드 구현시 가중치(weight)와 바이어스(bias)를 별도로 구분하지 않고 하나의 행렬로 취급하기 위한 프로그래밍 구현 기술**

```python
# 행렬에 열과 행 추가
A = np.array([ [10, 20, 30], [40, 50, 60] ])

# A matrix에 행(row)을 추가할 행렬. 1X3로 reshape
# 행을 추가하기 때문에 우선 열을 3열로 만들어야 함
row_add = np.array([70, 80, 90]).reshape(1, 3)

# A matrix에 열(column)을 추가할 행렬. 2X1로 reshape
# 열을 추가하기 때문에 우선 행을 2행으로 만들어야 함
column_add = np.array([1000, 2000]).reshape(2, 1)

# numpy.concatenate에서 axis = 0 -> 행(row) 기준
B = np.concatenate((A, row_add), axis=0)
print(B)
'''
  [[10 20 30]
   [40 50 60]
   [70 80 90]]
'''

# numpy.concatenate에서 axis = 1 -> 열(column) 기준
C = np.concatenate((A, column_add), axis=1)
print(C)
'''
  [[  10   20   30 1000]
   [  40   50   60 2000]]
'''
```



---

### Numpy Useful Function

**numpy.loadtxt(...)**

- seperator로 구분된 파일에서 데이터를 읽기 위한 함수
- **리턴값은 행렬이기 때문에 인덱싱 or 슬라이싱을 이용하여 데이터를 분리할 수 있음**
- **머신러닝 코드에서 입력데이터와 정답데이터를 분리하는 프로그래밍 기법**
- ex) CSV 파일에 25X4 의 데이터를 불러올 때 -> `np.loadtxt("파일이름", delimiter=',')`

```python
loaded_data = np.loadtxt('./data-01.csv', delimiter=',', dtype=np.float32)

x_data = loaded_data[:, 0:-1]
t_data = loaded_data[:, [-1]]

# 데이터 차원 및 shape 확인
print("x_data.ndim = ", x_data.ndim, ", x_data.shape = ", x_data.shape)
print("t_data.ndim = ", t_data.ndim, ", t_data.shape = ", t_data.shape)

# x_data.ndim = 2, x_data.shape = (25, 3)
# t_data.ndim = 2, t_data.shape = (25, 1)
```



**numpy.random.rand(...)**

- 0~1 사이의 값을 임의로 설정해주는 함수
- 무작위 가중치를 줄 때 사용

```python
# 0~1 사이의 random number 발생
random_number1 = np.random.rand(3)
random_number2 = np.random.rand(1, 3)
random_number3 = np.random.rand(3, 1)

print("random_number1 == ", random_number1, "random_number1.shape == ", random_number1.shape)
print("random_number2 == ", random_number2, "random_number2.shape == ", random_number2.shape)
print("random_number3 == ", random_number3, "random_number3.shape == ", random_number3.shape)

'''
  random_number1 ==  [0.28521269 0.00235992 0.92645211],    random_number1.shape ==  (3,)
  random_number2 ==  [[0.27148034 0.80042347 0.81873014]],  random_number2.shape ==  (1, 3)
  random_number3 ==  [[0.72031227]
                      [0.92357193]
                      [0.57148956]],	 											random_number3.shape ==  (3, 1)
'''
```



**numpy.sum(...), numpy.exp(...), numpy.log(...)**

```python
X = np.array([2, 4, 6, 8])

print("np.sum(X) == ", np.sum(X))
print("np.exp(X) == ", np.exp(X))
print("np.log(X) == ", np.log(X))

'''
  np.sum(X) ==  20
  np.exp(X) ==  [   7.3890561    54.59815003  403.42879349 2980.95798704]
  np.log(X) ==  [0.69314718 1.38629436 1.79175947 2.07944154]
'''
```



**numpy.max(...), numpy.min(...), numpy.argmax(...), numpy.argmin(...)**

- `max, min` : 최대값, 최소값 반환
- `argmax, argmin` : 최대값의 인덱스, 최소값의 인덱스 반환
- **Classification을 할 때 중요하게 사용됨 (정답을 찾아낼때)**

```python
X = np.array([ [2, 4, 6], [1, 2, 3], [0, 5, 8] ])

print("np.max(X) == ", np.max(X, axis=0))       # axis=0, 열 기준 -> 같은 열에서 가장 큰 값 모음
print("np.min(X) == ", np.min(X, axis=0))       # axis=0, 열 기준

print("np.max(X) == ", np.max(X, axis=1))       # axis=1, 행 기준
print("np.min(X) == ", np.min(X, axis=1))       # axis=1, 행 기준

print("np.argmax(X) == ", np.argmax(X, axis=0))       # axis=0, 열 기준 -> 같은 열에서 가장 큰 값의 인덱스
print("np.argmin(X) == ", np.argmin(X, axis=0))       # axis=0, 열 기준

print("np.argmax(X) == ", np.argmax(X, axis=1))       # axis=1, 행 기준
print("np.argmin(X) == ", np.argmin(X, axis=1))       # axis=1, 행 기준

'''
  np.max(X) ==  [2 5 8]
  np.min(X) ==  [0 2 3]
  np.max(X) ==  [6 3 8]
  np.min(X) ==  [2 1 0]
  np.argmax(X) ==  [0 2 2]
  np.argmin(X) ==  [2 1 1]
  np.argmax(X) ==  [2 2 2]
  np.argmin(X) ==  [0 0 0]
'''
```



**numpy.ones(...), numpy.zeros(...)**

```python
A = np.ones([3, 3])
print("A.shape == ", A.shape, ", A == ", A)
B = np.zeros([3, 2])
print("B.shape == ", B.shape, ", B == ", B)

'''
  A.shape ==  (3, 3) , A ==  [[1. 1. 1.]
                              [1. 1. 1.]
                              [1. 1. 1.]]
  B.shape ==  (3, 2) , B ==  [[0. 0.]
                              [0. 0.]
                              [0. 0.]]
'''
```

