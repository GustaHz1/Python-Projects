import pytesseract
import cv2

caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"/tesseract.exe"

# Lendo a imagem
imagem = cv2.imread("Spotify_menu.png")

# Convertendo a imagem para cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Melhorando o constraste
# A função retorna 2 valores sendo o primeiro o valor do limiar aplicado que não precisam
lixo, imagem = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY)

texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)

# Padronizando o texto
texto = texto.lower().strip().replace(" ", "")

if 'oquevocêquerouvir?' in texto:
    print("Possui o texto")
    
else:
    print("Não possui o texto")
