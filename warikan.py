import streamlit as st
import random

member = []
money = {}
total = 0

st.title("割り勘アプリ")

if st.sidebar.button("アプリを初期化"):
    st.session_state.clear()
    st.rerun()

length = st.number_input("何人で割り勘しますか？", value=2)

for i in range(length):
    member.append(st.text_input(f"{i+1}人目の名前を入力してください"))

for i, name in enumerate(member):
    if name.strip():
        money[name] = st.number_input(f"{name}さんは何円払いましたか？", min_value=0, step=1, value=0, key=f"input_{name}_{i}")
        total = total + money[name]

st.divider()

if st.button("精算結果を表示する"):
    ave = total//length

    for name in member:
        money[name] = money[name] - ave

    if total%length != 0:
        hasuu = total % length
        selected = random.sample(member, k = hasuu)
        for name in selected:
            money[name] -= 1

    while money:
        name_max = max(money, key = money.get)
        name_min = min(money, key = money.get)

        if (money[name_max] == 0) and (money[name_min] == 0):
            break

        if money[name_max] + money[name_min] >= 0:
            st.success(f"{name_min} => {name_max} {-money[name_min]} 円")
            money[name_max] += money[name_min]
            del money[name_min]
        else:
            st.success(f"{name_min} => {name_max} {money[name_max]} 円")
            money[name_min] += money[name_max]
            del money[name_max]  
    
    st.balloons()    


