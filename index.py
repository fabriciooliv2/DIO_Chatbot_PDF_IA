import fitz  # PyMuPDF
import openai
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Configurar modelo de embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Função para extrair texto de um PDF
def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with fitz.open(caminho_pdf) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

# Carregar e processar o PDF
caminho_pdf = "documento.pdf"  # Substituir pelo caminho real
documento_texto = extrair_texto_pdf(caminho_pdf)
sentencas = documento_texto.split(". ")  # Simples segmentação por frases

# Criar embeddings das sentenças
embeddings = model.encode(sentencas)

# Indexação com FAISS
d = embeddings.shape[1]  # Dimensão do embedding
index = faiss.IndexFlatL2(d)
index.add(np.array(embeddings))

# Função de busca
def buscar_resposta(pergunta):
    pergunta_embedding = model.encode([pergunta])
    _, indices = index.search(np.array(pergunta_embedding), k=1)
    return sentencas[indices[0][0]]

# Exemplo de uso
pergunta = "Qual é o objetivo do estudo?"
resposta = buscar_resposta(pergunta)
print("Pergunta:", pergunta)
print("Resposta:", resposta)
