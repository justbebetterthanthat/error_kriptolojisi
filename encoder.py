import random
import time
from datetime import datetime, timedelta

# =============================================================================
# PROJE ADI: ERROR KRİPTOLOJİSİ - ENCODER MODÜLÜ
# GÖREV: Veriyi şifrelemek, parçalamak ve log dosyasına gizlemek.
# YAZAR: Yiğit Emir ARIN - TÜBİTAK 2204-A
# =============================================================================

# --- HATA VE GÜRÜLTÜ SÖZLÜĞÜ (DATA MAPPING DICTIONARY) ---
# '0' Biti için atanan Standart Hatalar
LOG_LEVEL_0 = [
    "[ERROR] Connection timed out: Port 80 unreachable.",
    "[ERROR] DNS lookup failed for upstream service.",
    "[ERROR] Packet loss detected (Retry: 3).",
    "[ERROR] Remote host closed connection unexpectedly."
]

# '1' Biti için atanan Kritik Hatalar
LOG_LEVEL_1 = [
    "[CRITICAL] Memory access violation at 0x8F4A.",
    "[CRITICAL] Kernel panic: Process unexpected exit.",
    "[CRITICAL] Segmentation fault in thread_main.",
    "[CRITICAL] Buffer overflow detected at runtime."
]

# Entropi düşürmek için kullanılacak ÇÖP (NOISE) veriler
NOISE_LOGS = [
    "[INFO] Scheduled system maintenance checking...",
    "[INFO] Cache cleared successfully.",
    "[WARNING] High latency in auxiliary bus.",
    "[DEBUG] Variable dump: NULL response."
]

def text_to_bits(text, encoding='utf-8'):
    """Metin verisini 8-bitlik binary dizisine (01001...) çevirir."""
    bits = bin(int.from_bytes(text.encode(encoding), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def generate_log_file(message, filename="system_error_logs.txt"):
    """
    Şifreli bitleri hata satırlarına dönüştürür ve dosyaya yazar.
    Steganografi Katmanı burada çalışır.
    """
    print(f">> [SİSTEM] Veri işleniyor ve 'yokmuş gibi' gösteriliyor...")
    
    # 1. Kriptografik Simülasyon: Veriyi Binary'e çeviriyoruz (Kyber temsili)
    binary_data = text_to_bits(message)
    
    logs = []
    # Logların başlangıç zamanı (Şu an)
    current_time = datetime.now()

    # Sistemin gerçekçi görünmesi için başlık
    logs.append(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} [INFO] SERVER BOOT SEQUENCE STARTED (PID: 1045).")

    for bit in binary_data:
        # TRAFİK ŞEKİLLENDİRME (TRAFFIC SHAPING):
        # Loglar arasına milisaniyelik rastgele gecikmeler eklenir.
        # Bu, logların bir makine değil, doğal süreçlerle oluştuğunu gösterir.
        wait_time = random.uniform(0.02, 0.6) 
        current_time += timedelta(seconds=wait_time)
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # GÜRÜLTÜ EKLEME (NOISE INJECTION):
        # %25 ihtimalle araya sahte/masum loglar sıkıştırılır.
        if random.random() < 0.25:
            noise = random.choice(NOISE_LOGS)
            logs.append(f"{timestamp} {noise}")
            # Gürültüden sonra zamanı biraz daha ilerlet
            current_time += timedelta(seconds=random.uniform(0.01, 0.2))
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # VERİ GİZLEME (MAPPING):
        # Bit 0 -> [ERROR] satırı
        # Bit 1 -> [CRITICAL] satırı
        if bit == '0':
            log_msg = random.choice(LOG_LEVEL_0)
            logs.append(f"{timestamp} {log_msg}")
        else:
            log_msg = random.choice(LOG_LEVEL_1)
            logs.append(f"{timestamp} {log_msg}")

    # Bitiş imzası
    logs.append(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} [EMERGENCY] SYSTEM SHUTDOWN INITIATED.")

    # Dosyaya Yazma İşlemi
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(logs))
        print(f">> [BAŞARILI] '{filename}' dosyası oluşturuldu.")
        print(f">> [BİLGİ] Toplam Satır Sayısı: {len(logs)}")
    except IOError as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    # Örnek Gizli Mesaj (Kritik Anahtar)
    gizli_mesaj = input("Gizlenecek Kripto Anahtarı Girin: ")
    generate_log_file(gizli_mesaj)