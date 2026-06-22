import sys
import os

variables = {}

def yogu_error(msg, line_num):
    print(f"[Yogu Error] Linha {line_num}: {msg}")

def parse_value(val):
    val = val.strip()
    # Se for string entre aspas
    if val.startswith('"') and val.endswith('"'):
        return val[1:-1]
    # Se for número
    try:
        return float(val) if '.' in val else int(val)
    except:
        pass
    # Se for variável
    if val in variables:
        return variables[val]
    return val

def run_operation(expr):
    # Operadores: - = mais, / = multiplicar, | = dividir, : = menos
    for op_char, op_name in [('-', 'add'), ('/', 'mul'), ('|', 'div'), (':', 'sub')]:
        if op_char in expr:
            parts = expr.split(op_char, 1)
            left = parse_value(parts[0].strip())
            right = parse_value(parts[1].strip())
            try:
                if op_name == 'add':
                    return left + right
                elif op_name == 'mul':
                    return left * right
                elif op_name == 'div':
                    return left / right
                elif op_name == 'sub':
                    return left - right
            except Exception as e:
                return f"[Erro na operação: {e}]"
    return parse_value(expr)

class YoguEnd(Exception):
    pass

def run_line(line, line_num):
    line = line.strip()

    # Ignorar linhas vazias ou comentários (##)
    if not line or line.startswith('##'):
        return

    # TXT /"texto"\ — print
    if line.startswith('TXT'):
        content = line[3:].strip()
        if content.startswith('/') and content.endswith('\\'):
            inner = content[1:-1].strip()
            if inner.startswith('"') and inner.endswith('"'):
                print(inner[1:-1])
            elif inner in variables:
                print(variables[inner])
            else:
                yogu_error(f"TXT inválido: {inner}", line_num)
        else:
            yogu_error("Sintaxe TXT incorreta. Use: TXT /\"texto\"\\", line_num)

    # Ph 'variavel' — declarar variável
    elif line.startswith('Ph'):
        content = line[2:].strip()
        if content.startswith("'") and content.endswith("'"):
            var_name = content[1:-1].strip()
            if var_name not in variables:
                variables[var_name] = None
                print(f"[Yogu] Variável '{var_name}' declarada.")
            else:
                yogu_error(f"Variável '{var_name}' já existe.", line_num)
        else:
            yogu_error("Sintaxe Ph incorreta. Use: Ph 'nome'", line_num)

    # Ht 'variavel=operação' — atribuir valor/operar
    elif line.startswith('Ht'):
        content = line[2:].strip()
        if content.startswith("'") and content.endswith("'"):
            inner = content[1:-1].strip()
            if '=' in inner:
                var_name, expr = inner.split('=', 1)
                var_name = var_name.strip()
                expr = expr.strip()
                # Substituir Very e False
                if expr == 'Very':
                    expr_val = True
                elif expr == 'False':
                    expr_val = False
                else:
                    expr_val = run_operation(expr)
                if var_name in variables:
                    variables[var_name] = expr_val
                else:
                    yogu_error(f"Variável '{var_name}' não declarada. Use Ph primeiro.", line_num)
            else:
                yogu_error("Ht precisa de '='. Use: Ht 'var=valor'", line_num)
        else:
            yogu_error("Sintaxe Ht incorreta. Use: Ht 'variavel=valor'", line_num)

    # CLR — limpar terminal
    elif line == 'CLR':
        os.system('clear')

    # End — termina execução do arquivo
    elif line.lower() == 'end':
        raise YoguEnd()

    else:
        yogu_error(f"Comando desconhecido: '{line}'", line_num)

def run_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = [l.rstrip('\n') for l in f.readlines()]

        i = 0
        try:
            while i < len(lines):
                line = lines[i].strip()

                # If 'var' — condicional
                if line.startswith('If'):
                    content = line[2:].strip()
                    if content.startswith("'") and content.endswith("'"):
                        var_name = content[1:-1].strip()
                        condition = variables.get(var_name, False)
                        i += 1
                        block = []
                        while i < len(lines) and lines[i].strip().lower() != 'end':
                            block.append(lines[i])
                            i += 1
                        # Pular o End do bloco If (não é End de arquivo)
                        i += 1
                        if condition is True:
                            for j, bline in enumerate(block, 1):
                                run_line(bline, j)
                    else:
                        yogu_error("Sintaxe If incorreta. Use: If 'variavel'", i + 1)
                        i += 1
                else:
                    run_line(line, i + 1)
                    i += 1

        except YoguEnd:
            pass

    except FileNotFoundError:
        print(f"[Yogu] Arquivo '{filepath}' não encontrado.")

def print_welcome():
    print("versão 1.0 | © Yogu 2026")
    print("Bem-Vindo(a) ao Yogu.")
    print("Digite 'Go' para executar, 'sair' para sair ou 'help' para ver o tutorial.\n")

def print_tutorial():
    print("=================== TUTORIAL YOGU ===================")
    print("Comentários:")
    print("  ## Isto é um comentário e será ignorado.\n")
    print("Saída de Texto:")
    print("  TXT /\"Sua mensagem aqui\"\\     -> Exibe um texto fixo na tela.")
    print("  TXT /nome_da_variavel\\        -> Exibe o valor de uma variável.\n")
    print("Variáveis:")
    print("  Ph 'minha_var'                -> Declara uma nova variável.")
    print("  Ht 'minha_var = 10'           -> Atribui um valor ou booleano (Very/False).\n")
    print("Operações Matemáticas (Ht):")
    print("  -  : Soma         (Ex: Ht 'x = 5 - 2')  -> x vira 7")
    print("  :  : Subtração    (Ex: Ht 'x = 5 : 2')  -> x vira 3")
    print("  /  : Multiplicar  (Ex: Ht 'x = 5 / 2')  -> x vira 10")
    print("  |  : Dividir      (Ex: Ht 'x = 10 | 2') -> x vira 5\n")
    print("Condicionais:")
    print("  If 'minha_var'")
    print("      TXT /\"A condição era Very!\"\\")
    print("  End\n")
    print("Comandos do REPL:")
    print("  CLR   -> Limpa o terminal sem sumir com as instruções.")
    print("  Go    -> Executa o bloco de código enviado ao buffer.")
    print("  End   -> Finaliza a execução do bloco imediatamente.")
    print("  help  -> Abre este tutorial de ajuda.")
    print("  close -> Fecha o tutorial e volta para a tela inicial.")
    print("  sair  -> Fecha o interpretador Yogu.")
    print("=====================================================\n")

def run_repl():
    print_welcome()
    buffer = []
    while True:
        try:
            line = input("yogu> ")
            cleaned_line = line.strip()
            
            if cleaned_line.lower() == 'sair':
                print("Saindo do Yogu.")
                break
            elif cleaned_line.lower() == 'help':
                os.system('clear')
                print_tutorial()
            elif cleaned_line.lower() == 'close':
                os.system('clear')
                print_welcome()
            elif cleaned_line == 'CLR':
                os.system('clear')
                print_welcome()
            elif cleaned_line.lower() == 'go':
                if buffer:
                    # Executa o buffer acumulado
                    i = 0
                    try:
                        while i < len(buffer):
                            cur = buffer[i].strip()
                            if cur.startswith('If'):
                                content = cur[2:].strip()
                                if content.startswith("'") and content.endswith("'"):
                                    var_name = content[1:-1].strip()
                                    condition = variables.get(var_name, False)
                                    i += 1
                                    block = []
                                    while i < len(buffer) and buffer[i].strip().lower() != 'end':
                                        block.append(buffer[i])
                                        i += 1
                                    i += 1
                                    if condition is True:
                                        for j, bline in enumerate(block, 1):
                                            run_line(bline, j)
                                else:
                                    yogu_error("Sintaxe If incorreta.", i + 1)
                                    i += 1
                            else:
                                run_line(cur, i + 1)
                                i += 1
                    except YoguEnd:
                        pass
                    buffer = []  # Limpa o buffer após executar com sucesso
                else:
                    print("[Yogu] Nada para executar. Digite algumas linhas de código antes de 'Go'.")
            else:
                buffer.append(line)
        except KeyboardInterrupt:
            print("\nSaindo do Yogu.")
            break

if __name__ == '__main__':
    os.system('clear')
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        run_repl()
