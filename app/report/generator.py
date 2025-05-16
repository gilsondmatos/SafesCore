# app/reports/generator.py

from fpdf import FPDF
import pandas as pd
import os
from datetime import datetime

def generate_pdf_report(csv_path, output_path="relatorio_transacoes_criticas.pdf", score_threshold=50):
    df = pd.read_csv(csv_path)
    df_critico = df[df['score'] < score_threshold]

    if df_critico.empty:
        print("[INFO] Nenhuma transação crítica encontrada.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Relatório de Transações Críticas - SafeScore", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", '', 11)
    pdf.cell(0, 10, f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True)
    pdf.cell(0, 10, f"Total de transações críticas: {len(df_critico)}", ln=True)
    pdf.ln(10)

    for index, row in df_critico.iterrows():
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(0, 10, f"Transação: {row['hash']}", ln=True)
        pdf.set_font("Arial", '', 10)
        pdf.multi_cell(0, 8,
            f"De: {row['from']}\n"
            f"Para: {row['to']}\n"
            f"Valor: {row['value']} {row['token']}\n"
            f"Data/Hora: {row['timestamp']}\n"
            f"Score de Risco: {row['score']}\n"
            f"-----------------------------"
        )

    pdf.output(output_path)
    print(f"[INFO] Relatório gerado com sucesso: {output_path}")
