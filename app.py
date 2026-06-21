import os
from transformers import pipeline

def jalankan_ai():
    print("=" * 50)
    print("Memuat Model AI... (Mohon tunggu sebentar)")
    print("=" * 50)
    
    # Menggunakan model text-generation gratis dan ringan dari Hugging Face
    # Model: GPT-2 (bisa diganti dengan model lain seperti TinyLlama atau Phi-3)
    generator = pipeline('text-generation', model='gpt2')
    
    print("\n[AI Siap!] Ketik 'keluar' untuk menghentikan program.")
    
    while True:
        # Menerima input pertanyaan dari pengguna
        perintah = input("\nTanya AI: ")
        
        if perintah.lower() == 'keluar':
            print("Terima kasih telah menggunakan AI ini!")
            break
            
        if not perintah.strip():
            print("Input tidak boleh kosong.")
            continue
            
        print("AI sedang berpikir...")
        
        # Menghasilkan teks jawaban
        hasil = generator(perintah, max_length=100, num_return_sequences=1)
        
        # Menampilkan hasil jawaban AI
        print("\nJawaban AI:")
        print(hasil[0]['generated_text'])
        print("-" * 50)

if __name__ == "__main__":
    jalankan_ai()
