import sys

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
            # Pode ser variável ou string
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
                if var_name in variables:
                    variables[var_name] = run_operation(expr)
                else:
                    yogu_error(f"Variável '{var_name}' não declarada. Use Ph primeiro.", line_num)
            else:
                yogu_error("Ht precisa de '='. Use: Ht 'var=valor'", line_num)
        else:
            yogu_error("Sintaxe Ht incorreta. Use: Ht 'variavel=valor'", line_num)

    else:
        yogu_error(f"Comando desconhecido: '{line}'", line_num)

def run_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            run_line(line, i)
    except FileNotFoundError:
        print(f"[Yogu] Arquivo '{filepath}' não encontrado.")

def run_repl():
    print("Yogu 0.1 — digite 'sair' para sair\n")
    line_num = 1
    while True:
        try:
            line = input("yogu> ")
            if line.strip().lower() == 'sair':
                print("Saindo do Yogu.")
                break
            run_line(line, line_num)
            line_num += 1
        except KeyboardInterrupt:
            print("\nSaindo do Yogu.")
            break

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        run_repl()
