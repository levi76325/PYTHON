def numero_reverso (numero):
   reverso = 0

   while numero > 0:
      ultimo_valor = numero % 10
      reverso = (reverso * 10) + ultimo_valor
      numero = numero // 10
      return reverso


numero = int(input('Informe o numero: '))
resultado = numero_reverso(numero)
print(f'O numero Informado { numero } e o reverso dele é: { resultado }')

