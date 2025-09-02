## 📝 Introdução 

Este repositório reúne **atividades práticas e desafios desenvolvidos para aprendizado de Python e Flet**.
O objetivo foi explorar desde conceitos básicos da linguagem até a criação de interfaces gráficas modernas com Flet, praticando:

* Estruturação de projetos em Python

* Manipulação de componentes visuais

* Estilização e personalização de elementos

* Interatividade e navegação entre páginas

Esses exercícios serviram como etapas de aprendizado, consolidando fundamentos de programação e introduzindo o uso de Flet para criação de aplicativos web e mobile.


<br>

## 🛠️ Tecnologias Utilizadas

* **Python** → linguagem principal usada no desenvolvimento.

* **Flet** → framework para criação da interface gráfica (apps web e mobile com Python).

* **Visual Studio Code** → editor de código utilizado para escrever e organizar o projeto.

* **Git/GitHub** → versionamento e hospedagem do repositório.


<br> 

## 💻 Comandos Utilizados no Terminal

### 🔹 Ambiente Virtual
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 🔹 Instalação de Dependências
```bash
pip install flet-desktop
pip show flet
```

### 🔹 Execução do Projeto
```bash
flet run --web nomeprojeto.py
```

<br>

## 📘 Atividades Realizadas

### 1. Criar um app simples exibindo “Hello World": <br>
 Primeiro app simples com Flet, exibindo textos estilizados na página, configurando título, cores, tamanho e alinhamento, e aprendendo a adicionar elementos e iniciar o aplicativo com `ft.app()`. <br> <br>
<img width="749" height="872" alt="ex_01" src="https://github.com/user-attachments/assets/e1937538-74d3-4084-9619-766c1c49f246" />

<br> 
 
### 2. Botão Interativo: <br> 
  Botão interativo que altera o texto exibido na página ao ser clicado, ensinando como associar funções a eventos, modificar elementos da interface dinamicamente e atualizar a tela com `page.update()` em Flet. <br> <br>

  <img width="751" height="876" alt="ex_02" src="https://github.com/user-attachments/assets/4dc34c5b-b9c1-42cf-9b8a-0de5882bc5f8" />

<br> 

### 3. Campo de Texto Interativo: <br>

  Campo de texto interativo onde o usuário digita seu nome e, ao clicar em um botão, a aplicação valida a entrada e exibe uma mensagem personalizada na tela, demonstrando como capturar valores de entrada, realizar verificações e atualizar dinamicamente a interface em Flet.
  
<br> <br>
  <img width="749" height="868" alt="ex_03" src="https://github.com/user-attachments/assets/6eead780-9bd4-4982-81c5-9c1579504fa3" />

<br> 

### 4. Seletor de Cores Interativo: <br>
  Seletor de cores interativo usando um dropdown, permitindo que o usuário escolha uma cor e a aplicação altere dinamicamente a cor de um container, mostrando como vincular eventos de seleção a mudanças visuais na interface em Flet. <br> <br>

<img width="745" height="870" alt="ex_04_a" src="https://github.com/user-attachments/assets/c5dc333d-ab87-460e-ae44-a1b524cbb4f1" />
<img width="750" height="873" alt="ex_04_b" src="https://github.com/user-attachments/assets/1d0159b4-c96a-400c-bce1-1c873c99ba81" />
<img width="750" height="875" alt="ex_04_c" src="https://github.com/user-attachments/assets/b20bd6b5-23bb-4c23-bb48-7f0d15a59dde" />

  
### 5. Layout Básico: <br>

Layout organizado usando `Row` e `Column`, combinando botões e caixas coloridas, para aprender a estruturar elementos visualmente na tela, controlar alinhamento, espaçamento e hierarquia dentro de um app Flet. <br> <br>

<img width="750" height="870" alt="ex_05" src="https://github.com/user-attachments/assets/fbf0ecb3-d752-46e9-a5f2-a4d00a2f569d" />

<br>

### 6. Contador: <br>
Contador completo com botões de incrementar, decrementar e resetar, que altera dinamicamente o valor exibido e sua cor dependendo se é positivo, negativo ou zero, demonstrando manipulação de variáveis, eventos e atualização da interface em Flet. <br> <br>
<img width="749" height="876" alt="ex_06" src="https://github.com/user-attachments/assets/1cf4c46f-c74e-4458-96a3-60b084d08010" />
<br>

### 7. Calculadora: <br>

  Calculadora simples que realiza operações básicas (soma, subtração, multiplicação e divisão), validando entradas do usuário e exibindo o resultado dinamicamente, ensinando manipulação de campos de texto, dropdowns, eventos de clique e atualização da interface em Flet. <br> <br>

<img width="735" height="873" alt="ex_07" src="https://github.com/user-attachments/assets/2186b4d1-3f4f-4a5c-94cc-d661669a09f3" />

<br> 

### 8. Painel de Configuração: <br>
  Painel de configuração interativo que permite modificar o estilo e as cores de um texto em tempo real, incluindo negrito, itálico, sublinhado, tamanho da fonte e cores de texto e fundo, mostrando como vincular múltiplos controles a atualizações dinâmicas da interface em Flet. <br> <br>

  <img width="750" height="875" alt="ex_08" src="https://github.com/user-attachments/assets/c80fe5cc-9c28-4213-830f-4b55afdd275c" />

  <br>

### 9.  Galeria de Cards: <br>

  Zoológico Virtual interativo que exibe animais em cards coloridos com emoji, nome e descrição. O app permite filtrar por categoria, tamanho ou buscar por nome, atualizando dinamicamente os resultados e mostrando um contador de animais exibidos. Além disso, inclui um botão para limpar todos os filtros, demonstrando manipulação de listas, filtragem de dados e atualização da interface com Flet. <br> <br>
<img width="745" height="873" alt="ex_09" src="https://github.com/user-attachments/assets/7aa8b38f-a803-47a4-b5cd-f8cf0ea59792" />

<br>
  
### 10.  Multipáginas: <br>

O aplicativo multi-página desenvolvido com Flet possui as páginas Home, Perfil, Configurações e Sobre, navegáveis por uma barra inferior fixa que destaca a página ativa. Na Home há boas-vindas e instruções, no Perfil são exibidos dados do usuário e a possibilidade de ganhar pontos, nas Configurações é possível alterar modo escuro, notificações e som, e na Sobre há informações do app. O layout utiliza Stack e Column para organização, mantendo o estado do usuário de forma dinâmica. <br> <br>

<img width="747" height="869" alt="ex_10_a" src="https://github.com/user-attachments/assets/2ca27563-40e2-4b1c-a09e-2f6e4fe94f9c" />
<img width="751" height="872" alt="ex_10_d" src="https://github.com/user-attachments/assets/196b06b4-465a-419e-86ea-af33372dc97b" />
<img width="746" height="873" alt="ex_10_c" src="https://github.com/user-attachments/assets/b7309939-eb0a-41f1-8d76-46f615416c57" />
<img width="752" height="873" alt="ex_10_b" src="https://github.com/user-attachments/assets/21f43b07-ee7c-4a97-863f-605a2bf2fe1a" />

<br>

## 🏆 Desafios

### Desafio 5_a - Hobbys: <br>

Criador de Perfil desenvolvido com Flet, permitindo ao usuário preencher nome, idade e selecionar um hobby favorito. Após a validação dos dados, o app gera um cartão visual exibindo o nome, idade com categoria etária, hobby e um ícone colorido representativo. Além disso, inclui feedback de erros, botões para criar e limpar o perfil, e um layout centralizado e interativo que atualiza dinamicamente conforme as ações do usuário. <br> <br>

<img width="752" height="873" alt="ex_5_desafio" src="https://github.com/user-attachments/assets/236debfd-faa0-48de-86de-bbdb2750d365" />
<img width="1919" height="879" alt="ex_5a_desafio" src="https://github.com/user-attachments/assets/6bf862d8-bfc5-49cb-b608-bde96057652b" />
<img width="1919" height="877" alt="ex_5a_desafio2" src="https://github.com/user-attachments/assets/9a5ff1ba-095e-4174-9730-5d21690121e8" />

<br>

### Desafio 10_a - Lista de Tarefas: <br>

Lista de Tarefas Interativa desenvolvida com Flet, permitindo que o usuário adicione, conclua e exclua tarefas de forma dinâmica. O app exibe um campo para nova tarefa, botões para adicionar, limpar todas, excluir concluídas e concluir todas, e atualiza automaticamente o status mostrando o total de tarefas, quantas estão concluídas e quantas estão pendentes. Cada tarefa possui uma checkbox para marcar como concluída e um ícone para exclusão individual, proporcionando controle completo e visual intuitivo das tarefas. <br> <br>

<img width="750" height="873" alt="ex_10_desafio" src="https://github.com/user-attachments/assets/a6fd979f-1e73-46b7-af40-0d25cb42827e" />

<br> <br>


## ✅ Conclusão

Ao longo das atividades desenvolvidas, exploramos diferentes possibilidades de criação de interfaces interativas com Flet, aplicando conceitos de programação, lógica e design de forma prática. Foram criados aplicativos variados, como calculadora, painel de configuração de textos, galeria de animais com filtros, app multi-página, criador de perfis e lista de tarefas, cada um destacando funcionalidades específicas como manipulação de dados, validação de entradas, filtros dinâmicos, gerenciamento de estado e navegação entre páginas. Esses projetos demonstram a capacidade de combinar Python com interfaces gráficas modernas, tornando aplicações úteis, interativas e visualmente atraentes, ao mesmo tempo que reforçam habilidades de lógica, organização e boas práticas de desenvolvimento.
