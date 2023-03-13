# Best sallers mercado livre

Este script em Python utiliza a biblioteca `requests` para fazer requisições à API do Mercado Livre. O objetivo do script é permitir que o usuário selecione uma categoria de produtos do Mercado Livre e, em seguida, listar os produtos mais vendidos nessa categoria.

## Pré-requisitos
- Python 3.x
- Biblioteca requests

## Utilização
1. Baixe o script e salve-o em um arquivo com extensão `.py`
2. Certifique-se de que a biblioteca requests esteja instalada. Caso não esteja, execute o comando `pip install requests no terminal`.
3. Execute o script com o comando `python nome_do_arquivo.py`.
4. Siga as instruções apresentadas no console para selecionar a categoria desejada e visualizar os produtos mais vendidos.

## Funcionamento do Script
O script começa importando as bibliotecas necessárias `requests` e `os`. Em seguida, há duas variáveis que representam a URL base da API do Mercado Livre e uma URL que lista os produtos mais vendidos na categoria de eletrônicos.

A função `choose_category` faz uma requisição à API do Mercado Livre para listar as categorias disponíveis e exibe as opções para o usuário. Após o usuário selecionar a categoria desejada, a função retorna a categoria escolhida.

A função `best_sellers` recebe como parâmetro a categoria selecionada e faz uma nova requisição à API do Mercado Livre para listar os produtos mais vendidos nessa categoria. Os produtos são exibidos no console juntamente com seus respectivos títulos.