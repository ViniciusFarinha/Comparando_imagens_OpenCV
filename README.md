# Comparando_imagens_OpenCV
O programa compara as imagens com computação visual e consegue diferenciar as pessoas das fotos .


### Inspiração

url: https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

### Biblioteca

Utilizando a biblioteca OpenCv, é possível realizar trabalhos de visão computacional. Um deles é a comparação de fotos de rostos de pessoas para identificar se são pessoas diferentes ou se são a mesma pessoa.

### Metodologia

* Detecção das faces com o método HOG
* Utilizar método wrap para centralizar o rosto na imagem
* Recolher os encondings da face, gerando 128 medidas do rosto da pessoa
* Detectar a pessoa com base nos encodings
