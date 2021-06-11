# Processamento de Imagens: Segmentação e Detecção de Borda (PIBITI-CBPF)

## Técnicas de Segmentação
### K-means
Processo utilizado atualmente para segmentação inicial, a quantidade de cores na segmentação é definida nas linhas de código.
O k-means prioriza as cores por ocorrência, no caso de bordar muito espessas, os grãos nem sempre são priorizados. Assim, para que um grão seja diferenciado é necessário um alto valor de k, criando segmentações de partes desprezíveis.

<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/K-means/graocolor.jpg?raw=true" width="350" title="hover text">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/K-means/graocolor_kmeans.jpg?raw=true" width="350" alt="accessibility text">
</p>
<p align="center">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/K-means/estromatolito.tiff?raw=true" width="350" title="hover text">
  <img src="https://github.com/mayribeiro15/Pibiti-CBPF/blob/main/K-means/estromatolito_kmeans.tiff?raw=true" width="350" alt="accessibility text">
</p>



### Region Growing
### CNN Segmentation
## Técnicas de Detecção de Borda
### Watershed
### Slic
### Vetorização

