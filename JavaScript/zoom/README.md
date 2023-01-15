# Noom

Zoom Clone using NodeJS, WebRTC and Websockets.

#### WebRTC 공식 사이트(MDN)
https://developer.mozilla.org/en-US/docs/Web/API/

#### 서버 실행
- npm run dev

#### 설치 진행
1. npm i nodemon -D
2. npm i @babel/core @babel/cli @babel/node @babel/preset-env -D
3. npm i express
4. npm i pug

#### RTCPeerConnection
- Definition : A WebRTC connection between the local computer and a remote peer.
- Constructor : `RTCPeerConnection()`

#### RTCIceCandidate
- Definition : Internet Connectivity Establishment(인터넷 연결 생성)
- webRTC에 필요한 프로토콜들을 의미
- 멀리 떨어진 장치와 소통할 수 있게 하기 위함
- 다수의 cadidate(후보)들이 각각의 연결에서 제안되고, 서로 동의 하에 하나를 선택하여 소통 방식에 사용

#### 서버 공유
- 설치 : npm i -g localtunnel
- 공유 : npx localtunnel --port 3000

#### STUN 서버
- 공용주소를 알려주는 서버
- 강의에서는 구글에서 제공해주는걸 쓰지만 실제 서비스를 만들 때는 직접 STUN 서버를 만들어야함!!

#### createDataChannel()
- 데이터 채널을 만들어서 각종 데이터들을 서버를 거치지 않고 넘길 수 있음

#### WebRTC 단점
- 사람이 많아지면 느려짐 (Mesh 방식)
    - SFU(Selective Forwarding Unit) : 모두로부터 스트림을 받고, 서버가 그 스트림들을 압축.
        - 이 서버는 누가 호스트인지, 말하고 있는지, 스크린을 공유하고 있는지, 발표를 하는지 다 앎
        - 아무것도 안하는 사람의 사양을 낮춰서 성능을 끌어올려줌