import streamlit as st
import time
 
st.set_page_config(page_title="Website", page_icon="🌐")
 
st.markdown("""
    <style>
        .fool-container {
            text-align: center;
            margin-top: 80px;
        }
        .emoji-big {
            font-size: 100px;
            display: block;
            animation: bounce 1s infinite alternate;
        }
        .title-text {
            font-size: 64px;
            font-weight: 900;
            background: linear-gradient(135deg, #ff4b4b, #ff914d, #ffcc00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: block;
            animation: bounce 1s infinite alternate;
        }
        .subtitle-emoji {
            font-size: 60px;
            display: block;
            margin-top: 10px;
        }
        .subtitle-text {
            font-size: 32px;
            font-weight: 700;
            color: #7f3fbf;
            display: block;
            margin-top: 10px;
            animation: shake 0.5s infinite;
        }
        @keyframes bounce {
            from { transform: translateY(0px); }
            to   { transform: translateY(-15px); }
        }
        @keyframes shake {
            0%   { transform: rotate(-3deg); }
            50%  { transform: rotate(3deg); }
            100% { transform: rotate(-3deg); }
        }
    </style>
""", unsafe_allow_html=True)
 
# Slow spinner — 8 seconds of suspense 😈
with st.spinner("Loading something very important... 🤔"):
    time.sleep(8)
 
# Extra troll messages while progress crawls 🐢
messages = [
    "Almost there... hang tight! 😅",
    "Still loading... please wait 🙏",
    "Just a few more seconds... 😬",
    "Wow this is taking a while... 😳",
    "Any moment now... we promise! 🤞",
    "Seriously almost done... maybe 😶",
    "Ok we lied, still loading... 😂",
]
 
progress = st.progress(0, text=messages[0])
for i in range(1, 101):
    time.sleep(0.12)   # 0.12s per step = ~12 seconds total 🐢
    msg = messages[min(i // 15, len(messages) - 1)]
    progress.progress(i, text=f"{msg}  {i}%")
 
progress.empty()
 
# Big reveal
st.markdown("""
    <div class="fool-container">
        <span class="emoji-big">🤡</span>
        <span class="title-text">April Fools' Day</span>
        <span class="subtitle-emoji">🎉🎊🎈</span>
        <span class="subtitle-text">Just wasted 30 seconds of your life 😜🤪😝</span>
    </div>
""", unsafe_allow_html=True)
 
st.balloons()