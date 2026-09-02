# Esteganografia-via-DWT

Este projeto tem como objetivo demonstrar o uso e a aplicabilidade da técnica de esteganografia no domínio da frequência. O código trabalha com imagens nos formatos PNG e BMP, utilizando apenas tons de cinza.

No meio digital, uma abordagem relevante é a Transformada Discreta de Wavelet (DWT), que insere dados nos coeficientes de frequência da imagem, tornando a modificação menos perceptível. Este projeto tem como objetivo demonstrar o uso e a aplicabilidade da técnica de esteganografia no domínio da frequência. O código trabalha com imagens nos formatos PNG e BMP, utilizando apenas tons de cinza (grayscale). A ocultação de dados é realizada nos coeficientes de frequência gerados pela Transformada Discreta de Wavelet (DWT), especificamente com a wavelet Haar de nível 2. Neste código, é possível alterar as sub-bandas, como HL, LH e HH ( são as mais recomendáveis).

Entretanto, essa técnica possui uma limitação quanto à capacidade de ocultação, uma vez que utiliza apenas uma das sub-bandas disponíveis. Para aumentar a quantidade de dados ocultos, seria necessário adaptar o código para explorar outras bandas da DWT, com isto aumentamos a complexidade do código. 



1 - utilizando o código main.py é possível ter acesso ao algoritmo capaz de ocultar a mensagem (escrita no terminal) em uma imagem em tons de cinza(grayscale):
no terminal do pycharmy é necessário utilizar alguns comandos 
