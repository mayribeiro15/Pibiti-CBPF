# Processamento de Imagens: Algoritmos de Segmentação e Detecção de Borda com Análise de Redes Neurais Deep Learning (PIBITI-CBPF)

## Resumo 
O processamento de imagens para detecção de padrões em análises microscópicas representa um grande desafio em questões de automatização. O objetivo deste trabalho é utilizar a linguagem Python para implementar e analisar diversas técnicas de segmentação existentes a fim de gerar resultados sobre as abordagens mais eficientes. Primeiramente, foi realizado um embasamento teórico sobre segmentação de imagens, com ênfase nos métodos implementados pela biblioteca OpenCv, escolhida como base para o desenvolvimento dos códigos. Em seguida, foram analisados os principais algoritmos de segmentação e detecção de borda com a tentativa de facilitar a aplicação de técnicas cujos resultados ainda são dependentes de observação humana. Por fim, foi feita uma análise da aplicação da segmentação de imagens a Redes Neurais Deep Learning, em especial ao algoritmo CNN (Convolutional Neural Network), que possui uma configuração amplamente automatizada. Dessa forma, ao reunir tais análises subsequentes, os resultados demonstram um comparativo das técnicas de segmentação e do impacto da automatização no processamento de imagens aplicado.

Referências principais:
- https://kanezaki.github.io/pytorch-unsupervised-segmentation/ICASSP2018_kanezaki.pdf
- https://daneshyari.com/article/preview/6922503.pdf

## Técnicas de Segmentação
### K-means
O k-means consiste na coloração de uma determinada imagem em k cores. O processo é utilizado atualmente para segmentação inicial das imagens processadas e a quantidade de cores na segmentação é definida nas linhas de código. O algortimo prioriza as cores por ocorrência de pixels semelhantes, o que pode gerar erros em casos complexos.

Em casos simplificados o algoritmo consegue boa segmentação com um número baixo de interações.
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/K-means/estromatolito.jpg?raw=true" width="350">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/K-means/estromatolito_kmeans.jpg?raw=true" width="350">
</p>

No caso de bordas muito espessas por isso os grãos nem sempre são priorizados. Assim, para que um grão seja diferenciado é necessário um alto valor de k, criando segmentações de partes desprezíveis. O exemplo abaixo utiliza valor mínimo k=9 para segmentação dos grãos rosa e amarelo.
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/K-means/graocolor.jpg?raw=true" width="350" =>
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/K-means/graocolor_kmeans.jpg?raw=true" width="350">
</p>

Embora a definição do número de cores seja definido nas linhas de código, o K-means é considerado uma técnica de segmentação não supervisionada, pois o agrupamento de regiões é produto exclusivamente da semelhança entre os pixels.

### Region Growing

### Filtros Convolucionais
Os filtros convolucionais são uma forma de ponderar a informação de cada pixel com as de seus adjacentes através de um operador de convolução entre a matriz e o kernel (matriz de filtro) correspondente. Para evitar que a convolução seja aplicada manualmente, foi utilizada novamente a biblioteca do OpenCv cuja aplicação do filtro 2d apresentou resultado satisfatório nas etapas da convolução. Como o resultado da convolução pode acarretar em pixels negativos, pode ser aplicada a função Relu, para zerar esses valores.
No exemplo abaixo temos a aplicação de um filtro laplaciano na imagem original, primeiramente com a convolução detalhada e em seguida com a biblioteca disponível. Percebemos que o OpenCv pode ser um grande aliado para reduzir significativamente a aplicação convolucional.
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/CNN-Segmentation/idaho_convolve.jpg" width="350" =>
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/CNN-Segmentation/idaho_opencv.jpg" width="350">
</p>

O resultado da convolução será uma sequência de features maps, com as principais características ponderadas pelos kernels. Para a aplicação da CNN, que é uma sigla do termo em inglês para Redes Neurais Convolucionais, será necessário aplicar o resultado dessa segmentação como a primeira etapa de pré-processamento. Esse processo é responsável também pela redução das dimensões da imagem, o que acelera o procesamento devido a alta complexidade computacional do CNN.

## Técnicas de Detecção de Borda
### Slic
A técnica Slic é uma sigla do termo Simple Linear Iterative Clustering, que se baseia na técnica de agrupamento em superpixels. Um superpixel simboliza um agrupamento local de pixels segundo as semelhanças entre eles. Portanto, a técnica é análoga a clusterização por K-Means mas com a ressalva de que o algoritmo retorna a borda do superpixel de forma a gerar uma detecção de borda.
O algoritmo implementado pela classe da biblioteca do OpenCv tem como parâmetros o raio médio da região, o que representa uma grande desvantagem pois detecta bordas inexistentes em objetos maiores. Por essa razão, para este algoritmo foi utilizado a biblioteca Scikit-image, que possui maior quantidade de parâmetros a serem analisados.

No exemplo abaixo, a quantidade de regiões foi ajustada manualmente de forma a obter a borda da região principal.
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Slic/carb.jpg" width="350">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Slic/carb_slic.jpg" width="347">
</p>

Da mesma forma que o K-means, como o agrupamento de regiões é produto exclusivamente da semelhança entre os pixels, o Slic também pode ser considerado um algoritmo não supervisionado.

### Canny Edge
O algoritmo é amplamente difundido por utilizar, assim como o slic, uma segmentação com técnica de decisão arbitrária e direta. Nessa caso é utlizado, primeiramente, um kernel de filtro gaussiano que aplica um efeito de embaçamento na imagem. A partir da imagem filtrada, são analisados a magnitude e a orientação do gradiente entre os pixels da imagem, de forma a identificar as bordas.

A detecção de falhas internas e ranhuras como bordas é comum nesse algoritmo devido ao aparecimento indesejado de gradientes. Para controlar essa má interpretação, pode ser aplicado um processo de segmentação como pré-processamento.

Nos exemplos abaixo temos a imagem inicial com a detecção de borda direta e em seguida amdetecção de borda utilizando o K-Means como pré-processamento.

<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Canny-Edge/idaho_cannyedge.jpg" width="350">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Canny-Edge/idaho_cannyedge_kmeans.jpg" width="350">
</p>

### Watershed
O algortimo do watershed de baseia na divisão de regiões segundo a ideia de um fluxo de água partindo das bordas da imagem e passando pelas regiões de maior contraste, ou seja, as bordas da região de interesse. 
Após a imagem ser processada, é necessário aplicar transformações de threshold, closing e opening para que esta esteja apta a gerar uma detecção de bora efetva. O threshold realiza o filtro dos valores a serem considerados, reduzindo a variedade nos valores de pixels; a função closing destaca a região central dos pontos de interesse, gerando a região de certeza, chama sure foreground; por fim, a função opening realiza a dilatação dos pontos, a partir da qual podemos obter o que chamamos de sure background, ou seja, a parte da imagem que pode ser desconsiderada já que está a uma margem segura dos pontos de interesse. Dessa forma, a região possível para detecção de borda é limitada ao espaço entre o sure foreground e o sure background e a função do watershed pode ser aplicada com maior rendimento. 
Esse algoritmo é utilizado atualmente por ser efetivo na maioria dos casos embora a maior dificuldade seja aplicar pré-processamento necessário.

Em casos mais simplificados o algoritmo apresenta uma boa segmentação apenas com o pré-processamento descrito mas, assim como no Canny Edge, em casos em que a região de interesse possui maiores variações, é vantajoso utilizar algoritmos de segmentação no pré-processamento. No exemplo abaixo, temos um comparativo da aplicação direta do watershed e da aplicação após o uso da segmentação por k-means.
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Watershed/mineral_watershed.jpg" width="350">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Watershed/mineral_watershed_kmeans.jpg" width="350">
</p>
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Watershed/estromatolito_watershed.jpg" width="350">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Watershed/estromatolito_watershed_kmeans.jpg" width="350">
</p>

Além dos métodos acima, podem ser aplicados pré-processamentos específicos para um bom resultado do watershed. Por esse fator, a técnica é considerada como supervisionada pois demanda acompanhamento para segmentação manual ou treinamento das classes.

## CNN - Convolucional Neural Segmentation

Nos algoritmos anteriores, era necessário um acompanhamento de forma a escolher regiões, número de segmentação ou até mesmo seeds inciais para o processamento da imagem. A segmentação por redes neurais ou deep learning traz uma automatização pois aplica técnicas de machine learning  em redes neurais para treinamento de classes de modo que o programa possa reconhecer sozinho padrões em várias camadas de processamento de imagem.

Devido a alta complexidade computacional do algoritmo, são necesssárias etapas de pré-processamento das imagens. Como explicado na seção sobre filtros convolucionais, os feature maps são considerados a primeira etapa pois, além de aplicar a transformação convolucional e também operam significativa redução das dimensões da imagem. Esses features maps configuram o range de filtros a serem avaliados e treinados pelo deep learning.

Para o treinamento da rede neural, são necessárias mais duas etapas. A primeira delas é o pooling, que aplica distorções e rotações na imagem de forma a enfatizar as características principais no feature map, sendo capaz de reduzir ainda mais a dimensionalidade e reduzindo também o overfitting presente na convolução. O resultado nessa etapa é uma sequência de pool maps para cada feature map reduzido. Por fim, em cada matriz de max pooling, é aplicado um flattening dimensionando cada matriz com apenas uma coluna para aplicação da rede neural densa.

Para que a rede neural seja aplicada de fato, é necessário treinamento da segmentação para diferentes inputs de imagens, de forma a relacionar os flat maps da rede com o resultado final, descartando os feature maps que são desconexos com as principais características. Para a aplicação nesse projeto, utilizaremos um classe treinada previamente e que pode ser integrada ao pré-processamento com OpenCV.

## Materiais de Referência
Além das referências principais adicionadas no resumo, foram utilizados os seguintes materiais:
K-means:
- https://docs.opencv.org/3.4/d1/d5c/tutorial_py_kmeans_opencv.html
- https://www.thepythoncode.com/article/kmeans-for-image-segmentation-opencv-python

Region Growing:
- https://www.programmersought.com/article/81151779785/
- https://developpaper.com/simple-implementation-of-region-growing-in-python/#:~:text=Region%20growing%20is%20an%20image,are%20met%2C%20region%20growth%20stops.
- https://github.com/Borda/pyImSegm

CNN Segmentation:
- https://www.pyimagesearch.com/2021/05/14/convolution-and-cross-correlation-in-neural-networks/
- https://www.pyimagesearch.com/2018/11/19/mask-r-cnn-with-opencv/

Slic:
- https://docs.opencv.org/3.4/df/d6c/group__ximgproc__superpixel.html
- https://www.programmersought.com/article/70014349754/
- https://www.pyimagesearch.com/2014/07/28/a-slic-superpixel-tutorial-using-python/

Watershed:
- https://docs.opencv.org/4.5.2/d3/db4/tutorial_py_watershed.html

Canny Edge:
- https://docs.opencv.org/3.4/da/d5c/tutorial_canny_detector.html
- https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
