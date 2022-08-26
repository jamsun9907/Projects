# Section 1 Project

- **제출 가이드**
    
    ![Untitled](Section%201%20Project%20d9afbc3879e84051975966617bf21b0b/Untitled.png)
    
    ![Untitled](Section%201%20Project%20d9afbc3879e84051975966617bf21b0b/Untitled%201.png)
    
- *Refferences*
    
    [Python 입문자의 Data Science(Kaggle) 도전](https://www.slideshare.net/ParkMijeong/pycon-korea-2017-python-data-sciencekaggle) : 데이터 분석 프로세스 확인 가능
    
    ****[Data Science Process: 7 Steps explained with a Comprehensive Case Study](https://www.embedded-robotics.com/data-science-process/#data-science-process-a-step-by-step-approach)** : 데이터 분석 단계 케이스 스터디로 정리되어 있음
    
    **[VGCharts](https://www.vgchartz.com/)** : Project data 출처
    

# Due date : 29일 월요일 5시

---

## Plan (3 days)

### 📌 To-do list

- [x]  회사, 상황 가정하기
- [x]  데이터 분석 단계 프래임 워크 가져오기
    - [x]  [Process](https://www.embedded-robotics.com/data-science-process/#data-science-process-a-step-by-step-approach)
        - [x]  공부해서 정리하기(필요한 부분 까지만)
- [x]  데이터 전처리
    - [x]  품질의 문제
        - [x]  결측값 처리
        - [x]  중복값 처리
            - [x]  이름 중복…
    - [x]  구조의 문제
        - [x]  feature engineering
        - [x]  Sales 데이터 지역 나누어 long form만들기
            - [x]  Sales, Sales Region 으로 나누기
- [ ]  EDA (역대)
    - [x]  Descriptive statistic
        - [x]  장르에 따른 평균 판매량 및 시장점유율
        - [x]  지역별 장르 선호도
    - [ ]  시각화
        - [x]  Platform 별 역대 흐름 (라인그래프)
        - [ ]  누적 차트로 시간에 따른 플랫폼
        - [x]  지역별 Platform 선호도
        - [x]  장르 별 역대 흐름 (라인차트)
        - [ ]  전체 기간 장르 barchart(점유율)
            - [ ]  5년 단위로 쪼개서 상위 3개 장르 보여주기
    - [ ]  지역 별 선호도 - ANOVA
        - [ ]  장르
        - [ ]  플랫폼
- [ ]  EDA 최근 추세
    - [ ]  시각화
    - [ ]  가설 수립
    - [ ]  모델 결정

- [ ]  Data canvas 채우기 [Data canvas](https://www.notion.so/Data-canvas-70b615c762f2443bb897a5357a287a0b)

### Timeline (Actual)

**24th**

11:00 - 1:00 | 데이터 분석 계획 수립

---

1:00 - 2:00 | Lunch time

---

2:00 - 9:00 | Data processing & Wranggling

---

**25th**

11:00 - 3:30 | EDA & Feature engineering

3:30 - 5:30| EDA & 간단한 시각화

5:30 - 9:30 | Data processing again…

9:30 - 11:00 | Data modeling - K-means

25일 Tomorrow : EDA 및 EDA시각화, 가설 수립

26일 : 가설 검증 및 클러스터링 기법 활용. 스토리 텔링 기획

29일 : 발표 자료 작성 및 영상 제작

1. **회사, 상황 가정하기**

콘솔게임사, 좋은 IP를 가지고 있고, 기존 RPG 게임이 대박이 나서 해당 IP를 가지고 메인 시리즈(이미 개발중) 외에 짧은 텀에 낼 수 있는 가벼운 서브 게임을 다음 분기(2022.09)에 기획할 예정. 

*게임사의 가정은 진행하면서 더 추가하기*

1. **문제 정의**
- [ ]  다음 분기의 게임 장르는 어떤 것으로 골라야 하는가?
- [ ]  플랫폼은? → 개발팀 전달
- [ ]  해당 장르, 플랫폼에서 상위를 차지하는 주요 게임사 및 게임은 무엇인가? → 기획팀 레퍼런스 전달용
- [ ]  어느 지역을 우선적으로 출시해야하는가? → localization 우선 순위 결정을 위해

1. 가설 수립
    1. 지역에 따라서 선호하는 게임 장르가 다를 것이다. → 지역이 4개이므로 ANOVA 분석 사용
    2. 연도별 게임 트랜드 → x 축 Year, y 축 total, 연도로 장르로 데이터 집계
        1. 5년 단위로 쪼개서 상위 3개 게임 장르에 대해 보여주기 
        2. → 누적 막대그래프로 보여주기 : x축 시계열, y축 누적분포
        3. 연도 / Total 출고량 데이터 스캐터로 찍어서 
    
    c. 출고량이 높은 게임에 대한 분석 및 시각화 프로세스
    
    - 출고량 상위 5% 게임에 대해 분석하기. (기술 통계 추가)