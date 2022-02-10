"""def _get_client_name ():
	client_name = None

	while not client_name:
		client_name = str.lower(input('What is the client name ? '))

		if client_name == 'exit':
			client_name = None
			break

	return client_name

_get_client_name()"""

import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)


def consulta_clientes(tupla):
	print("\n{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('IDENTIFICACIÓN', 'NOMBRE',
																						   'APELLIDO', 'PAIS', 'CIUDAD',
																						   'CELULAR', 'CORREO',
																						   'FECHA DE PAGO', 'NUMERO TC',
																						   'ESTADO PAGO'))
	for row in tupla:
		id = row[0]
		nombre = row[1]
		apellido = row[2]
		pais = row[3]
		ciudad = row[4]
		celular = row[5]
		correo = row[6]
		fecha_pago = row[7]
		numero_tc = row[8]
		estado_pago = row[9]

		print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(id, nombre,
																							 apellido,
																							 pais, ciudad,
																							 celular,
																							 correo,
																							 fecha_pago,
																							 numero_tc,
																							 estado_pago))

tupla = [('1', 'Juan', 'Perez', 'Colombia', 'Bogota', '312312312', 'o@gmail.com', '12/12/12', '123456789', 'Pagado'),
		 ('2', 'Juan', 'Perez', 'Colombia', 'Bogota', '312312312', 'o@gmail.com', '12/12/12', '123456789', 'Pagado'),
		 ('3', 'Juan', 'Perez', 'Colombia', 'Bogota', '312312312', 'o@gmail.com', '12/12/12', '123456789', 'Pagado'),
		 ('4', 'Juan', 'Perez', 'Colombia', 'Bogota', '312312312', 'o@gmail.com' , '12/12/12', '123456789', 'Pagado')
		 ]

consulta_clientes(tupla)