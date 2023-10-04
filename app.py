import streamlit as st

# 타이틀 및 간단한 설명
st.title("Welcome to Minji's Portfolio")

# 상단 메뉴
menu = st.selectbox("Menu", [ "Education", "Work Experience", "Technical Stack", "Projects","Identity"])



# Identity 섹션
if menu == "Identity":
    st.header("Identity")
    st.write("■ I - Innovation")
    st.write("■ D - Diligent")
    st.write("■ E - Essence")
    st.write("■ N - Uniqueness")
    st.write("■ T - Trendsetter")
    st.write("■ I - Implementation")
    st.write("■ T - Trustworthiness")
    st.write("■ Y - Yes")

# Education 섹션
elif menu == "Education":
    st.header("Education")

    st.subheader("Highest Education_Master's Degree")
    st.write("Sookmyung Women's University - Master of Big Data Analysis Convergence")
    st.write("The Master of Big Data Analysis Convergence program at Sookmyung Women's University is a comprehensive program that focuses on advanced data analysis techniques, artificial intelligence, and data management. This program equips students with the skills to extract valuable insights from large datasets and make data-driven decisions, contributing to the rapidly growing field of data science.")
    st.write("   ■ Big Data Visualization Seminar")
    st.write("   ■ Artificial Intelligence Seminar")
    st.write("   ■ Big Data Planning")
    st.write("   ■ Python Programming for Big Data")
    st.write("   ■ Personal Information Protection Act")
    st.write("   ■ PBL(Project-Based Learning)")
    st.write("   ■ Big Data and Media Seminar")
    st.write("   ■ Database")
    st.write("   ■ Business Analytics")
    st.write("   ■ Deep Learning Programming")

# Work Experience 섹션
elif menu == "Work Experience":
    st.header("Work Experience")

    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

    st.write("Experience 3: 숙명여자대학교 Intellectual Property Human Resources Development (IP HRD)")
    st.write("   ■  Job Position: 데이터 분석, 연구 및 개발")
    st.write("   ■  IP HRD는 특허청에서 지원하는 AI 특허 교육 프로젝트")

    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

    st.write("Experience 2: 농협중앙회")
    st.write("   ■  Job Position: 신용, 예수금 데이터 분석, 통계")
    st.write("   ■  농협중앙회에서 여신과 수신 업무를 담당하면서 금융 데이터 분석 및 효율적인 의사 결정을 지원")

    st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

    st.write("Experience 1: 삼성서울병원")
    st.write("   ■  Job Position: 수납 및 CS 담당")

# Technical Stack 섹션
elif menu == "Technical Stack":
    st.header("Technical Stack")

    st.subheader("Languages")
    st.write('  "Python"')
    st.write('  "HTML"')
    st.write('  "Markdown"')
    st.write('  "SQL"')

    st.subheader("Algorithms & Techniques")
    st.write('"Supervised Learning"')
    st.write('  "Random Forest Classifier"')

    st.write('"Unsupervised Learning"')
    st.write('   "Latent Dirichlet Allocation"')
    st.write('   "K-Means Clustering"')

    st.write('"Natural Language Processing"')
    st.write('  "BERT"')
    st.write('  "GPT"')

    st.subheader("Visualization")
    st.write('   "pandas"')
    st.write('   "matplotlib"')
    st.write('   "seaborn"')

    st.subheader('"Machine Learning & NLP')
    st.write('  "Scikit-learn"')
    st.write('  "transformers"')
    st.write('  "PyTorch"')
    st.write('  "Korpora"')
    st.write('  "gensim"')

    st.write('"Text Preprocessing & Web Scraping"')
    st.write('  "tokenizers"')
    st.write('  "re"')
    st.write('  "Web Crawling"')

    st.subheader("Data Processing & Distributed Storage")
    st.write('  "Hadoop"')

    st.subheader("Web Applications & Dashboarding")
    st.write('   "Streamlit"')

    st.subheader("Data Retrieval & Integration")
    st.write('  "API Integration"')

    st.subheader("Data Exchange Formats")
    st.write('  "JSON"')

    st.subheader("Development Environments & Tools")
    st.write('  "Google Colab"')
    st.write('  "Jupyter"')
    st.write('  "PyCharm"')

########## CSS를 사용하여 배경 이미지 변경하기 ##########

st.markdown(
    """
    <style>
    body {
        background-color: rgba(135, 206, 235, 0.5); /* 반투명한 블루 색상 설정 */
        color: white; /* 글자 색상 */
        font-size: 15px; /* 글자 크기 */
        font-family: Playfair Display, sans-serif; /* 글꼴 설정 */
        text-align: left; /* 텍스트 정렬 (왼쪽) */
    }
    </style>
    """,
    unsafe_allow_html=True
)