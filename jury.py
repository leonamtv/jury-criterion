def jury ( p ) :
    """
    Função para verificar se um sistema é ou não
    estável, utilizando o critério de Jury.
    ---
    Function to verify the stability of a system
    according to Jury criterion.
    """

    debug = False

    def eval ( p, v ) :
        """
        Função para calcular um valor 'v' aplicado
        em um polinômio 'p'
        ----
        Function to evaluate a value 'v' in a poly-
        nom 'p'
        """
        res = 0
        for i in range( len(p) ): 
            res += p[::-1][i] * ( v ** ( i ))
        return res
    
    def printa ( a ) :
        """
        Função para imprimir uma lista de coefici-
        entes.
        ----
        Function to print a line of coefficients in
        forward and reverse order.
        """
        if len(a) > 0 :
            for i in a :
                print('%.4f\t\t' % round(i, 4), end='')
            print()
            for i in a[::-1] :
                print('%.4f\t\t' % round(i, 4), end='')
            print()

    # Calcula grau do polinômio
    n = len(p) - 1

    # Verifica primeira condição
    if eval ( p, 1 ) <= 0 :
        print('1. Sistema instável.')
        return

    # Verifica segunda condição
    if (((-1) ** n ) * eval ( p, -1 )) <= 0 :
        print('2. Sistema instável.')
        return

    # Inverte a ordem dos coeficientes do polinômio
    # para que podemos prosseguir com mais facilidade
    p = p[::-1]

    # Verifica terceira condição
    if abs(p[0]) >= abs(p[-1]) :
        print('3. Sistema instável.')
        return

    # Define a linha atual como os coeficientes do 
    # polinômio
    l = p

    # Caso estejamos debugando o código, imprime a 
    # linha
    if debug :
        printa(l)

    # Itera até que tenhamos apenas 1 coeficiente
    # restante na linha
    for i in range ( n + 1 ) :
        # Define nova linha
        nl = []
        for j in range ( len(l) - 1 ) :
            
            x0   = l[0]
            xk   = l[j]
            xn   = l[-1]
            xn_k = l[-(j + 1)]

            # Calcula o determinante e adiciona na nova linha
            nl.append( x0 * xk - xn * xn_k )
        
        # Define a linha atual como a nova linha
        l = nl

        # Se o tamanho da linha for maior que 1
        # faz o teste de estabilidade:
        # |b0| > |bn-1|
        # |c0| > |cn-2|
        # |d0| > |dn-3|
        # ...
        if len(l) > 1 :
            if abs(l[0]) <= abs(l[-1]) :
                print(f'{4 + i}. Sistema instável.')
                return

        # Caso estejamos debugando o código, imprime a 
        # linha
        if debug :
            printa(l)

    # Se chegar até aqui é porque o sistema é estável
    print('Sistema estável')
