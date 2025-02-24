import cfg_cpf_validator as c

cpf = input("Insira um CPF (com ou sem formatação): ")

valid_structure, derivation_tree = c.cfg.validate_structure(cpf)

d1, d2 = c.check_digits.calculate_check_digits(cpf)

valid_check_digits = c.cfg.validate_check_digits(cpf, d1, d2)

valid_cpf, _ = c.validate(cpf)

print(f"CPF em análise: {cpf}")
print(f"Estrutura válida: {valid_structure}")
print(f"Primeiro dígito verificador calculado: {d1}")
print(f"Segundo dígito verificador calculado: {d2}")
print(f"Dígitos verificadores válidos: {valid_check_digits}")
print(f"CPF válido: {valid_cpf}")
print("Árvore de derivação da CFG de estrutura:")
derivation_tree.pretty_print()
