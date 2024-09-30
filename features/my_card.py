import streamlit as st


# title : descript 쓰는곳
def container_text(streamlit_st, _title, _descript):
    _container = streamlit_st.container(border=False)
    title, descript = _container.columns([2.2, 9])
    title.write(_title)
    descript.write(_descript)


# 프로필 카드 안 내용
def my_card(st):
    card_container = st.container(border=True)
    col1, col2, col3 = card_container.columns([0.5, 1.0, 0.1])

    col1.image(
        "images/circle_profile.png",
        caption="Decembaek",
        width=130,
        # use_column_width="always",
    )
    col1.subheader("")
    # col1.subheader("Decembaek")

    col2.subheader("백승규 Seunggyu Baek")
    col2.write("경력 1년 Python 개발자")

    # title, descript = col2.columns([2.2, 9])
    container_text(col2, "Email :", "tmdrbpp123@gmail.com")
    container_text(
        col2,
        "SKill :",
        "Python, Django, deploy, Streamlit, Docker, linux, React, Js, OpenCV",
    )
    container_text(col2, "DevTool :", "PyCharm, vscode, Git, xcode, cursor")

    # github, python, blog, _ = col2.columns([4, 4, 4, 1])
    # github.image(
    #     "images/github.png",
    #     caption="github",
    #     width=50,
    # )
    # python.image(
    #     "images/django.png",
    #     caption="python",
    #     width=50,
    # )
    # github.link_button(
    #     "Github",
    #     "https://github.com/decembaek",
    #     help="깃허브 이동",
    #     type="primary",
    # )
    # instar.link_button(
    #     "Instagram",
    #     "https://www.instagram.com/_decembaek",
    #     help="인스타 이동",
    #     type="primary",
    # )

    # blog.link_button(
    #     "Blog",
    #     "https://wingyu-story.tistory.com/",
    #     help="블로그 이동",
    #     type="secondary",
    # )
