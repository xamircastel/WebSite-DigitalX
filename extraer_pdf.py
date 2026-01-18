"""
Script para extraer el contenido de texto de archivos PDF
y guardarlo en archivos de texto (.txt) accesibles.
"""

import pdfplumber
from pathlib import Path
import os


def extraer_texto_pdf(ruta_pdf: str, ruta_salida: str = None) -> str:
    """
    Extrae todo el texto de un archivo PDF.
    
    Args:
        ruta_pdf: Ruta al archivo .pdf
        ruta_salida: Ruta donde guardar el archivo .txt (opcional)
    
    Returns:
        El texto extraído del PDF
    """
    texto_completo = []
    
    nombre_archivo = Path(ruta_pdf).stem
    texto_completo.append(f"{'='*60}")
    texto_completo.append(f"DOCUMENTO PDF: {nombre_archivo}")
    texto_completo.append(f"{'='*60}\n")
    
    try:
        with pdfplumber.open(ruta_pdf) as pdf:
            texto_completo.append(f"Total de páginas: {len(pdf.pages)}\n")
            
            for num_pagina, pagina in enumerate(pdf.pages, 1):
                texto_completo.append(f"\n{'─'*40}")
                texto_completo.append(f"PÁGINA {num_pagina}")
                texto_completo.append(f"{'─'*40}\n")
                
                # Extraer texto de la página
                texto = pagina.extract_text()
                if texto:
                    texto_completo.append(texto)
                else:
                    texto_completo.append("[Página sin texto extraíble - posiblemente solo imágenes]")
                
                # Extraer tablas si existen
                tablas = pagina.extract_tables()
                if tablas:
                    for i, tabla in enumerate(tablas, 1):
                        texto_completo.append(f"\n[TABLA {i}]")
                        for fila in tabla:
                            # Limpiar celdas None
                            celdas = [str(celda).strip() if celda else "" for celda in fila]
                            texto_completo.append(" | ".join(celdas))
                
    except Exception as e:
        texto_completo.append(f"\n❌ Error al procesar: {e}")
    
    resultado = "\n".join(texto_completo)
    
    # Guardar en archivo si se especifica ruta de salida
    if ruta_salida:
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        with open(ruta_salida, "w", encoding="utf-8") as f:
            f.write(resultado)
        print(f"✓ Guardado: {ruta_salida}")
    
    return resultado


def procesar_todos_los_pdfs(carpeta_base: str):
    """
    Busca y procesa todos los archivos .pdf en una carpeta y subcarpetas.
    """
    carpeta_base = Path(carpeta_base)
    carpeta_salida = carpeta_base / "documentos_texto"
    
    archivos_pdf = list(carpeta_base.rglob("*.pdf"))
    
    print(f"\n📁 Encontrados {len(archivos_pdf)} archivos PDF\n")
    
    for archivo in archivos_pdf:
        try:
            # Crear nombre de archivo de salida
            nombre_relativo = archivo.relative_to(carpeta_base)
            ruta_txt = carpeta_salida / nombre_relativo.with_suffix(".txt")
            
            print(f"📄 Procesando: {archivo.name}")
            extraer_texto_pdf(str(archivo), str(ruta_txt))
            
        except Exception as e:
            print(f"❌ Error procesando {archivo.name}: {e}")
    
    print(f"\n✅ Proceso completado. Archivos guardados en: {carpeta_salida}")


if __name__ == "__main__":
    # Carpeta base del proyecto
    CARPETA_PROYECTO = r"c:\proyectos\WebSite-DigitalX\imagenes"
    
    procesar_todos_los_pdfs(CARPETA_PROYECTO)
