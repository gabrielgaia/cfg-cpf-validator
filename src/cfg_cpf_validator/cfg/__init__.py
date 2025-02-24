import typing as t

import jinja2 as jinja
import nltk as n

CFG_STRUCTURE = n.CFG.fromstring(
    """
    S -> D D D D D D D D D D D | D D D '.' D D D '.' D D D '-' D D
    D -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    """
)

CFG_CHECK_DIGITS_PRODUCTIONS_TEMPLATE = """
    S -> FCD SCD
    FCD -> '{{ check_digit_1 }}'
    SCD -> '{{ check_digit_2 }}'
"""

structure_parser = n.parse.ChartParser(CFG_STRUCTURE)


def validate_structure(
    cpf: t.Union[
        str,
        int,
    ],
) -> tuple:
    """
    Valida estrutura de um CPF com base em uma Gramática Livre de Contexto.

    Parâmetros:
        cpf (str | int): CPF a ser validado.

    Retorna:
        tuple: Tupla contendo um boolean indicando se a estrutura do CPF é
        valida e um objeto `nltk.tree.Tree` com as derivações do CPF na CFG.
    """
    tokens = list(str(cpf))
    tree = next(structure_parser.parse(tokens))
    return bool(tree), tree


def validate_check_digits(
    cpf: t.Union[str, int],
    check_digit_1: t.Union[str, int],
    check_digit_2: t.Union[str, int],
):
    """
    Valida os dígitos verificadores de um CPF com base em uma Gramática Livre
    de Contexto feita com os dígitso verificadores passados como argumento.

    Parâmetros:
        cpf (str | int): CPF a ter seus dígitos verificadores validados.
        check_digit_1 (str | int): Número que deve ser o primeiro dígito
        verificador do CPF.
        check_digit_2 (str | int): Número que deve ser o segundo dígito
        verificador do CPF.

    Retorna:
        tuple: Tupla contento um boolean indicando se os dígitos verificadores
        do CPF estão corretos e um objeto `nltk.tree.Tree` com as derivações dos
        dígitos verificadores na CFG.
    """
    cfg_check_digits_productions = jinja.Template(
        CFG_CHECK_DIGITS_PRODUCTIONS_TEMPLATE
    ).render(check_digit_1=check_digit_1, check_digit_2=check_digit_2)

    cfg_check_digits = n.CFG.fromstring(cfg_check_digits_productions)

    check_digits_parser = n.parse.ChartParser(cfg_check_digits)

    tokens = list(str(cpf)[-2:])
    try:
        tree = check_digits_parser.parse(tokens)
        return bool(tree), tree
    except ValueError:
        return False
