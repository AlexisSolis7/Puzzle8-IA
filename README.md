# Solucionador do 8-Puzzle - Versão Interativa Web

## Visão Geral
Este projeto é um solucionador interativo e didático para o clássico problema do 8-puzzle, desenvolvido para uso em disciplinas de Inteligência Artificial na universidade. Possui uma interface web baseada em Python e Flask, permitindo aos usuários visualizar e experimentar o algoritmo de busca A* e dois heurísticos: distância de Manhattan e peças fora do lugar.

## Funcionalidades
- **Interface Web Interativa:** Configure facilmente os estados inicial e final, execute o solucionador e visualize cada etapa.
- **Algoritmo de Busca A*:** Encontra o caminho mais curto de forma eficiente.
- **Heurísticas:** Escolha entre distância de Manhattan e peças fora do lugar para fins didáticos.
- **Verificação de Solubilidade:** Garante que apenas quebra-cabeças solucionáveis sejam processados.
- **Visualização Passo a Passo:** Veja cada movimento e o raciocínio por trás dele.
- **Comentários Didáticos:** O código é anotado para uso em sala de aula e autoestudo.

## Primeiros Passos
### Pré-requisitos
- Python 3.7+
- Flask

### Instalação
1. Clone este repositório:
   ```powershell
   git clone <url-do-seu-repositorio>
   cd IA
   ```
2. Instale o Flask:
   ```powershell
   pip install flask
   ```

### Executando a Aplicação Web
1. Inicie o servidor:
   ```powershell
   python AStarPuzzleInteractiveWeb.py
   ```
2. Abra o navegador e acesse `http://127.0.0.1:5000`

## Como Usar
- **Defina os Estados Inicial e Final:** Use a interface web para inserir os estados do quebra-cabeça.
- **Escolha o Heurístico:** Selecione Manhattan ou peças fora do lugar.
- **Resolver:** Clique em 'Resolver' para executar o algoritmo A* e visualizar a solução.
- **Avance pelos Passos:** Use os botões de navegação para ver cada movimento.

## Estrutura de Arquivos
- `AStarPuzzleInteractiveWeb.py`: Aplicação principal Flask com toda a lógica e frontend.
- `AStarPuzzleTerminal.py`: Solucionador via terminal para testes rápidos (opcional).
- `README.md`: Documentação do projeto.

## Notas Didáticas
- O código é amplamente comentado para explicar cada função e etapa do algoritmo.
- O frontend foi projetado para clareza, tornando-o adequado para demonstrações em sala de aula.
- A solubilidade é verificada pelo método de inversões, garantindo que apenas quebra-cabeças válidos sejam resolvidos.

## Algoritmos
### Busca A*
- Explora o espaço de estados do quebra-cabeça usando uma fila de prioridade.
- Utiliza heurísticas para estimar o custo até o objetivo.
- Retorna o caminho mais curto se o quebra-cabeça for solucionável.

### Heurísticas
- **Distância de Manhattan:** Soma das distâncias de cada peça até sua posição final.
- **Peças Fora do Lugar:** Contagem de peças que não estão na posição correta.

## Solubilidade
- O quebra-cabeça só é solucionável se o número de inversões for par.
- O aplicativo verifica isso antes de tentar resolver.

## Personalização
- Você pode modificar o código para adicionar novos heurísticos ou alterar o estilo da visualização.
- Para uso em sala de aula, ajuste os comentários e a interface conforme necessário.

## Licença
Este projeto é para uso educacional. Você pode modificar e compartilhar para fins acadêmicos e em sala de aula.

## Autor
- [Alexis Solis]
- [Laura Soares]
- [Universidade Federal de Santa Catarina]
- [Disciplina: Inteligência Artificial]

---
Para dúvidas ou sugestões de melhorias, abra uma issue ou envie um pull request.
