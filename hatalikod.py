import logging
import random
import time

# 1. Loglama ayarlarını yapıyoruz (Dosyaya kaydetmesi için)
logging.basicConfig(
    filename='error_logs.txt', 
    filemode='w', # Her çalıştırışta dosyayı sıfırdan oluştur
    level=logging.ERROR, 
    format='%(asctime)s [%(levelname)s] Module:%(module)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def sahte_hata_ureteci():
    """Mesajda olmayan, kafa karıştırmak için rastgele hata satırları ekler."""
    fake_errors = [
        "Connection timeout in localized area.",
        "Buffer overflow warning at memory 0x84F.",
        "Unknown signal received from port 8080.",
        "Update checking failed: Server not reachable."
    ]
    logging.error(random.choice(fake_errors))

def veriyi_gizle(mesaj):
    print(">> Şifreleme işlemi başlatılıyor...")
    print(f">> Gizlenecek Mesaj: {mesaj}")
    
    # Gerçekçilik katmak için başlangıç hatası
    logging.critical("SYSTEM CRITICAL FAILURE INITIATED...")
    
    for harf in mesaj:
        # Harfi ASCII sayısına çevir (Örn: 'A' -> 65)
        ascii_deger = ord(harf)
        
        # KAFA KARIŞTIRICI: Araya sahte hata atalım (Mesajın %30'u kadar ihtimalle)
        if random.random() < 0.3:
            sahte_hata_ureteci()
            
        try:
            # 2. ÖZEL BÖLÜM: Harfin kodunu bir "Memory ID" gibi göstererek hata fırlatıyoruz
            # Hata mesajı şöyle görünecek: "Memory allocation failed at ID: 65"
            raise MemoryError(f"Memory allocation failed at block ID: {ascii_deger}")
            
        except MemoryError as e:
            # Hata oluştuğunda bunu log dosyasına 'Error' olarak kaydet
            logging.error(e)
            
        # Sistem biraz "zorlanıyormuş" gibi bekletelim (isteğe bağlı)
        time.sleep(0.01)

    # Bitiş fake logu
    logging.critical("DUMPING MEMORY TO DISK. SYSTEM HALTED.")
    print(">> İşlem tamam! Hatalar 'error_logs.txt' dosyasına gizlendi.")

# --- KULLANIM ---
gizli_mesaj = input("Şifrelenecek Mesajı Girin: ")
veriyi_gizle(gizli_mesaj)