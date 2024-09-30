import os
import requests
from datetime import datetime
import base64
import json

import streamlit as st
from PIL import Image

# from dotenv import load_dotenv

# # load .env
# load_dotenv()

# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_API_KEY = st.secrets["general"]["OPENAI_API_KEY"]

if __name__ == "__main__":

    # st.sidebar.page_link("Profile.py", label="Home", icon="🏠")
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

    st.title("이미지 평가 AI 🤖")

    image_file = st.file_uploader(
        "이미지 파일을 업로드 해주세요. 이미지는 따로 저장되지 않습니다",
        type=["png", "jpg", "jpeg"],
    )
    if image_file is not None:

        # st.write(type(image_file))

        image = Image.open(image_file)
        # 이미지를 화면에 표시
        st.image(image, caption="업로드된 이미지", use_column_width=True)

        with st.spinner("이미지 분석 중 ..."):

            # 이미지 데이터를 바이트 형태로 변환합니다.
            image_bytes = image_file.getvalue()
            # 이미지를 base64로 인코딩합니다.
            encoded_image = base64.b64encode(image_bytes).decode("utf-8")

            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"""너는 사진 전문가야. 냉정하게 판단해야 해.
                                            이 그림을 한글로 설명해줘. 잘 찍은 건 잘 찍었다, 못 찍은 건 못 찍었다고 설명해줘.
                                            100점을 만점으로 이미지에 점수를 매겨줘.
                                            """,
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{encoded_image}"
                                },
                            },
                        ],
                    },
                ],
                "functions": [
                    {
                        "name": "set_image_evaluation",
                        "description": "이미지에 대한 평가를 설정합니다.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "total_description": {
                                    "type": "string",
                                    "description": "사진에 대한 전체적인 평가",
                                },
                                "bad_description": {
                                    "type": "string",
                                    "description": "사진에 대한 부정적인 평가",
                                },
                                "good_description": {
                                    "type": "string",
                                    "description": "사진에 대한 긍정적인 평가",
                                },
                                "score": {
                                    "type": "integer",
                                    "description": "사진에 대한 전체적인 점수 (0 ~ 100 사이의 숫자)",
                                },
                            },
                            "required": ["total_description", "score"],
                        },
                    }
                ],
                "function_call": {"name": "set_image_evaluation"},
            }

            headers = {
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            }

            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
            )

            result = response.json()
            # result
            content = result["choices"][0]["message"]["function_call"]["arguments"]

            content = json.loads(content)
            # content
            # print(content)
            # json.loads(content)
            # print(type(content))
            try:
                st.write("전체적 평가")
                st.caption(content["total_description"])
            except:
                pass

            try:
                st.write("사진 점수")
                st.caption(content["score"])
            except:
                pass

            try:
                st.write("긍적적 평가")
                st.caption(content["good_description"])
            except:
                pass

            try:
                st.write("부정적 평가")
                st.caption(content["bad_description"])
            except:
                pass

        st.success("분석이 완료 되었습니다", icon="✅")
