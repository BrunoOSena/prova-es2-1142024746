from senha import senha_valida, MINIMO


def test_senha_exatamente_minimo():
    senha = "a" * MINIMO
    resultado = senha_valida(senha)
    assert resultado is True


def test_senha_minimo_menos_um():
    senha = "a" * (MINIMO - 1)
    resultado = senha_valida(senha)
    assert resultado is False


def test_senha_vazia():
    senha = ""
    resultado = senha_valida(senha)
    assert resultado is False


def test_senha_apenas_espacos():
    senha = " " * (MINIMO + 2)
    resultado = senha_valida(senha)
    assert resultado is False
