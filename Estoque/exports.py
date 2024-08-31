import os
import shutil
from openpyxl.styles import Font, Alignment

def verificar_e_recriar_modelo(caminho_modelo, caminho_modelo_original):
    # Verifica se o arquivo modelo existe
    if not os.path.exists(caminho_modelo):
        # Se não existir, copia o modelo original para o caminho do modelo
        shutil.copy(caminho_modelo_original, caminho_modelo)

def ajustar_largura_colunas(ws):
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Coluna que está sendo processada
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = max_length + 1
        ws.column_dimensions[column].width = adjusted_width

def estilo_estoque(cell, col):
    # Define a fonte
    font = Font(name='Arial', size=11)

    # Define o alinhamento condicionalmente
    if col == 'E':
        alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    else:
        alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

    # Aplica os estilos à célula
    cell.font = font
    cell.alignment = alignment

def estilo_historico(cell, col):
    # Define a fonte
    font = Font(name='Arial', size=11)

    # Define o alinhamento condicionalmente
    if col == 'F':
        alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    else:
        alignment = Alignment(horizontal='center', vertical='center')

    # Aplica os estilos à célula
    cell.font = font
    cell.alignment = alignment