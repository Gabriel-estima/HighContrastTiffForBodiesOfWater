
# Guia básico para utilizar esse mini arquivo (para usuários de debian/ubuntu)

## O que deve ser instalado antes de começar?

- todas as dependencias básicas de python: python3, pip (utilizados para interpretar e instalar pacotes de python)
- com o pip, intalar pillow e numpy: 'pip install pillow' e 'pip install numpy' (pacotes utilizados para manipular imagens)
- pacote de modificação de metadata de arquivos tiff/tif: 'sudo apt install libimage-exiftool-perl' (pacote utilizado para recuperar metadata geográfica de arquivos tiff) 

#### Obs.: arquivos extras -> "google earth pro" para verificar se as imagens são visíveis e sua metadata está correta

## Como utilizar esse mini arquivo para gerar GeoTiff's com highlights da hidrografia local? 

1. Depois de instalar os pacotes necessários, deve-se colocar a pasta "\bin" no PATH do sistema, para que os scripts em python e bash possam ser acessados onde forem requisitados 

2. Para gerar imagens com contraste razoável entre áreas "encharcadas" e "secas", deve-se utilizar como base as imagens: "VV - decibel gamma0" e "VH - decibel gamma0" encontradas na aba de download de imagens do site [Copernicus Browser](https://browser.dataspace.copernicus.eu) 

3. Depois, de baixar o arquivo zip com as imagens tiff em uma pasta vazia, como a "\imagens" presente neste arquivo, executar o comando "mergeGeoAll". Esse script bash extrai as imagens base, cria a imagem de alto contraste a partir delas, reconstitui a metadata geográfica e depois remove as imagens extraídas (a menos que a flag "-k" seja usada depois do comando para manter as imagens extraídas) 

#### Obs2.: Neste arquivo já existem duas imagens prontas para tomar como base o resultado esperado do algorítimo, junto com o arquivo zip com as imagens de base



