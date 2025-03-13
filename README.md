# 📚 Chatbot Baseado em PDFs com IA 🤖

## 📌 Visão Geral
Este projeto implementa um chatbot interativo capaz de responder perguntas com base no conteúdo de arquivos PDF. Para isso, utilizamos IA generativa, embeddings e busca vetorizada para estruturar um sistema inteligente de recuperação de informações.

## 🚀 Tecnologias Utilizadas
- **PyMuPDF** (`fitz`): Extração de texto dos PDFs
- **Sentence-Transformers** (`all-MiniLM-L6-v2`): Criação de embeddings das sentenças
- **FAISS**: Indexação e busca eficiente de textos
- **OpenAI API** *(opcional)*: Para aprimorar respostas com IA generativa
- **Streamlit** *(futuro)*: Para criar uma interface interativa

## 📂 Estrutura do Projeto
```
📁 chatbot_pdf_ai
│-- 📄 documento.pdf           # Exemplo de arquivo PDF
│-- 📜 chatbot_pdf.py          # Código principal
│-- 📜 requirements.txt        # Dependências do projeto
│-- 📜 README.md               # Documentação do projeto
```

## ⚙️ Como Rodar o Projeto
1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/chatbot_pdf_ai.git
   cd chatbot_pdf_ai
   ```
2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
3. **Adicione um arquivo PDF para análise**
   - Substitua `documento.pdf` pelo seu próprio arquivo

4. **Execute o chatbot**
   ```bash
   python chatbot_pdf.py
   ```
5. **Faça perguntas sobre o conteúdo do PDF!** 🎯

## 🛠 Melhorias Futuras
- 🔹 Implementar interface com `Streamlit`
- 🔹 Adicionar integração com OpenAI para respostas aprimoradas
- 🔹 Melhorar segmentação de texto e embeddings

📢 **Contribuições são bem-vindas!** Se tiver sugestões, abra uma issue ou faça um pull request. 🚀

