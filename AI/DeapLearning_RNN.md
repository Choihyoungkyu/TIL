# DeapLearning_RNN



#### 일반 신경망과 RNN의 차이

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223165149254.png)

1. 은닉층의 출력값을 만들어주는 활성화함수가 'relu'가 아닌 'tanh'를 사용함
2. 은닉층의 출력값이 출력층으로 전달될 뿐만 아니라, 다시 은닉층의 입력값으로도 전달되는 순환구조를 가짐



#### RNN - 순환 신경망 (Recurrent Neural Network)

1. 내부적으로 순환(recurrent) 되는 구조를 이용
2. 순서(sequence)가 있는 데이터를 처리하는데 강점을 가진 신경망

 

#### 순서(sequence)가 있는 데이터

- 문장이나 음성 같은 연속적인 데이터를 말하는데, 이런 데이터는 문장에서 놓여진 위치(순서)에 따라 의미가 달라지는 것을 알 수 있음
- 즉, 현재 데이터 의미를 알기 위해서는 이전에 놓여 있는 과거 데이터도 알고 있어야 함
  - (I work / I google [대명사+동사], at google / at work [전치사+명사])
- RNN은 이러한 과거의 데이터를 알기 위해서
  1. 은닉층 내에 순환(Recurrent) 구조를 이용하여 과거의 데이터를 기억해두고,
  2. 새롭게 입력으로 주어지는 데이터와 은닉층에서 기억하고 있는 과거 데이터를 연결시켜 그 의미를 알아내는 기능을 가지고 있음

#### RNN 동작 원리 - 정성적 분석 (I work at google)

![I work at google](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223165953941.png)

- 매 순환구조마다 이전의 단어들에 의해 영향을 받은 단어가 입력으로 주어짐 -> 순서 관계 비교에 쓰임



#### RNN 동작 원리 - 시간 개념 포함

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223170147004.png)

---



## SimpleRNN

#### SimpleRNN 개요

![](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223170427885.png)



#### 시계열 데이터 기반의 RNN 구조

![시계열 데이터 기반의 RNN 구조](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223170454846.png)



#### SimpleRNN API - `tf.keras.layers.SimpleRNN()`

![SimpleRNN API](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223170816050.png)



#### RNN 개발 프로세스

![RNN 개발 프로세스](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223170852942.png)

- 중요 !
  - 학습 데이터 생성 시 (batch size, time steps, input dims)의 3차원 텐서 구조로 주어져야됨!

---



## SimpleRNN example

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223171316176.png)

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223171352286.png)

![3](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223171536193.png)

![4](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223171617891.png)

![5](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223171629870.png)



#### SimpleRNN 단점 - 장기 의존성 문제(the problems of long-term dependency)

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223171954268.png)



#### SimpleRNN vs LSTM

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223172107923.png)

---



## LSTM

#### LSTM 구조 - 개요

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223172258557.png)

- forget gate
  - 과거의 정보를 얼마나 잊을지 혹은 가져갈지를 계산하는 gate
- input gate
  - 현재의 정보를 과거에 얼마나 반영할지를 계산하는 gate
- output
  - 현재 레이어의 출력값을 계산해주는 gate



#### LSTM 구조 - forget gate

![forget1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223172500858.png)



#### LSTM 구조 - input gate

![input1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223172639604.png)



#### LSTM 구조 - cell state

![cell1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223172749854.png)



#### LSTM 구조 - output gate

![output1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230223172905356.png)

---



## RNN Example - 삼성전자 주가 예상

#### 개발 과정 - 시계열 데이터 분석 및 예측

- 데이터 로드 및 분포 확인
  - `df=pd.read_csv(), df.describe(), df.hist(), plot() 등`
- 데이터 전처리
  - outlier / missing value 확인 후 대체(또는 삭제) 처리
  - 데이터 정규화(normalization) / 표준화(standardization)
  - 딥러닝 학습을 위한 feature column / label column 정의
- 데이터 생성
  - window size 설정 후 feature / label 시계열 데이터 생성
  - 학습 데이터 생성, 이때 입력 데이터는 (batch size, time steps, input dims) 형태의 3차원 텐서로 생성되어야 함
- 순환신경망 모델 구축 및 학습



#### 데이터 로드 및 분포 확인



