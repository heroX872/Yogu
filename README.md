# 🟡 Linguagem de Programação Yogu

O **Yogu** é uma linguagem de programação interpretada simples, com uma sintaxe própria e única, desenvolvida em Python.
Criada por [HeroX872](https://github.com/HeroX872)

---

## 🚀 Como Começar

### Requisitos
- Python 3.x

### Executando o Yogu

**Modo Interativo (REPL / Console):**
```bash
python yogu.py

```
**Executando um arquivo diretamente:**
```bash
python yogu.py nome_do_arquivo.yg

```
## 📖 Sintaxe e Comandos
### 🖨️ Saída de Texto — TXT
Exibe um texto fixo ou o valor de uma variável na tela.
```yogu
TXT /"Olá Mundo"\
TXT /nomeDaVariavel\

```
### 📦 Declarar Variável — Ph
Cria uma nova variável no sistema.
```yogu
Ph 'minhaVar'

```
### ⚙️ Atribuir / Operar — Ht
Atribui um valor ou realiza uma operação matemática. Também aceita os booleanos Very (verdadeiro) e False (falso).
```yogu
Ht 'minhaVar=10'
Ht 'status=Very'

```
### 🔀 Condicionais — If / End
Executa um bloco de código se a variável testada for verdadeira (Very).
```yogu
Ph 'estaPronto'
Ht 'estaPronto=Very'

If 'estaPronto'
    TXT /"Sistema online"\
End

```
## ➕ Operadores
O Yogu usa um conjunto próprio de operadores, invertidos por padrão:
| Símbolo | Operação | Significado Tradicional |
|---|---|---|
| - | Soma | + |
| : | Subtração | - |
| / | Multiplicação | * |
| | | Divisão | / |
### Exemplos:
```yogu
Ph 'x'
Ht 'x=5-3'
TXT /x\

```
> Saída: 8 *(5 + 3)*
> 
```yogu
Ph 'y'
Ht 'y=10/2'
TXT /y\

```
> Saída: 20 *(10 × 2)*
> 
## 💬 Comentários
Use ## para escrever comentários. Eles são totalmente ignorados pelo interpretador.
```yogu
## Isto é um comentário
TXT /"Yogu é massa"\

```
## 💻 Comandos do Console (REPL)
Quando estiver usando o modo interativo, você pode gerenciar o código digitado com estes comandos:
 * Go — Executa todo o bloco de código que está guardado no buffer atual.
 * CLR — Limpa a tela do terminal sem apagar o código que você já digitou.
 * save — Limpa a tela e pede o nome do arquivo para salvar seu código direto na raiz da pasta Download/ com a extensão .yg.
 * edit — Sobrescreve um arquivo .yg existente na pasta Download/ com o código que está no seu buffer atual.
 * procurar — Limpa a tela, busca um arquivo .yg na sua pasta Download/ e carrega o código dele direto no console para você rodar com o Go.
 * help — Abre o tutorial interno de ajuda.
 * close — Fecha o tutorial e restaura exatamente o código que você estava digitando antes.
 * sair — Fecha o interpretador Yogu.
## 📄 Exemplo Completo
```yogu
## Testando variáveis e condições no Yogu

Ph 'num'
Ht 'num=4/5'

Ph 'checar'
Ht 'checar=Very'

If 'checar'
    TXT /"O resultado é:"\
    TXT /num\
End

```
**Saída:**
```
O resultado é:
20

```
## 📁 Extensão de Arquivo e Caminhos
Os arquivos de código do Yogu usam a extensão .yg. No Android (Termux ou Pydroid 3), o sistema salva e busca os arquivos diretamente na raiz do seu armazenamento público:
```
/sdcard/Download/

```
## 🛠️ Status do Projeto
O Yogu está em desenvolvimento ativo. Próximas novidades planejadas:
 * Laços de repetição (While / For)
 * Entrada de dados pelo usuário (Input)
 * Suporte a quebras de linha dentro do TXT
## 📜 Licença
Licença MIT — Livre para usar, modificar e distribuir.
> Feito com 💛 por HeroX872
> 
```
