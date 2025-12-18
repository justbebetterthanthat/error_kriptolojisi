import re

# =============================================================================
# PROJE ADI: ERROR KRİPTOLOJİSİ - DECODER MODÜLÜ
# GÖREV: Karmaşık log dosyasını ayrıştırmak ve veriyi kurtarmak.
# =============================================================================

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    """Elde edilen 0-1 dizisini tekrar anlamlı yazıya çevirir."""
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def analyze_and_decode(filename="system_error_logs.txt"):
    print("-" * 50)
    print(f">> [DECODER] Log Dosyası Taranıyor: {filename}")
    
    extracted_bits = ""
    processed_lines = 0
    noise_ignored = 0
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        for line in lines:
            processed_lines += 1
            
            # FİLTRELEME KATMANI (FILTERING):
            # Sistem önce satırın bir "veri" mi yoksa "gürültü" mü olduğuna bakar.
            # INFO ve WARNING logları, yanıltmaca olduğu için yok sayılır.
            if "[INFO]" in line or "[WARNING]" in line:
                noise_ignored += 1
                continue
            
            # ÇÖZÜMLEME KATMANI (DECODING):
            # Sözlük kurallarına göre geri dönüşüm yapılır.
            if "[ERROR]" in line:
                extracted_bits += "0"
            elif "[CRITICAL]" in line:
                # "SYSTEM HALTED" bitiş komutudur, veri değildir.
                if "SYSTEM HALTED" not in line:
                    extracted_bits += "1"
        
        # Sonuçların Raporlanması
        print(f">> [ANALİZ] Toplam Taranan Satır: {processed_lines}")
        print(f">> [ANALİZ] Temizlenen Gürültü (Noise): {noise_ignored} satır")
        print(f">> [SONUÇ] Ayrıştırılan Ham Veri (Bits): {extracted_bits[:30]}...") # İlk 30 biti göster
        
        # Binary'den Orijinal Mesaja Dönüş
        if extracted_bits:
            original_message = text_from_bits(extracted_bits)
            print("-" * 50)
            print(f"✅ GİZLİ MESAJ ÇÖZÜLDÜ: {original_message}")
            print("-" * 50)
        else:
            print(">> Hata: Dosya içinde anlamlı veri bulunamadı.")
            
    except FileNotFoundError:
        print("HATA: 'system_error_logs.txt' dosyası bulunamadı. Önce Encoder'ı çalıştırın.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    analyze_and_decode()