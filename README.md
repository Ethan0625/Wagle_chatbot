# 오픈도메인 챗봇 프로젝트(Wagle)

## 프로젝트 요약

이 프로젝트는 모두의 연구소 산하 교육기관 [AIFFEL](https://aiffel.io/)과 서울시와 서울 산업진흥원이 주관한 [SSAC](https://ssac.seoul.kr/main/index.jsp)이 연계한 AIFFELXSSAC교육 과정에서 <U>**team Wagle이 진행한 챗봇 프로젝트**</U> 입니다.  
  
SKT에서 개발한 KoGPT2를 기반으로 정희원님이 제작하신 챗봇 모델 <U>**KoGPT2-chatbot을 활용하여 챗봇을 구성**</U>하였습니다.  
  
챗봇모델을 직접 제작하는 것 보다 학습에 필요한 데이터셋을 정제하고 <U>**기존에 제작된 챗봇모델을 활용하여 양질의 결과를 얻는 것을 목표**</U>로 하였습니다.  
  
<U>**학습에 사용된 데이터는 아래의 Dataset부분을 참조**</U>하시기 바랍니다.


## 구성원  
  
박병학 (팀리딩, 모델 리서치 및 학습) [![GitHub-Mark-32px](https://user-images.githubusercontent.com/48716219/102974622-31c3b680-4542-11eb-815d-70efcdeb2e75.png)](https://github.com/Ethan0625)[![nb30](https://user-images.githubusercontent.com/48716219/102975150-f37ac700-4542-11eb-9606-9414ed89f0de.png)](https://ethan-library.tistory.com/)

박상효 (데이터 분석 및 정제, 웹개발) [![GitHub-Mark-32px](https://user-images.githubusercontent.com/48716219/102974622-31c3b680-4542-11eb-815d-70efcdeb2e75.png)](https://github.com/ixxxxu/) [![nb30](https://user-images.githubusercontent.com/48716219/102975150-f37ac700-4542-11eb-9606-9414ed89f0de.png)](https://velog.io/@ixxxxuxo)

이창호 (데이터 분석 및 수집) [![GitHub-Mark-32px](https://user-images.githubusercontent.com/48716219/102974622-31c3b680-4542-11eb-815d-70efcdeb2e75.png)](https://github.com/philosucker)[![nb30](https://user-images.githubusercontent.com/48716219/102975150-f37ac700-4542-11eb-9606-9414ed89f0de.png)](https://questionet.tistory.com/)

임진호 (데이터 분석 및 수집) [![GitHub-Mark-32px](https://user-images.githubusercontent.com/48716219/102974622-31c3b680-4542-11eb-815d-70efcdeb2e75.png)](https://github.com/Jake1152)[![nb30](https://user-images.githubusercontent.com/48716219/102975150-f37ac700-4542-11eb-9606-9414ed89f0de.png)](https://jake1152.tistory.com/)

장인학 (모델 리서치 및 학습) [![nb30](https://user-images.githubusercontent.com/48716219/102975150-f37ac700-4542-11eb-9606-9414ed89f0de.png)](https://jjanhan.tistory.com/)


## Project milestone  
  
1) 사전회의 (21.05.03 ~ 21.05.07)
    - 프로젝트 방향결정
    - 마감기한 전까지 챗봇 관련 모델을 새로만드는 것은 어렵다고 판단
    - 차후에 수집된 데이터를 정제하여 양질의 데이터셋으로 만들고, 이를 만들어진 모델에 학습시켜 양질의 결과물을 얻기로 결정

2) 데이터 수집 및 정제 (21.05.10 ~ 21.05.28)
    - 국립국어원, AI HUB, 깃허브 등의 플랫폼을 활용하여 데이터 수집
    - 데이터 확인결과, KoGPT2기반의 챗봇 모델에 그대로 적용하기에는 어렵다고 판단
    - 멀티 턴기반의 데이터를 싱글턴 기반의 데이터로 변환 및 정제
    - 정제 과정상세  
        (1) 불용어 처리  
            -> 기본적인 불용어처리 + 고유명사를 대명사로 변환(자체 불용어 사전 제작)
            
        (2) 멀티턴 기반 대화를 싱글턴 기반의 데이터로 정제  
            -> 두명의 화자가 대화를 여러번 주고받는 형태의 데이터를 한번 주고받는 형태의 싱글턴으로 변환
        
        (3) (2)과정을 거치면서 맥락이 무너진 데이터 확인 및 수정
        
3) 핵심모델 리서치 및 연구 (21.05.10 ~ 21.05.28)
    - 데이터를 정제하는 과정에서 바로 사용 가능한 챗봇모델 리서치 및 연구
    - 초기에는 KcBert를 활용하여 챗봇모델을 제작하려 하였지만 자연어 생성에 특화된 KoGPT2를 사용하기로 결정
    - 최적의 파라미터를 찾기위해 기능 추가(검증 과정, 시각화 과정 등)
    
4) 모델 학습 (21.05.10 ~ 21.06.18)

5) 웹구현 (21.06.14 ~ 21.06.18)


## 사용한 기술 스택  
- Git
- Python, Jupyter Notebook
- Pytorch
- Pandas
- Google Cloud, Ainize


## Dataset

|데이터 이름|출처|링크|
|:---:|:---:|:---:|
|SDRW 일상대화 말뭉치|국립국어원|[LINK](https://corpus.korean.go.kr/)|
|SERW 구어 말뭉치|국립국어원|[LINK](https://corpus.korean.go.kr/)|
|SBRW 구어 말뭉치|국립국어원|[LINK](https://corpus.korean.go.kr/)|
|송영숙님 말뭉치|깃허브|[LINK](https://github.com/songys/Chatbot_data)|
|웰니스 대화 스크립트 데이터셋|AI HUB|[LINK](https://aihub.or.kr/keti_data_board/language_intelligence)|
|트위터 대화 시나리오|AI HUB|[LINK](https://aihub.or.kr/keti_data_board/language_intelligence)|
|한국어 연속적 대화 데이터 셋|AI HUB|[LINK](https://aihub.or.kr/keti_data_board/language_intelligence)|

## How to Use (in terminel)
```
!git clone https://github.com/Ethan0625/Wagle_chatbot
!cd Wagle_chatbot
!pip3 install -r requirements.txt
!CUDA_VISIBLE_DEVICES=0 python train_torch.py --gpus 1 --chat
```


## Demo
- 준비중


## Deep Learning Model

KoGPT2(GPT2 기반 Pretrained model)
![image](https://user-images.githubusercontent.com/70437384/120886945-5d87b400-c62b-11eb-94ac-ce987ed12a0b.png)
Open AI에서 2015년 발표한 GPT이후에 2019년에 공개된 GPT2모델을 기반으로 만들어진 KoGPT2 모델입니다.
SKT-AI에서 한국어 위키 백과, 뉴스, 모두의 말뭉치 v1.0, 청와대 국민청원 등의 데이터로 학습된 모델입니다.

## Reference
- [KoGPT2](https://github.com/SKT-AI/KoGPT2#demo)
- [KoGPT2-chatbot](https://github.com/haven-jeon/KoGPT2-chatbot)