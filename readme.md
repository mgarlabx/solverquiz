# SolverQuiz

O SolverQuiz é um sistema para elaboração de questões no padrão Enade, de acordo com o [Guia de Elaboração e Revisão de Itens](https://download.inep.gov.br/bni/enade/guia_de_elaboracao_e_revisao_de_itens.pdf) do INEP.

## Instalação

O SolverQuiz foi concebido para funcionar com três ferramentas principais: `OpenAI`, `Zotero` e `Streamlit`.

### OpenAI

É preciso obter uma chave da API da OpenAI, a qual pode ser obtida nesse [link](https://platform.openai.com/api-keys).

### Zotero

O Zotero é um software gratuito e de código aberto que ajuda pesquisadores a coletar, organizar, citar e compartilhar referências bibliográficas e materiais de pesquisa. As referências selecionadas serão arquivadas no Zotero e utilizadas para a elaboração do texto-base das questões.

Para baixar e instalar o Zotero, ver [aqui](https://www.zotero.org/).

É preciso também instalar a extensão do Zotero para o Chrome, ver [aqui](https://chromewebstore.google.com/detail/ekhagklcjbdpajgpjgmbionohlpdbjgc).

Depois de baixar e instalar o Zotero, deve-se criar uma coleção para armazenar as referências que serão utilizadas para a geração das questões. É importante anotar a chave dessa coleção (disponível na URL da versão web do Zotero), pois será usada na configuração abaixo.

Deve ser também ser anotado o Id do usuário, bem como criada uma chave da API. Essas informações estão disponíveis nesse [link](https://www.zotero.org/settings/security).

### Streamlit

O Streamlit é uma biblioteca Python de código aberto que permite criar e compartilhar rapidamente aplicativos web personalizados para ciência de dados e aprendizado de máquina, utilizando apenas algumas linhas de código Python.

O SolverQuiz foi desenvolvido para rodar totalmente em Python, através do Streamlit. Portanto, é preciso de alguma experiência nessa biblioteca para instalar e rodar o SolverQuiz. Clique [aqui](https://streamlit.io/) para saber mais sobre o Streamlit.

Após baixar os códigos do Github, é preciso criar uma pasta chamada `.streamlit` e nela criar o arquivo `secrets.toml` com o seguinte conteúdo:

```
OPENAI_API_KEY = "SUA-CHAVE-DA-API-DA-OPENAI"
ZOTERO_API_KEY = "SUA-CHAVE-DA-API-DO-ZOTERO"
ZOTERO_USER_ID = "SEU-USER-ID-DO-ZOTERO"
ZOTERO_COLLECTION_KEY = "SUA-CHAVE-DA-COLECAO-DO-ZOTERO"

[connections.questoes_db]
url = "sqlite:///questoes.db"
```

## Funcionamento

O funcionamento do SolverQuiz está organizado em cinco etapas:

### 1. Selecionar

Nessa etapa é feita a escolha do curso para o qual será elaborada a questão, bem como o assunto relacionado. A lista de assuntos para cada curso foi constituída a partir do respectivo edital, cuja portaria na íntegra se encontra disponível no link da página.

### 2. Buscar

Com base no curso e assunto escolhidos, o SolverQuiz faz uma busca de artigos e notícias relacionados. Esses artigos serão usados na definição do "texto-base" a partir do qual a questão será elaborada. Será exibida uma lista e o usuário deverá visitar os sites sugeridos. Aqueles que forem considerados como válidos, deverão ser salvos usando a extensão do Zotero no Chrome. É possível também adicionar referências diretamente no Zotero, a partir de outras fontes que forem consideradas convenientes.

### 3. Listar

Essa tela irá exibir os artigos selecionados para uma revisão e escolha daquele que será usado para a elaboração da questão. Há dois botões nessa tela. Um para `selecionar` o artigo desejado e outro para `excluir` o artigo, caso desejado.

### 4. Elaborar

É nessa tela que é feita a elaboração da questão propriamente dita. Há opções para a escolha do tipo de questão (resposta única, resposta múltipla e asserção/razão), bem como para o grau de dificuldade (fácil, média e difícil). Após ser criada, se o usuário ficar satisfeito com o resultado, há um botão para `salvar` a questão no banco de dados.

### 5. Consultar

Nessa etapa são listadas as questões selecionadas. Nesse momento, é possível `editar` o conteúdo de cada questão, fazendo pequenos ajustes que eventualmente sejam necessários. Além disso, é possível `baixar` a questão no formato JSON (para ser importada em outros sistemas), bem como `excluir` se for o caso.


