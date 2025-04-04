# GCode-Parser

Bu, G-code komutlarını ayrıştırmak için basit bir Python tabanlı ayrıştırıcıdır. G-code, 3D yazıcılar ve CNC makineleri gibi bilgisayarlı üretim makineleri tarafından kullanılan bir komut setidir. Bu proje, G-code dosyalarını çözümleyip her bir komutu yapılandırılmış bir biçimde analiz etmeyi amaçlar.

## Özellikler

- G-code dosyalarını satır satır okur  
- Her bir G veya M komutunu ve ona bağlı parametreleri ayrıştırır  
- Ayrıştırılan komutları sözlük (dictionary) listesi olarak döndürür  
- Yorumları ve boş satırları yok sayar

## Kullanım

Aşağıdaki gibi bir G-code dosyasını çözümlemek için `parser.py` dosyasını çalıştırabilirsiniz:

```bash
python parser.py example.gcode
```

Komut dosyası `example.gcode` dosyasını okuyacak ve çıktıyı standart çıktıya (terminale) yazacaktır.

## Örnek G-code Satırı

```gcode
G1 X10 Y20 F1500
```

Bu satır şu şekilde ayrıştırılır:

```json
{
  "command": "G1",
  "params": {
    "X": 10.0,
    "Y": 20.0,
    "F": 1500.0
  }
}
```

## Çıktı Formatı

Ayrıştırılmış G-code çıktısı bir JSON dizisi (listesi) olarak yapılandırılır. Her komut bir sözlük (dictionary) olarak gösterilir. Örnek çıktı:

```json
[
  {
    "command": "G1",
    "params": {
      "X": 10.0,
      "Y": 20.0,
      "F": 1500.0
    }
  },
  {
    "command": "M3",
    "params": {}
  }
]
```

## Kurulum

Python 3.x yüklü olmalıdır. Ek bağımlılık yoktur.

## Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Bir hata bildirimi oluşturun veya doğrudan bir çekme isteği (pull request) gönderin.

## Lisans

Bu proje MIT lisansı altındadır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.
