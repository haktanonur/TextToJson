import docx
import re
import json
import sys

# .docx dosyasını aç
docx_path = sys.argv[1] if len(sys.argv) > 1 else "input.docx"
output_json = sys.argv[2] if len(sys.argv) > 2 else "file.json"

try:
    doc = docx.Document(docx_path)
except Exception as e:
    print(f".docx dosyası açılırken bir hata oluştu: {e}")
    exit(1)

# Tüm metni oku
content = ""
for para in doc.paragraphs:
    content += para.text + "\n"

# Her çifti kelime olarak işlemek için satırları temizle
pairs = re.findall(r"(.+?):\s*(.+)", content)

# JSON formatına çevir
word_dict = {pair[0].strip(): pair[1].strip() for pair in pairs}

# Sonucu JSON dosyasına yaz
try:
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(word_dict, json_file, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"JSON dosyasına yazılırken bir hata oluştu: {e}")
    exit(1)

# Çıktıyı ekrana da basmak istersen
## print(json.dumps(word_dict, ensure_ascii=False, indent=4))