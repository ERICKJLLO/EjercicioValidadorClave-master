from abc import ABC

class ReglaValidacion(ABC):
    def __init__(self, longitud_minima=8):
        self.longitud_minima = longitud_minima

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    def _validar_longitud(self, clave):
        return len(clave) >= self.longitud_minima