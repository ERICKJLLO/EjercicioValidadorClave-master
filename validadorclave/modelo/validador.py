from abc import ABC, abstractmethod
from errores import ValidadorError, NoCumpleLongitudMinimaError, NoTieneCaracterEspecialError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTienePalabraSecretaError

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
    
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_minima=8)

    def contiene_caracter_especial(self, clave):
        return bool(re.search(r'[!@#$%^&*()_+=\-{}\[\]:;"\'<>,.?/]', clave))

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError

        return True
