# Transfer Learning



#### 전이 학습 (Transfer Learning) 개념 및 필요성

- 학습 데이터 부족
  - CNN 모델의 품질을 높이기 위해서는, 즉 임의의 데이터에 대해 정확도는 높이고 오버피팅은 줄이기 위해서는 기본적으로 많은 양의 데이터를 이용하여 학습하여야 함
  - 많은 학습 데이터를 확보하려면 많은 비용과 시간이 소요되기 때문에 현실적으로는 쉽지 않은데, 이러한 데이터가 부족한 어려움을 해결하기 위해 등장한 것이 전이학습
- **전이 학습이란**
  - 아주 큰 데이터 셋, 즉 21,841 부류에 대해 약 1419만 장의 이미지로 구성되어 있는 ImageNet 데이터를 사용해서 학습된 모델의 가중치를 가져와서, 우리가 해결하려는 문제에 맞게 보정해서 사용하는 것을 의미
  - 이때 큰 데이터 셋을 사용해서 훈련된 모델을 **사전 학습 모델(pre-trained model)**이라고 함



#### 사전 학습 모델 구조

```
입력 --> (사전 학습 모델) --> 출력

(사전 학습 모델)
사전 학습된 특징 추출기 -> 사전 학습된 분류기
```

- 사전 학습된 특징 추출기 (pre-trained feature extractor)

  - 특징 추출기(feature extractor)는 컨볼루션 층과 풀링 층의 조합으로 구성되어 있으며 ImageNet 데이터에 대해 이미 학습되어 있음

  - ```
    Conv -> Conv -> Pooling
    ```

    - 특징 추출기의 출력 데이터를 **bottleneck** 또는 feature vector 등으로 지칭함

- 사전 학습된 분류기 (pre-trained classifier)

  - 분류기(classifier)는 완전 연결 층으로 구성되며 추출된 특징을 입력으로 받아 최종적으로 주어진 이미지에 대한 클래스(정답)을 카테고리 형태로 분류하는 역할 수행

  - ```
    Dense -> Dense -> Dense(softmax) ->
    ```

    - 오버피팅을 줄이기 위해 출력 층 이전의 Dense layer 사이에는 Dropout, BatchNormalization layer 등을 add 할 수 있음



#### 사전 학습 모델 종류

- TensorFlow가 제공하는 pre-trained model 이름과 크기, ImageNet 데이터에 대한 1순위와 5순위 정확도, 파라미터 개수 및 층의 깊이 등을 나타내고 있음
- 우리가 사용할 데이터 셋에서 어떤 구조의 모델이 최고의 성능을 낼지 모르기 때문에, 다양한 모델을 사용하여 학습시켜보고 결과를 비교해보는 것도 중요!!

![사전 학습 모델 종류](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225132351724.png)



#### 파인 튜닝 (fine-tuning)

- 사전 학습 모델의 가중치를 미세하게 조정하는 기법
- 새롭게 분류하려는 데이터의 종류와 전체 개수를 미리 분석한 후, 그것을 바탕으로 사전 학습 모델 가중치 일부만을 재학습 시키거나 또는 모든 가중치를 처음부터 다시 학습시킬 수 있음
- 파인 튜닝 진행 시 많은 연산량이 필요하므로 일반적으로 CPU보다는 GPU를 많이 사용

![파인 튜닝](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225132645342.png)



#### Transfer Learning 사용법

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225132817121.png)

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225132825381.png)

---



## Cats and Dogs

#### Cats and Dogs 학습 데이터

![1](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225133217523.png)



#### 모델 구축 (pre-trained Xception + User-Defined Classifier)

![2](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225133309949.png)



#### ImageDataGenerator 정의

![3](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225133439188.png)



#### 모델 컴파일 및 학습

![4](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225133552877.png)



#### 손실 및 정확도

![5](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225133639901.png)



#### 테스트 데이터 로드 및 예측

![6](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225133705989.png)

![7](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230225133846618.png)

