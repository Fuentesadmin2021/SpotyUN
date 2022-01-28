
# 1. python setup.py sdist 
# 2. pip3 install (nombre del paquete Ejp: paquetes_ad)
# 3. pip3 uninstall (nombre del paquete Ejp: paquetes_ad)

from setuptools import setup
setup(

    name = "paquetevalidaciond",
    version = "1.0",
    description = "Paquete para validación de información",
    author = "Admin SpotyUN",
    author_email = "sin email",
    url = "sin url",
    packages = ["paquetes_ad", "paquetes_ad"] 
)

