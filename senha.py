MINIMO = 12

def senha_valida(senha):
    if not senha or senha.isspace():
        return False
    return len(senha) >= MINIMO
