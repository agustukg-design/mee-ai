# --- IMPOR PUSTAKA MODERN ---
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1. MUAT FILE PDF
print("⏳ SEDANG MEMBACA PDF...")
try:
    # Ini akan membaca file 'data.pdf' yang sudah Bapak upload
    loader = PyPDFLoader("data.pdf") 
    docs = loader.load()
    print(f"✅ Berhasil memuat {len(docs)} halaman PDF.")
except Exception as e:
    print(f"❌ ERROR: {e}")
    exit()

# 2. PECAH DATA (Agar muat di otak)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# 3. SIMPAN KE MEMORI (CHROMA)
print("⏳ SEDANG MENGHAFAL ISI PDF (Tunggu sebentar)...")
vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=OllamaEmbeddings(model="gemma2:2b")
)
retriever = vectorstore.as_retriever()

# 4. INSTRUKSI
template = """Kamu adalah asisten cerdas.
Gunakan informasi dari dokumen PDF berikut untuk menjawab pertanyaan.

Konteks PDF: {context}

Pertanyaan: {question}

Jawaban:"""

custom_prompt = PromptTemplate.from_template(template)

# 5. RANGKAIAN AI
llm = Ollama(model="gemma2:2b")
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | custom_prompt
    | llm
    | StrOutputParser()
)

# 6. TES PERTANYAAN
# Kita tanya apa isi PDF itu
pertanyaan = "Jelaskan rangkuman isi dokumen ini dan sebutkan poin pentingnya!"
print(f"\n❓ PERTANYAAN: {pertanyaan}")
print("🤖 GEMMA BERPIKIR...")

hasil = rag_chain.invoke(pertanyaan)
print("\n✅ JAWABAN DARI FILE PDF:")
print(hasil)
