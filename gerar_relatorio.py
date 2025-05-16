# gerar_relatorio.py

from app.report.generator import generate_pdf_report

if __name__ == "__main__":
    generate_pdf_report("app/data/transacoes_com_score.csv")
