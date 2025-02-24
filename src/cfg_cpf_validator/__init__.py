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
        tuple: Tupla contendo um boolean indicando se o CPF é válido, um objeto
        `nltk.tree.Tree` contendo as derivações do CPF na CFG e outro objeto
        `nltk.tree.Tree` contendo as derivações dos dígitos verificadores na
        CFG.
    """
    cpf_valid_structure, cpf_structure_derivation_tree = cfg.validate_structure(
        cpf
    )
    d1, d2 = check_digits.calculate_check_digits(cpf)
    cpf_valid_check_digits, cpf_check_digits_derivation_tree = (
        cfg.validate_check_digits(cpf, d1, d2)
    )

    return (
        (cpf_valid_structure and cpf_valid_check_digits),
        cpf_structure_derivation_tree,
        cpf_check_digits_derivation_tree,
    )
