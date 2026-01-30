import streamlit as st
import pandas as pd
from itertools import combinations
from collections import Counter

st.set_page_config(page_title="Mega-Sena", page_icon="🎯", layout="wide")

st.title("🎯 Analisador de Repetições – Mega-Sena")
st.markdown("Use direto no celular 📱")

arquivo = st.file_uploader("📂 Envie o CSV da Mega-Sena", type="csv")

if arquivo:
    df = pd.read_csv(arquivo)
    numeros = df.iloc[:, 1:7].values.tolist()

    st.subheader("📊 Frequência dos números")
    todos = [n for jogo in numeros for n in jogo]
    freq = Counter(todos)
    st.dataframe(
        pd.DataFrame(freq.items(), columns=["Número", "Quantidade"])
        .sort_values("Quantidade", ascending=False),
        use_container_width=True
    )

    st.subheader("🔁 Pares mais repetidos")
    pares = []
    for jogo in numeros:
        pares.extend(combinations(sorted(jogo), 2))
    st.dataframe(
        pd.DataFrame(Counter(pares).most_common(15), columns=["Par", "Repetições"]),
        use_container_width=True
    )

    st.subheader("🔂 Trios mais repetidos")
    trios = []
    for jogo in numeros:
        trios.extend(combinations(sorted(jogo), 3))
    st.dataframe(
        pd.DataFrame(Counter(trios).most_common(15), columns=["Trio", "Repetições"]),
        use_container_width=True
    )

    st.subheader("📈 Repetição entre concursos")
    repeticoes = []
    for i in range(1, len(numeros)):
        repetidos = len(set(numeros[i]) & set(numeros[i-1]))
        repeticoes.append({
            "Concurso": f"{i} → {i+1}",
            "Repetidos": repetidos
        })

    st.dataframe(pd.DataFrame(repeticoes), use_container_width=True)
