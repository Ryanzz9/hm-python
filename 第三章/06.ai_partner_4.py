import json
from datetime import datetime

import streamlit as st
import os
from openai import OpenAI
from pandas.core import col

# 设置页面的配置项

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="😈",

    #布局
    layout = "wide",

    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}

)

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#生成会话标识的函数

def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# 保存会话信息函数

def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
       session_data = {
           "nick_name": st.session_state.nick_name,
           "nature": st.session_state.nature,
           "current_session": st.session_state.current_session,
           "messages": st.session_state.messages
        }

    # 如何session目录不存在就创建
       if not os.path.exists("sessions"):
          os.mkdir("sessions")

        # 保存会话数据到文件

       with open(f"sessions/{st.session_state.current_session}.json", "w",encoding="utf-8") as f:
            json.dump(session_data,f,ensure_ascii=False,indent=2)


# 加载所有的会话列表信息
def load_all_sessions():
    session_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    return session_list

# 加载指定的会话

def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            # 读取会话数据
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
    except Exception as e:
        st.error(f"加载会话失败！ {session_name}: {e}")

# 大标题

st.title("AI智能伴侣")

#展示聊天信息


# Logo
st.logo("./20260716170506_152_27.jpg")

#系统提示词
#system_prompt = "你是一名非常可爱的AI助理，你的名字叫小暖暖，请你使用温柔可爱的语气回答用户的问题"

system_prompt = """
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：规则：
        1. 每次只回1条消息
        2. 禁止任何场景或状态描述性文字
        3. 匹配用户的语言
        4. 回复简短，像微信聊天一样
        5. 有需要的话可以用❤🌸等emoji表情
        6. 用符合伴侣性格的方式对话
        7. 回复的内容，要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
"""


# 初始化聊天信息

if "messages" not in st.session_state:
    st.session_state.messages = []

# 昵称

if "nick_name" not in st.session_state:
    st.session_state.nick_name= "小悦悦"


# 性格
if "nature" not in st.session_state:
    st.session_state.nature= "活泼开朗的南方姑娘"

# 会话标识
if "current_session" not in st.session_state:
   st.session_state.current_session = generate_session_id()

st.text(f"会话名称： {st.session_state.current_session}")



# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # elif message["role"] == "assistant":
    #     st.chat_message("assistant").write(message["content"])


# 左侧侧边栏

# st.sidebar.subheader("伴侣信息")
# nick_name = st.sidebar.text_input("昵称")

# 左侧的侧边栏 - with：streamlit中上下文管理器

with st.sidebar:
    #会话信息
    st.subheader("AI控制面板")
    # 新建会话按钮
    if st.button("新建会话",width="stretch",icon="✏"):
       save_session()


        # 2.创建新的会话
       if st.session_state.messages: #如果聊天消息非空，True ；否则False
          st.session_state.messages = []
          st.session_state.current_session = generate_session_id()
          save_session()
          st.rerun() # 重新运行页面

    # 历史会话
    st.text("历史会话")
    session_list = load_all_sessions()
    for session in session_list:
        col1,col2 = st.columns([5,1])
        with col1:
            #加载会话信息
            if st.button(session,width="stretch",icon="📄",key=f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
               load_session(session)
               st.rerun() # 重新运行页面
        with col2:
            #删除会话
            if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):
               pass
        # st.button(session,width="stretch",icon="📄")
        # st
# 每个按钮都得有一个唯一标识
#·第二个按钮: st.button(""， …)所有删除按钮都用空字符串"”作为label，Streamlit 会认为它们是“相同元素”，从而报错StreamlitDuplicateElementId.

    st.subheader("伴侣信息")
    # 昵称输入框
    nick_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    #性格输入框
    nature = st.text_area("性格",placeholder="请输入性格",value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature




#消息输入框


prompt = st.chat_input("请输入问题")

if prompt: # 字符串会自动转换为布尔值，如果字符串非空，则为True；“” 否则为False
    # "user" or "assistant"
    st.chat_message("user").write(prompt)
    print("调用AI大模型，提示词",prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})


    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
    )


    # print("大模型返回的结果：",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # 输出大模型返回的结果（流式输出的解析方式）
    response_message = st.empty() # 创建一个空的组件，用于展示大模型返回的结果

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})


    # 大模型相应完就保存会话信息到文件
    save_session()