import re # Düzenli İfadeler (Regex) kütüphanesi

def sifreyi_coz(dosya_yolu):
    print(">> Log dosyası analiz ediliyor...")
    cozulen_mesaj = ""
    
    try:
        with open(dosya_yolu, 'r') as dosya:
            satirlar = dosya.readlines()
            
        for satir in satirlar:
            # 1. Filtreleme: Biz sadece "Memory allocation" hatalarına şifreyi gizlemiştik.
            # Diğer "Connection failed" vs. hatalarını yoksayacağız.
            
            # Regex: "block ID: " yazısından sonra gelen sayıları yakala (\d+)
            bulunan = re.search(r"block ID: (\d+)", satir)
            
            if bulunan:
                # Sayıyı yakaladık (String olarak)
                sifreli_sayi_str = bulunan.group(1)
                
                # Sayıyı tam sayıya (int) çevir
                sifreli_sayi = int(sifreli_sayi_str)
                
                # Sayıyı harfe çevir (ASCII dönüşümü)
                harf = chr(sifreli_sayi)
                
                # Mesaja ekle
                cozulen_mesaj += harf
                
        print("-" * 30)
        print(f"✅ GİZLİ MESAJ BULUNDU: {cozulen_mesaj}")
        print("-" * 30)
        
    except FileNotFoundError:
        print("Hata: Log dosyası bulunamadı! Önce şifreleyiciyi çalıştırın.")

# --- KULLANIM ---
sifreyi_coz('error_logs.txt')