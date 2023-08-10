# Comparação de Algoritmos de Busca em Arrays e Arquivos

Este projeto analisa e compara a eficiência de diferentes algoritmos de busca, especificamente busca linear e binária, quando aplicados a arrays e arquivos.

## 📌 Índice

- [Introdução](#-introdução)
- [Dependências](#-dependências)
- [Estrutura de Dados](#-estrutura-de-dados)
- [Algoritmos de Busca](#-algoritmos-de-busca)
- [Medição de Performance](#-medição-de-performance)
- [Testes em RAM vs. Disco](#-testes-em-ram-vs-disco)
- [Salvando Resultados](#-salvando-resultados)
- [Como Usar](#-como-usar)

## 🚀 Introdução

O projeto foi desenvolvido para avaliar a eficiência de algoritmos de busca em diferentes cenários: busca em arrays (na memória RAM) e busca em arquivos (no disco). Através de testes práticos, o projeto mede o tempo necessário para encontrar um valor específico, fornecendo insights sobre a performance de cada método.

## 📦 Dependências

- **Numpy**: Uma biblioteca em Python usada para operações matemáticas e manipulação de arrays. No projeto, é usada para criar e manipular arrays, bem como para ler e escrever dados em arquivos no formato binário.

## 📚 Estrutura de Dados

- **Arrays**: São estruturas de dados que armazenam uma coleção de itens em posições contíguas na memória. No projeto, utilizamos arrays do Numpy devido à sua eficiência e facilidade de manipulação.

## 🔍 Algoritmos de Busca

- **Busca Linear**: Este algoritmo percorre cada elemento do array (ou arquivo) sequencialmente até encontrar o elemento desejado ou até chegar ao final da estrutura.
  
- **Busca Binária**: Requer que os dados estejam ordenados. O algoritmo divide repetidamente o intervalo de busca pela metade até encontrar o elemento desejado ou até que o intervalo esteja vazio.

## ⏱ Medição de Performance

- **Tempo de Busca**: Utilizamos a função `perf_counter` do módulo `time` para medir o tempo de execução de cada busca. Esta função fornece uma contagem de tempo de alta resolução, ideal para medir curtos períodos de tempo.

- **Cálculo da Média**: Para obter uma estimativa mais precisa do tempo de busca, cada algoritmo é executado várias vezes (padrão é 10) e o tempo médio é calculado.

## 💽 Testes em RAM vs. Disco

- **Testes em RAM**: Os algoritmos de busca são aplicados diretamente aos arrays criados na memória RAM.
  
- **Testes em Disco**: Os dados do array são primeiro escritos em um arquivo no formato binário. Os algoritmos de busca são então aplicados ao arquivo, lendo os dados diretamente do disco.

## 📂 Salvando Resultados

- **Formato JSON**: Os resultados dos testes, incluindo o tamanho da RAM utilizada, o elemento procurado e os tempos de busca, podem ser salvos em um arquivo JSON para análise posterior.

## 🖥 Como Usar

1. Execute o código.
2. No menu interativo, escolha o tipo de busca e o local (array ou arquivo) ou opte por executar todos os testes de uma vez.
3. Se escolher uma busca específica, defina o tamanho dos dados e o valor a ser buscado.
4. O programa executará a busca e exibirá o tempo médio de execução e o resultado.
5. Você pode optar por salvar os resultados em um arquivo JSON para análise posterior.

###### Agradecimentos a Danilo pela ajuda e ideia 👍
