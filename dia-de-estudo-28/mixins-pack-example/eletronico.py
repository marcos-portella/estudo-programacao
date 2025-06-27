from log import LogPrintMixin, LogFileMixin

class Eletronico:
    def __init__(self,nome):
        self._nome = nome
        self._ligado = True

    def ligar(self):
              if not self._ligado:
                    self._lilgado = True

    def desligar(self):
        if not self._ligado:
            self._ligado = False


class Smartphone(Eletronico, LogFileMixin): # Evite ao máximo herança múltipla
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)



    def desligar(self):
        super().desligar()

        if self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_success(msg)
