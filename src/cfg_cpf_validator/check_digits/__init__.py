DIVIDER = 2


def calculate_check_digit(
    cpf: str,
    multipliers: list,
) -> int:
    sum = 0
    for i in range(len(multipliers)):
        sum += int(cpf[i]) * multipliers[i]
        remainder = sum % 11
    return 0 if remainder < DIVIDER else 11 - remainder


def calculate_check_digits(cpf) -> list:
    """
    Calcula dígitos verificadores do CPF fornecido.

    Parâmetros:
        cpf (str): CPF a ser calculado.

    Retorna:
        list: Lista com os dígitos verificadores.
    """
    # Remover caracteres não numericos do cpf
    cpf = "".join(filter(str.isdigit, cpf))

    # Cálculo do 1° digito
    multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    d1 = calculate_check_digit(cpf, multipliers)

    # Cálculo do 2° digito
    multipliers.insert(0, 11)
    d2 = calculate_check_digit(cpf, multipliers)

    return d1, d2
