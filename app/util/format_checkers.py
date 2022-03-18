"""
Utilidades para comprobar formatos de entrada de datos

"""

import re


def valid_dni_format(dni):
    """
    Comprueba el formato del DNI.

    Sólo se comprueba el formato con una expresión regular.

    .. todo:: Falta comprobar la letra con el algoritmo para el `cálculo dígito dni <http://www.interior.gob.es/web/servicios-al-ciudadano/dni/calculo-del-digito-de-control-del-nif-nie>`_

    :param dni: El dni a comprobar

    :type dni: string
    """
    p = re.compile("^[0-9]{8}[a-zA-Z]$")
    return p.match(dni)
