import typing as t

from cfg_cpf_validator import cfg, check_digits


def validate(
    cpf: t.Union[
        str,
        int,
    ],
) -> tuple:
    """
    Valida um CPF.

    Parâmetros:
        cpf (str | int): CPF a ser validado.

    Retorna:
        tuple: Tupla contendo um boolean indicando se o CPF é válido e uma
        lista com as derivações do CPF na CFG.
    """
    cpf_structure, cpf_derivation_tree = cfg.validate_structure(cpf)
    d1, d2 = check_digits.calculate_check_digits(cpf)
    cpf_check_digits = cfg.validate_check_digits(cpf, d1, d2)

    return (cpf_structure and cpf_check_digits), cpf_derivation_tree
