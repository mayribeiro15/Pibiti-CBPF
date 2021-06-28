# Processamento de Imagens: Segmentação e Detecção de Borda (PIBITI-CBPF)

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


### Region Growing
### CNN Segmentation
## Técnicas de Detecção de Borda
### Watershed
O algortimo do watershed de baseia na divisão de regiões segundo a ideia de um fluxo de água partindo das bordas da imagem e passando pelas regiões de maior contraste, ou seja, as bordas da região de interesse. 
Após a imagem ser processada, é necessário aplicar transformações de threshold, closing e opening para que esta esteja apta a gerar uma detecção de bora efetva. O threshold realiza o filtro dos valores a serem considerados, reduzindo a variedade nos valores de pixels; a função closing destaca a região central dos pontos de interesse, gerando a região de certeza, chama sure foreground; por fim, a função opening realiza a dilatação dos pontos, a partir da qual podemos obter o que chamamos de sure background, ou seja, a parte da imagem que pode ser desconsiderada já que está a uma margem segura dos pontos de interesse. Dessa forma, a região possível para detecção de borda é limitada ao espaço entre o sure foreground e o sure background e a função do watershed pode ser aplicada com maior rendimento. 
Esse algoritmo é utilizado atualmente por ser efetivo na maioria dos casos embora a maior dificuldade seja aplicar pré-processamento necessário.

Em casos mais simplificados o algoritmo apresenta uma boa segmentação apenas com o pré-processamento acima. No exemplo abaixo, o resultado do watershed foi plotado sobre a imagem para melhor visualização.
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Watershed/coins.jpg" width="350">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Watershed/coins_watershed.jpg" width="350">
</p>

Em casos em que a região de interesse possui maiores variações, é vantajoso utilizar algoritmos de segmentação no pré-processamento. No exemplo abaixo, temos um comparativo da aplicação direta do watershed e da aplicação após o uso da segmentação por k-means.
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Watershed/estromatolito_watershed.jpg" width="350">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/Watershed/estromatolito_watershed_kmeans.jpg" width="350">
</p>

### Slic
### Vetorização

