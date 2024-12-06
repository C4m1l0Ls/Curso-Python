class CuentaBancaria:
    def __init__(self, titular, saldo, clave):
      self.titular = titular
      self._saldo = saldo
      self.__clave = clave
      

    def depositar(self, cantidadDeposito):
      self._saldo += cantidadDeposito
      return f"El saldo Actual {self._saldol}"
      

    def retirar(self, cantidadRetiro):
       if cantidadRetiro > self._saldo:
         return"Saldo Insuficiente"
       self._saldo -= cantidadRetiro
       return f"Retiroso exitoso. El saldo actual es {self._saldo}"
        

    def modificaClave(self, nuevaClave):
      self.__clave = nuevaClave
      return F"Clave modificada. la nueva clave es {self.__clave}"

cuentaBancaria1 = CuentaBancaria("lLuis Guillemor", 1000000, 1234)
print (cuentaBancaria1.titular)
print (cuentaBancaria1._saldo)

print(cuentaBancaria1.depositar(500000))
print(cuentaBancaria1.depositar(500000))
print(cuentaBancaria1.retirar(100000))
print(cuentaBancaria1.retirar(100000))
print(cuentaBancaria1.retirar(100000))
print(cuentaBancaria1.retirar(100000))

print(cuentaBancaria1.modificarClave(123456789))
