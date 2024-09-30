import streamlit as st
from openai import OpenAI

# from dotenv import load_dotenv

import os

from features.my_card import my_card


# load .env
# load_dotenv()

# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# MY_TEXT = os.environ.get("MY_TEXT")
# OPENAI_API_KEY 사용
OPENAI_API_KEY = st.secrets["general"]["OPENAI_API_KEY"]

# MY_TEXT 사용
MY_TEXT = st.secrets["my_text"]["MY_TEXT"]


def project_card(st, title, descript, image_path, github):
    card_container = st.container(border=True)
    card_container.subheader(title)
    card_container.write(descript)


# 카드 생성
def make_card(st, text):
    card_container = st.container(border=True)
    card_container.write(text)


# 💌💾📝


def main():
    st.title("Decembaek Profile")
    st.caption("핸드폰 보단 디스플레이가 큰 PC 환경을 추천 드립니다.")
    # 명함
    my_card(st)

    # 자기소개
    make_card(
        st,
        text="""
                   안녕하세요, Python, JavaScript 개발자 백승규라고 합니다. \n
                   현재 회사 생활하고 있으며, 주업무는 Python 으로 백엔드 서버 또는 인공지능 관련 SW를 제작합니다 \n
                   \n
                   제 프로필에 오신걸 환영합니다 😊
                   """,
    )

    st.header("💬 Chatbot")
    st.caption(
        "저를 대신할 AI 챗봇 입니다. 저에 대해서 물어볼게 있으면 마음껏 물어보세요"
    )
    st.caption(
        "저랑 관련 없는 이야기를 하면 대답을 회피합니다. 대답을 안 해주면 메일 남겨주세요 답변을 추가하겠습니다"
    )
    # 프로젝트 설명
    # make_card(
    #     st,
    #     text="""
    #                     사이드 탭을 열면 이미지 AI가 있습니다 \n
    #                     나의 이미지를 업로드 해서 점수를 매겨보세요
    #                     """,
    # )

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "안녕하세요, 개발자 Decembaek Bot 입니다.",
            },
            {"role": "assistant", "content": "뭐든지 물어보세요"},
            {
                "role": "system",
                "content": MY_TEXT,
            },
        ]

    for msg in st.session_state.messages:
        if not msg["role"] == "system":
            st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():

        client = OpenAI(api_key=OPENAI_API_KEY)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=st.session_state.messages
        )
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)


if __name__ == "__main__":
    st.set_page_config(
        page_title="Decembaek_library",
        page_icon="images/Original.png",
        initial_sidebar_state="expanded",
        layout="centered",
        menu_items={
            "About": "# 오직 Python으로만 만들었습니다. skill : Streamlit ",
        },
    )
    with st.sidebar:
        st.subheader("Contact")
        st.page_link(
            "https://www.instagram.com/_decembaek/", label="Instagram", icon="💌"
        )
        st.page_link("https://github.com/decembaek", label="Github", icon="💾")
        st.page_link("https://wingyu-story.tistory.com/", label="Blog", icon="📝")

    main()
