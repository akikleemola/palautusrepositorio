import re

from matchers import QueryBuilder


_TOKEN_PATTERN = re.compile(r"\s*(>=|=|<|[A-Za-z_][A-Za-z0-9_]*|[+-]?\d+)")
_IDENTIFIER_PATTERN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
_INTEGER_PATTERN = re.compile(r"[+-]?\d+")


def _tokenize(query):
    tokens = []
    position = 0

    while position < len(query):
        match = _TOKEN_PATTERN.match(query, position)
        if match is None:
            if query[position:].strip() == "":
                break

            raise ValueError("Invalid query syntax")

        tokens.append(match.group(1))
        position = match.end()

    return tokens


def _add_condition(builder, tokens):
    if len(tokens) != 3:
        raise ValueError("Invalid query syntax")

    first, operator, value = tokens

    if first == "team" and operator == "=":
        if _IDENTIFIER_PATTERN.fullmatch(value) is None:
            raise ValueError("Invalid team name")

        return builder.plays_in(value)

    if (
        _IDENTIFIER_PATTERN.fullmatch(first) is None
        or first in ("and", "or")
        or _INTEGER_PATTERN.fullmatch(value) is None
    ):
        raise ValueError("Invalid query condition")

    number = int(value)

    if operator == ">=":
        return builder.has_at_least(number, first)

    if operator == "<":
        return builder.has_fewer_than(number, first)

    raise ValueError("Invalid query operator")


def _split_on(tokens, separator):
    groups = []
    current_group = []

    for token in tokens:
        if token == separator:
            if not current_group:
                raise ValueError("Invalid query syntax")

            groups.append(current_group)
            current_group = []
        else:
            current_group.append(token)

    if not current_group:
        raise ValueError("Invalid query syntax")

    groups.append(current_group)
    return groups


def parse(query):
    tokens = _tokenize(query)
    or_groups = _split_on(tokens, "or")
    queries = []

    for or_group in or_groups:
        conditions = _split_on(or_group, "and")
        builder = QueryBuilder()

        for condition in conditions:
            builder = _add_condition(builder, condition)

        queries.append(builder)

    if len(queries) == 1:
        return queries[0].build()

    return QueryBuilder().one_of(*queries).build()
