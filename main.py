import cv2
import numpy as np
from tkinter import Tk, filedialog


# =====================================
# Essa função implementa uma Transformada Haar 2D inteira para uma imagem
# =====================================
def haar_int_2d(img):

    h, w = img.shape

    h2 = h // 2
    w2 = w // 2

    LL = np.zeros((h2,w2), dtype=np.int32)
    LH = np.zeros((h2,w2), dtype=np.int32)
    HL = np.zeros((h2,w2), dtype=np.int32)
    HH = np.zeros((h2,w2), dtype=np.int32)


    for i in range(h2):
        for j in range(w2):

            a = int(img[2*i,2*j])
            b = int(img[2*i,2*j+1])
            c = int(img[2*i+1,2*j])
            d = int(img[2*i+1,2*j+1])

            LL[i,j] = (a+b+c+d)//4
            LH[i,j] = (a+b-c-d)//4
            HL[i,j] = (a-b+c-d)//4
            HH[i,j] = (a-b-c+d)//4


    return LL,LH,HL,HH



# =====================================
# Haar Inteiro 2D - Inversa
# =====================================
def haar_int_inv_2d(LL,LH,HL,HH):

    h,w = LL.shape

    img = np.zeros((h*2,w*2),dtype=np.int32)


    for i in range(h):
        for j in range(w):

            ll = int(LL[i,j])
            lh = int(LH[i,j])
            hl = int(HL[i,j])
            hh = int(HH[i,j])


            img[2*i,2*j]     = ll+lh+hl+hh
            img[2*i,2*j+1]   = ll+lh-hl-hh
            img[2*i+1,2*j]   = ll-lh+hl-hh
            img[2*i+1,2*j+1] = ll-lh-hl+hh


    return img



# =====================================
# EOF
# =====================================
EOF = [
    1,1,1,1,
    1,1,1,1,
    1,1,1,1,
    1,1,1,0
]



# =====================================
# HH2 banda utilizada para ocultar os dados - algoritmo LSB de forma direta.
# =====================================
def inserir_mensagem(banda, mensagem):

    bits = []


    # UTF-8
    dados = mensagem.encode("utf-8")


    for byte in dados:

        bits.extend(
            [int(x) for x in format(byte,"08b")]
        )


    bits.extend(EOF)


    contador = 0


    for i in range(banda.shape[0]):

        for j in range(banda.shape[1]):

            valor = int(banda[i,j])


            # somente coeficientes positivos maiores ou igual a 2
            if valor >= 2:


                if contador < len(bits):

                    bit = bits[contador]


                    valor = (valor & ~1) | bit


                    banda[i,j] = valor


                    contador += 1


                else:

                    print("Bits da mensagem:",
                          contador-len(EOF))

                    print("EOF inserido")

                    return banda



    print("Capacidade insuficiente")

    return banda



# =====================================
# EXTRAÇÃO da mensagem
# =====================================
def extrair_mensagem(banda):

    bits = []


    for i in range(banda.shape[0]):

        for j in range(banda.shape[1]):

            valor = int(banda[i,j])


            if valor >= 2:


                bits.append(valor & 1)


                if len(bits) >= len(EOF):


                    if bits[-len(EOF):] == EOF:


                        bits = bits[:-len(EOF)]


                        dados = []


                        for k in range(0,len(bits),8):

                            byte = bits[k:k+8]


                            if len(byte) < 8:
                                break


                            valor_byte = 0


                            for b in byte:

                                valor_byte = (valor_byte << 1) | b


                            dados.append(valor_byte)


                        return bytes(dados).decode(
                            "utf-8",
                            errors="replace"
                        )


    return ""



# =====================================
# PROGRAMA PRINCIPAL
# =====================================

Tk().withdraw()


arquivo = filedialog.askopenfilename(
    title="Imagem",
    filetypes=[("PNG/BMP","*.png *.bmp")]
)



img = cv2.imread(
    arquivo,
    cv2.IMREAD_GRAYSCALE
).astype(np.int32)



h_original,w_original = img.shape

# caso a imagem tenha valores difirentes tipo 105 x 100 pixels, 1080 x 967 pixels. Caso, tamanho esteja correto, por exemplo
# 100 x 102, 1080 x 966 pixels, não é aplicado.

h = h_original - (h_original % 4)
w = w_original - (w_original % 4)


img = img[:h,:w]



# =====================================
# DWT 2 níveis
# =====================================

LL1,LH1,HL1,HH1 = haar_int_2d(img)

LL2,LH2,HL2,HH2 = haar_int_2d(LL1)



modo = input(
"\n1 - Inserir\n2 - Extrair\nEscolha: "
)



# =====================================
# INSERIR
# =====================================

if modo=="1":

    mensagem = input("Mensagem: ")

    HL2 = inserir_mensagem(
        HL2,
        mensagem
    )

# posso trocar HH2 por outra banda!


    LL1_rec = haar_int_inv_2d(
        LL2,
        LH2,
        HL2,
        HH2
    )


    imagem_rec = haar_int_inv_2d(
        LL1_rec,
        LH1,
        HL1,
        HH1
    )


    imagem_rec = imagem_rec[:h_original,:w_original]


    cv2.imwrite(
        "stego.png",
        np.clip(imagem_rec,0,255).astype(np.uint8)
    )


    print("Imagem stego criada")



# =====================================
# EXTRAIR
# =====================================

elif modo=="2":


    texto = extrair_mensagem(
        HL2
    )


    print("\nMensagem:")
    print(texto)