# Esteganografia-via-DWT

Este projeto tem como objetivo demonstrar o uso e a aplicabilidade da técnica de esteganografia no domínio da frequência. O código trabalha com imagens nos formatos PNG e BMP, utilizando apenas imagens em tons de cinza (grayscale), com as dimensões de 256 x 256 píxels.

No meio digital, uma abordagem relevante é a Transformada Discreta de Wavelet (DWT), que permite inserir dados nos coeficientes de frequência da imagem, tornando as modificações menos perceptíveis.

Neste projeto, a ocultação dos dados é realizada nos coeficientes de frequência gerados pela Transformada Discreta de Wavelet (DWT), utilizando a wavelet Haar de nível 2. É possível alterar sub-bandas como HL, LH e HH, sendo essas as mais recomendáveis para a ocultação dos dados.

Entretanto, essa técnica possui uma limitação quanto à capacidade de ocultação, uma vez que a implementação utiliza apenas uma das sub-bandas disponíveis. Para aumentar a quantidade de dados ocultos, seria necessário adaptar o código para explorar outras bandas da DWT. Essa alteração aumentaria a complexidade do código.

1 - Instalação/Download

Para executar o algoritmo, é necessário utilizar o PyCharm. Primeiramente, faça o download do código e abra a pasta do projeto no PyCharm.

Após abrir o projeto, localize o arquivo main.py no painel de arquivos do PyCharm e abra-o.

Em seguida, abra o Terminal do PyCharm.

No terminal, instale as bibliotecas necessárias para executar o código:

pip install opencv-python
pip install numpy

Após a instalação das bibliotecas, o arquivo main.py pode ser executado pelo PyCharm. Para isso, clique com o botão direito sobre o arquivo main.py e selecione Run 'main'.

2 - Escolha da imagem

Após iniciar o programa, selecione a imagem em tons de cinza (grayscale) que será utilizada no processo de esteganografia.

3 - Inserção ou extração da mensagem

Após selecionar a imagem, o programa apresentará duas opções:

Inserir – utilizada para ocultar uma mensagem na imagem;
Extrair – utilizada para recuperar uma mensagem previamente ocultada.
Inserir

Ao selecionar a opção "inserir", o programa solicitará, no terminal, a mensagem que será ocultada:

Digite a mensagem secreta:

Digite a mensagem desejada e pressione Enter. O algoritmo realizará o processo de ocultação da mensagem na imagem selecionada.

Extrair

Ao selecionar a opção "extrair", o programa realizará o processo inverso. O algoritmo analisará a imagem e decodificará a mensagem secreta previamente ocultada, apresentando-a no terminal.

