class Calculadora:
    @staticmethod
    def somar(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtrair(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def dividir(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    @staticmethod
    def calcular(operacao: str, a: float, b: float) -> float:
        operacoes = {
            '+': Calculadora.somar,
            '-': Calculadora.subtrair,
            '*': Calculadora.multiplicar,
            '/': Calculadora.dividir,
        }
        if operacao not in operacoes:
            raise ValueError(f"Operação inválida: {operacao}")
        return operacoes[operacao](a, b)


def main():
    calc = Calculadora()
    print("=== CALCULADORA PROFISSIONAL ===")
    print("Operações disponíveis: +, -, *, /")
    try:
        a = float(input("DIGITE O PRIMEIRO NÚMERO: ").strip().replace(",", "."))
        operacao = input("DIGITE A OPERAÇÃO (+, -, *, /): ").strip()
        b = float(input("DIGITE O SEGUNDO NÚMERO: ").strip().replace(",", "."))
        resultado = calc.calcular(operacao, a, b)
        print(f"RESULTADO: {a} {operacao} {b} = {resultado}")
    except ValueError as e:
        print(f"ERRO: {e}")
    except Exception as e:
        print(f"ERRO INESPERADO: {e}")


if __name__ == "_main_":
    main()