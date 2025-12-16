# --- IMPOR PUSTAKA MODERN (SESUAI REQUEST BAPAK) ---
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# --- 1. DATA BUDAYA MEE & PAPUA (REVISI FINAL) ---
teks_budaya = """
FAKTA PENTING TENTANG MAKANAN DAN BUDAYA PAPUA (SUKU MEE):
1. Makanan pokok: Makanan pokok orang Papua BUKAN Nasi Timbel. Itu salah besar.
2. Papeda: Makanan asli adalah Papeda (Sagu) disajikan dengan Ikan Kuah Kuning.
3. Ubi Jalar: Dalam bahasa daerah Mee, ubi jalar disebut NOTA atau DUGII.
4. Babi: Di wilayah Pegunungan Tengah (Suku Mee), babi disebut EKINA.
5. Bakar Batu: Tradisi memasak bersama disebut Bakar Batu (Barapen).
6. Sayuran: Sayur lilin, gedi, dan bunga pepaya adalah sayuran umum.

Tolong hafalkan istilah NOTA, DUGII, dan EKINA ini baik-baik.
"""

print("⏳ MEMULAI SISTEM RAG MODERN (NOTA & EKINA)...")

# --- 2. PERSIAPAN DATA (SPLIT & EMBED) ---
# Ubah teks menjadi dokumen
docs = [Document(page_content=teks_budaya)]

# Pecah dokumen (Teknik Recursive Splitter ala Profesional)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.split_documents(docs)

# Masukkan ke Database Vektor (ChromaDB)
# Kita pakai 'gemma2:2b' juga untuk embedding supaya hemat kuota
vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=OllamaEmbeddings(model="gemma2:2b")
)
retriever = vectorstore.as_retriever()

# --- 3. BUAT PROMPT KHUSUS ---
template = """Kamu adalah asisten ahli budaya Papua khususnya Suku Mee.
Gunakan data konteks di bawah ini untuk menjawab pertanyaan. 
Jika data ada di konteks, gunakan bahasa asli (Nota/Dugii/Ekina).

Konteks: {context}

Pertanyaan: {question}

Jawaban:"""

custom_prompt = PromptTemplate.from_template(template)

# --- 4. SIAPKAN OTAK GEMMA ---
llm = Ollama(model="gemma2:2b")

# --- 5. RANGKAIAN AI (CHAIN) - INI BAGIAN CANGGIHNYA ---
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | custom_prompt
    | llm
    | StrOutputParser()
)

# --- 6. EKSEKUSI PERTANYAAN ---
pertanyaan = "Apa nama asli makanan pokok ubi dan babi dalam bahasa Mee? Jelaskan!"

print(f"\n❓ PERTANYAAN: {pertanyaan}")
print("🤖 GEMMA BERPIKIR...")

hasil = rag_chain.invoke(pertanyaan)

print("\n✅ JAWABAN FINAL:")
print(hasil)
