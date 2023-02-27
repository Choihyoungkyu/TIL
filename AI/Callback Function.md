# Callback

#### Callback 개념

1. 특정한 상황에서 실행되는 함수를 시스템에 먼저 등록
2. 해당 상황이 발생했을 때 등록되어 있는 함수가 실행됨
3. 시스템에서의 결과를 통해 개발자는 등록된 콜백 함수가 실행된 것을 알 수 있음



#### TensorFlow Callback Function

- 모델의 학습 방향, 저장 시점, 학습 정지 시점 등에 관한 상황을 모니터링 하기 위해 주로 사용됨
  - 학습 도중에 학습률(learning rate)을 변화시키거나, 일정시간이 지나도 검증 데이터(validation data), 손실 값(val_loss)이 개선되지 않으면 학습을 멈추게 하는 등의 작업
    1. ReduceLROnPlateau : 학습 중에 학습률을 변화시킴
    2. ModelCheckpoint : 모델의 가중치(weight)값을 중간에 저장할 수 있게 해줌
    3. EarlyStopping : 모델 성능 지표가 일정 시간 동안 개선되지 않을 때 조기 종료 가능



#### 학습률 조정 - ReduceLROnPlateau

- 모델의 성능 개선이 없을 경우, 학습률(Learning Rate)를 조절해서 모델의 개선을 유도하는 콜백함수로서 factor 파라미터를 통해 학습률을 조정 (factor < 1.0)

```python
from tensorflow.keras.callbacks import ReduceLROnPlateau

reduceLR = ReduceLROnPlateau(monitor='val_loss',	# val_loss 기준으로 callback 호출
                            factor = 0.5,			# callback 호출시 학습률을 1/2로 줄임
                            patience=5,			# epoch 5 동안 개선되지 않으면 callback 호출
                            verbose=1)				# 로그 출력

hist = model.fit(x_train, t_train,
                epochs=50, validation_split=0.2,
                callbacks=[reduceLR])
```



#### 모델 가중치 중간 저장 - ModelCheckpoint

- 모델의 학습 도중에 조건을 만족했을 때 현재의 가중치(weight)를 중간 저장함
  - 학습시간이 오래 걸린다면, 혹시 중간에 memory overflow나 crash가 나더라도 다시 가중치를 불러와서 학습을 이어나갈 수 있기 때문에, 이러한 중간 저장 기능은 학습시간을 단축시킬 수 있음

```python
from tensorflow.keras.callbacks import ModelCheckpoint

file_path = './modelchpoint_test.h5'			# 저장할 file path

checkpoint = ModelCheckpoint(file_path,			# 저장할 file path
                            monitor='val_loss',	# val_loss 값이 개선되었을 때 호출
                            verbose=1,			# log 출력
                            save_best_only=True,# best 값만 저장
                            mode='auto')		# auto는 자동으로 best를 찾음

hist = model.fit(x_train, t_train,
                epochs=50, validation_split=0.2,
                callbacks=[checkpoint])
```



#### 학습 조기 종료 - EarlyStopping

- 모델 성능 지표가, 우리가 설정한 epoch 동안 개선되지 않을 때 조기 종료 가능
  - 일반적으로 EarlyStopping과 ModelCheckpoint 조합을 통해서, 개선되지 않는 학습에 대한 조기 종료를 실행하고, ModelCheckpoint로부터 가장 best model을 다시 로드하여 학습을 재게하는 경우가 일반적

```python
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

file_path = './modelchpoint_test.h5'			# 저장할 file path

checkpoint = ModelCheckpoint(file_path,			# 저장할 file path
                            monitor='val_loss',	# val_loss 값이 개선되었을 때 호출
                            verbose=1,			# log 출력
                            save_best_only=True,# best 값만 저장
                            mode='auto')		# auto는 자동으로 best를 찾음

stopping = EarlyStopping(monitor='val_loss',	# 관찰대상은 val_loss
                        patience=5)				# 5 epoch 동안 개선되지 않으면 조기종료

hist = model.fit(x_train, t_train,
                epochs=50, validation_split=0.2,
                callbacks=[checkpoint, stopping])
```

