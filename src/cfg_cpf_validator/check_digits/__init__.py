import typing as t

DIVIDER = 2


def calculate_check_digit(
    cpf: t.Union[str, int],
    multipliers: list,
) -> int:
    """
    Calcula um dígito verificador com base nosw multiplicadores fornecidos.

    Parâmetros:
        cpf (str | int): CPF a ter o dígito calculado.
        multipliers (list): Lista de multiplicadores para o cálculo.

    Retorna:
        int: Dígito verificador calculado.
    """
    sum = 0
    for i in range(len(multipliers)):
        sum += int(cpf[i]) * multipliers[i]
        remainder = sum % 11
    digit = 0 if remainder < DIVIDER else 11 - remainder
    return digit


def calculate_check_digits(cpf: t.Union[str, int]) -> tuple:
    """
    Calcula dígitos verificadores do CPF fornecido.

    Parâmetros:
        cpf (str | int): CPF a ter os dígitos verificadores calculados.

    Retorna:
        tuple: Tupla com os dígitos verificadores.
    """
    cpf = "".join(filter(str.isdigit, cpf))
    multipliers = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    d1 = calculate_check_digit(cpf, multipliers)
    multipliers.insert(0, 11)
    d2 = calculate_check_digit(cpf, multipliers)
    return d1, d2
