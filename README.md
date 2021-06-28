# Processamento de Imagens: Segmentação e Detecção de Borda (PIBITI-CBPF)

## Técnicas de Segmentação
### K-means
Processo utilizado atualmente para segmentação inicial, a quantidade de cores na segmentação é definida nas linhas de código. O k-means prioriza as cores por ocorrência de pixels semelhantes, o que pode gerar erros em casos complexos.

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
### Slic
### Vetorização

