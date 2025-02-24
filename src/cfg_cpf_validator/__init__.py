import typing as t

from cfg_cpf_validator import cfg, check_digits


def validate(
    cpf: t.Union[
        str,
        int,
    ],
) -> bool:
    """
    Valida um CPF.

    Parâmetros:
        cpf (str | int): CPF a ser validado.

    Retorna:
        bool: Indica se o CPF é válido.
    """
    cpf_structure = cfg.validate_structure(cpf)
    d1, d2 = check_digits.calculate_check_digits(cpf)
    cpf_check_digits = cfg.validate_check_digits(cpf, d1, d2)

    return cpf_structure and cpf_check_digits
