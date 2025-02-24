import cfg_cpf_validator as c

cpf = input("Insira um CPF (com ou sem formatação): ")

valid_structure, structure_derivation_tree = c.cfg.validate_structure(cpf)

d1, d2 = c.check_digits.calculate_check_digits(cpf)

valid_check_digits, check_digits_derivation_tree = c.cfg.validate_check_digits(
    cpf, d1, d2
)

valid_cpf, _, _ = c.validate(cpf)

print(f"CPF em análise: {cpf}")
print(f"Estrutura válida: {valid_structure}")
if valid_structure:
    print("Árvore de derivação da CFG de estrutura:")
    structure_derivation_tree.pretty_print()
print(f"Primeiro dígito verificador calculado: {d1}")
print(f"Segundo dígito verificador calculado: {d2}")
print(f"Dígitos verificadores válidos: {valid_check_digits}")
if valid_check_digits:
    print("Árvore de derivação da CFG de dígitos verificadores:")
    check_digits_derivation_tree.pretty_print()
print(f"CPF válido: {valid_cpf}")
