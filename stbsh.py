import streamlit as st  # streamlit 라이브러리 임포트

# 타이틀 텍스트 출력
st.title('홍익대학교 산업·데이터공학과 📚')

# 텍스트 출력
st.write('# 1. 산업·데이터공학과 소개')

# Markdown 문법으로 작성된 문장 출력
st.markdown(
    '''
    ## 교육목표
    - 산업·데이터공학과는 4차 산업 혁명시대의 핵심 자원인 산업 빅데이터에 대해 다양한 정량적인 데이터 분석 기법을 사용하여 산업 시스템의 분석, 설계 및 운영의 효율화와 최적화를 도모하는 학문이다. 전통적인 산업공학의 적용 대상인 생산/제조, 품질, 물류 시스템, 인간공학, 금융/공공/의료/헬스 서비스, HCI 등 첨단 시스템을 대상으로, 최근 4차 산업혁명 시대에 필수적인, 빅데이터, 데이터사이언스, 통계, 데이터마이닝, 머신러닝, 최적화, 인공지능 등의 교육을 강화하는 것을 교육 목표로 하고 있다.
    

    ## 역사
    - 산업·데이터공학과는 기존의 산업공학과를 뿌리로 두고 있다. 산업공학은 산업혁명 이후 1910년대에 대량생산시스템의 도입과 더불어 태동하였다. 프레드릭 테일러라는 미국의 기계공학자이자 산업공학자는 ‘과학적 관리의 원칙’에서 시간연구와 작업연구를 통하여 작업에 관한 과학적인 분석을 시도하였다. 과학경영으로 대표되는 테일러리즘은 제조업 전반에 확산되며 생산성 향상에 크게 이바지 하였고, 이것이 현재의 산업·데이터공학이 되었다.

    ## 현재와 미래
    - 산업·데이터공학은 타 학문과의 결합에 매우 자유로운 성향을 가지고 있는 산업공학에 뿌리를 두고 있어 연계성이 매우 뛰어나다. 뿐만 아니라 기존의 산업공학의 학문에 데이터사이언스, 머신러닝, 인공지능 등의 학문 교육을 강화한 전공이므로 21세기 새로운 인재상에 부합하는 교육이 될 것이다.
    '''
    )

# DataFrame 출력
import pandas as pd  # pandas 라이브러리 임포트

st.write('# 2. 졸업생 취업통계')  # 텍스트 출력
df = pd.DataFrame({  # DataFrame 생성
    '최근 5년간 진출 직무': [{'품질 보증/경영/관리/전략/기획,소프트웨어 개발/관리 등'}],
    '최근 5년간 진출 회사': [{'삼성전자,LG전자,게임개발회사,한국전력기술,현대하이닉스,CJ 등'}]
},index=['목록'])

st.dataframe(df)  # DataFrame 출력

# 그래프 출력
import numpy as np
st.write('# 3.산업공학과 취업현황')
df1 = pd.DataFrame({
    '전체':[{72.6}],
    '남':[{74.5}],
    '여':[{67.6}]
}, index=['%'])
st.dataframe(df1)

df2 =pd.DataFrame({'첫직장 월평균임금':[12.5,25.6,22,20.2,19.7,100]}, 
                  index=['0~150만원(%)','151~200만원(%)','201~250만원(%)','251~300만원(%)','301만원 이상(%)','합계(%)'])

st.dataframe(df2)

st.markdown(
    '''
    ### 참고문헌
    - [산업·데이터공학과 홈페이지](https://ie.hongik.ac.kr/dept/index.html)
    ''')
st.set_page_config(     # 페이지 설정
    page_title="Hello", # 페이지 Tab의 타이틀
    page_icon="👋",     # 페이지 Tab의 아이콘
    layout="wide",  # 페이지 레이아웃: centered, wide
    initial_sidebar_state="expanded", # 사이드바 초기 상태: auto, collapsed, expanded
    menu_items={        # 페이지 오른쪽 상부의 메뉴에 추가할 메뉴 항목: Get help, Report a bug, About
        'Get help': 'https://docs.streamlit.io',
        'About': "# 이것은 헤더. \n - 마크다운 문법 지원 \n - [네이버](https://naver.com)"
    }
)

st.write("# 파이썬 프로그래밍 수업에 오신 것을 환영합니다.! 👋")   # st.write()를 이용한 헤더 작성

st.sidebar.success("위의 목록에서 Demo를 선택하시오.")  # 사이드바에 success 메시지 출력

st.markdown(   # st.markdown()을 이용한 본문 작성
    """
    **파이썬 프로그래밍** 수업을 통해 _웹 어플리케이션_을 만들어 봅시다.
    **👈 왼쪽의 사이드바**에서 원하는 데모를 선택하세요.
    
    ### Streamlit에 대하여 더 알고싶으신가요?
    - [홈페이지](https://streamlit.io)
    - [공식문서](https://docs.streamlit.io)
    - [커뮤니티 포럼](https://discuss.streamlit.io)

    ### 더 복잡한 데모를 보고 싶으신가요?
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
