def centrar(janela, largura, altura):
    larguratela = janela.winfo_screenwidth()
    alturatela = janela.winfo_screenheight()
    posicaox = larguratela//2 - largura//2
    posicaoy = alturatela//2 - altura//2

    return f"{largura}x{altura}+{posicaox}+{posicaoy}"
