# Deep Learning



#### 성능 개선

- **Optimizer** : 최적화
  - 손실 함수를 줄이도록 해주는 것
  - 하이퍼 파라미터(hyper parameter)를 최적화 시켜야 좋은 성능을 보여줌
  - 얼마나 진행할지 결정하는 에포크(Epoch), 내부 노드(뉴런) 수, 일정한 데이터를 버려서 오버피팅(Overfitting, 과적합)이 일어나지 않게 하는 드롭아웃(Dropout) 등등 모델을 생성할 때 수많은 파라미터를 조정하게 되는데 그 중에 가장 드라마틱하고 쉽게 바꿔주는 것이 옵티마이저



#### Optimizer 원리

- 학습 데이터(Train data)셋을 이용하여 모델을 학습할 때 데이터의 실제 결과와 모델이 예측한 결과를 기반으로 잘 줄일 수 있게 만들어주는 역할

![Optimizer종류](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230221092248107.png)



```python
pip install opencv-python numpy matplotlib
```



## CNN (Convolutional Neural Network)

- 인간의 시신경을 모방하여 만든 딥러닝 구조
- Convolution 연산을 이용하여 공간적인 정보를 유지하고, Fully connected Neural Network 대비 연산량을 획기적으로 줄였으며, 이미지 분류에서 좋은 성능을 보임



#### CNN 구조 => 특징 추출기(Feature Extractor) + 분류기(Classifier)

![image-20230223155040348](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223155040348.png)

- 일반적인 컨볼루션 신경망(CNN) 구조는 특징추출기(Feature Extractor)와 분류기(Classifier)가 합쳐져 있는 형태
  - **특징 추출기**는 컨볼루션 레이어와 풀링 레이어의 다양한 조합으로 구성되며, 이미지 데이터의 특징을 추출하고 압축하는 역할 수행
  - **분류기**는 완전연결층인 Dense Layer와 과적합(overfitting)을 방지하기 위한 Dropout Layer 등의 다양한 조합으로 구성되며, 정답을 분류하는 역할 수행



#### TensorFlow CNN API - Conv Layer, Pool Layer

![CNN API](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223155302964.png)



#### TensorFlow CNN API - Flat Layer, Dense Layer, Dropout Layer

![CNN API](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223155411365.png)



#### Convolution (합성곱)

- 두 함수 (f, g)를 이용해서 한 함수(f)의 모양이 나머지 함수 (g)에 의해 모양이 수정된 제 3의 함수 (f * g)를 생성해주는 연산자로 통계, 컴퓨터 비전, 자연어 처리, 이미지 처리, 신호 처리 등 다양한 분야에서 이용됨

![컨볼루션 정의](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223154017852.png)



#### Convolution 연산

![Convolution 연산 과정](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223154111656.png)



#### Convolution층 개요

![Convolution층 개요](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223154410005.png)



#### 패딩 (Padding)

![패딩 사용 이유](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223154552893.png)



#### 컨볼루션 연산을 통한 출력 데이터 크기(shape) 계산

- 입력 데이터 크기 (H, W), 필터 크기 (FH, FW), 패딩 P, 스트라이드 S 일 때 **출력 데이터 크기 (OH, OW)**
- `OH = (H+2P-FH) / S + 1`
- `OW = (W+2P-FW) / S + 1`





---



## MNIST

- 손으로 직접 쓴 흑백의 숫자 (필기체 숫자)들로 이루어진 데이터



#### 딥러닝 아키텍처

- 입력층
  - 입력층에서는 28 x 28 크기를 가지는 2차원 이미지 데이터를 1차원 벡터로 변환해야 함
- 은닉층
  - 일반적으로 1개 이상의 은닉층으로 이루어져 있으며 각각의 은닉층은 내부에 많은 노드(node)로 구성됨
  - 은닉층의 개수와 노드의 개수는 전형적인 **하이퍼 파라미터**로서 학습 데이터와 주어진 환경 그리고 성능 등을 고려하여 개발자 스스로 최적의 값을 찾아야 함
- 출력층
  - 출력층 노드 개수는 정답(label)의 범주와 같은 10개로 설정해야함!



#### 딥러닝 개발 프로세스 (이미지 데이터)

1. 데이터 정의
   - MNIST, Fashion-MNIST, Cifar10과 같은 학습 데이터 셋은 load_data()를 이용하여 불러올 수 있음
2. 데이터 전처리
   - 학습 데이터가 이미지인 경우, 학습 데이터에 대한 정규화(normalization)와 원핫 인코딩(one-hot encoding)과 같은 데이터 전처리(preprocessing)가 필요함
   - 일반적으로 정규화는 MinMax 또는 표준화 알고리즘을 사용하며, 원핫 인코딩은 TensorFlow 2.x에서는 to_categorical() API를 이용하여 수행됨
3. 모델 구축
   - 모델(model)을 생성하고 model.add()를 통해 입력 층, 은닉 층, 출력 층을 구성함
   - 은닉 층 부분은 일반적인 ANN에서는 Dense()를 사용하지만, CNN에서는 Conv2D(), MaxPool2D(), Flatten() 등으로 은닉 층 부분을 구성
4. 모델 컴파일
   - model.compile() API를 이용하여 optimizer, loss function 등을 지정
   - 학습 데이터의 정답이 원핫 인코딩일 경우
     - loss function : `loss='categorical_crossentropy'`
   - 원핫 인코딩이 아닐 경우
     - loss function : `loss='sparse_categorical_crossentropy'`
5. 학습
   - model.fit() API를 이용하여 이미지 데이터에 대한 학습을 진행
6. 모델 평가
   - model.evaluate() API를 이용해 테스트 데이터에 대한 정확도를 측정
   - 혼돈 행렬(confusion matrix)을 사용하면 우리가 구축한 모델(model)의 강점과 약점, 즉 어떤 데이터에 대해서 우리 모델이 혼란스러워 하는지 등을 파악할 수 있음



#### 데이터 전처리 (정규화, 표준화, 원핫 인코딩)

- 정규화 (Normalization)
  - 딥러닝에서 입력 데이터의 상대적 크기에 대한 영향을 줄이기 위해, MinMax 공식을 이용해 모든 데이터 범위를 0 ~ 1 사이의 값으로 변화시키는 과정
  - data_new = (data - Min) / (Max - Min)
- 표준화 (Standardization)
  - 딥러닝 모델이 더 높은 precision을 가질 수 있도록, 데이터 평균(Mean)과 표준편차(Std)를 이용해 특정 범위를 벗어난 데이터는 outlier로 간주하여 제거하는 과정
  - data_new = (data - Mean) / Std
- 원핫 인코딩 (One-Hot Encoding)
  - 정답 개수와 동일한 크기를 가지는 리스트를 만든 후 정답에 해당하는 리스트의 인덱스 값에는1을 넣고, 나머지 인덱스에는 모두 0을 넣어 정답을 표현하는 방식
  - 즉, 리스트에서 가장 큰 값을 가지는 인덱스를 정답으로 인식

---



## CNN Example - MNIST dataset

#### 주의 ! - CNN에서는 입력 데이터를 (높이, 너비, 채널) 형태로 바꿔줘야됨!!

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223155846656.png)

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223160100924.png)

![3](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223160113358.png)

---



## CNN Example - Fashion MNIST

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223160140921.png)

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223160203019.png)

---



## CIFAR-10 CNN Example

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223160516309.png)

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223160738905.png)

---



## CNN 성능 향상 (오버피팅 ⬇, 정확도⬆)

#### 더 많은 레이어(layer) 쌓기

- 컨볼루션 레이어가 중첩된 더 깊은 구조가 될수록 성능은 크게 개선됨
- AlexNet(2012, 8 layers), VGGNet(2014, 19 layers), GoogleLeNet(2014, 22 layers), ResNet(2015, 152 layers), ...



#### 이미지 데이터 보강 (Image Data Argumentation)

- 딥러닝에서는 많은 학습 데이터를 사용하면 성능을 개선시킬 수 있음
- 기존의 (이미지) 데이터가 있을 때, 해당 데이터를 원본으로 해서 다양한 변형(rotate, shear, zoom, shift, horizontal flip, ...)을 주고, 이렇게 생성된 데이터를 원본 학습 데이터에 포함시켜 수많은 학습 데이터를 확보 가능



#### 높은 해상도(High Resolution) 학습 데이터 확보

- 동일한 CNN 구조라면, 상대적으로 높은 해상도의 학습데이터를 통해서 성능을 개선시킬 수 있음
  - [CIFAR 10] 32 x 32 <=> [ImageNet image] 469 x 387



#### L1 Norm, L2 Norm 등의 가중치 규제(Regularization), Dropout, 배치 정규화(Batch Normalization) 등을 통해 성능 개선 가능

---



## 이미지 데이터 보강 (Image Data Argumentation)

- 원본 이미지에 적절한 변형을 가해서 새로운 데이터를 만들어내는 방식
- 장점
  - 다양한 데이터를 입력시킴으로써 모델을 더욱 견고하게 만들어주기 때문에 더 높은 성능 기대
  - CNN 모델을 학습시키기에 수집된 데이터가 적은 경우, 강력한 힘을 발휘



#### 케라스 -> 이미지 데이터 보강을 위한 ImageDataGenerator 제공

- `rotation_range, width_shift_range, height_shift_range, rescale, shear_range, horizontal_flip` 등이 있음
- ImageDataGenerator를 사용할 경우 flow(), flow_from_directory() 등의 함수를 통해 이미지 데이터 보강 가능

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223161952188.png)



#### flow() 함수 예제

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223163717053.png)

- JpegImageFile 타입을 `img_to_array` 함수로 타입을 바꿔줘야됨!

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223163829719.png)

- 주의 ! - 3차원의 텐서들을 4차원의 텐서로 바꿔줘야함

![3](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223163952486.png)



#### flow_from_directory() 함수 예제

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223164024735.png)

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223164124577.png)

---



## 성능 향상을 위한 CNN 구조 및 데이터

![0](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223164352825.png)

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223164542294.png)

- 원본 데이터의 훼손을 막기 위해 `copy()`를 사용

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223164639000.png)

![3](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223164744879.png)

![4](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223164813870.png)

![5](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223164837266.png)

- 데이터 보강 & layer 강화를 통해 정확도를 높이고 robust한 모델을 만들 수 있음

