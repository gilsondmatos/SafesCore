# app/dashboard/web_panel.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
import pandas as pd
import io

from app.report.generator import generate_pdf_report


# Caminho do CSV
csv_path = os.path.join("app", "data", "transacoes_com_score.csv")

st.set_page_config(page_title="SafeScore Dashboard", layout="wide")
st.title("📊 SafeScore - Painel de Risco de Transações On-Chain")

# Carrega o CSV
def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        st.error("Arquivo de transações não encontrado. Execute o main.py primeiro.")
        return pd.DataFrame()

# Aplica cor de fundo com base no score
def highlight_score(val):
    if val >= 70:
        color = '#d4edda'  # verde claro
    elif val >= 40:
        color = '#fff3cd'  # amarelo claro
    else:
        color = '#f8d7da'  # vermelho claro
    return f'background-color: {color}'

# Carregar dados
df = load_data(csv_path)

if not df.empty:
    st.sidebar.header("🔎 Filtros")

    # Filtro por endereço (from ou to)
    enderecos = pd.unique(df[['from', 'to']].values.ravel('K'))
    endereco_selecionado = st.sidebar.selectbox("Filtrar por endereço:", options=["Todos"] + sorted(enderecos.tolist()))

    # Filtro por score
    score_min, score_max = st.sidebar.slider("Filtrar por score:", min_value=0, max_value=100, value=(0, 100))

    # Aplicar filtros
    if endereco_selecionado != "Todos":
        df = df[(df['from'] == endereco_selecionado) | (df['to'] == endereco_selecionado)]
    df = df[(df['score'] >= score_min) & (df['score'] <= score_max)]

    st.subheader("📄 Transações Monitoradas")

    # Exibir tabela com destaque
    styled_df = df.style.applymap(highlight_score, subset=['score'])
    st.dataframe(styled_df, use_container_width=True)

    # Botão para exportar CSV filtrado
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    st.download_button(
    label="📥 Exportar CSV filtrado",
    data=csv_buffer.getvalue(),
    file_name="transacoes_filtradas.csv",
    mime="text/csv"
    )
    
   # Botão para gerar e baixar o relatório PDF
    if st.button("📄 Gerar Relatório PDF de Transações Críticas"):
        generate_pdf_report(csv_path)

        try:
            with open("relatorio_transacoes_criticas.pdf", "rb") as f:
                st.download_button(
                    label="📥 Baixar Relatório PDF",
                    data=f,
                    file_name="relatorio_transacoes_criticas.pdf",
                    mime="application/pdf"
                )
            st.success("Relatório gerado com sucesso.")
        except FileNotFoundError:
            st.error("Erro: Relatório não foi encontrado.")


    # Estatísticas básicas
    st.subheader("📈 Estatísticas de Score")
    st.metric("Transações totais", len(df))
    st.metric("Score médio", round(df['score'].mean(), 2))

    # Gráfico de distribuição
    st.subheader("📊 Distribuição dos Scores")
    st.bar_chart(df['score'].value_counts().sort_index())
