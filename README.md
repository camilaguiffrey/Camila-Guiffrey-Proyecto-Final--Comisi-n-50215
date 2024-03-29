Alumna: Guiffrey, Camila.

Título: “El sitio del mar”

Versión: 1.0

Descripción

El sitio del Mar es un proyecto destinado a la reserva de alojamiento en las ciudades de la costa Argentina. En el sitio podemos visualizar los alojamientos disponibles, el precio, donde se ubican, entre otros campos; y tiene la posibilidad de ver y escribir reseñas acerca de los mismos.

Cómo utilizarlo

Una vez instalado, podemos abrir el sitio y encontrarnos con una página principal donde se visualiza un panel con las diferentes ciudades de las cuales podemos hallar alojamientos (aún no es funcional), y una cabecera en la cual se hallan botones con diferentes funcionalidades:

1.  Inicio: este botón nos dirige a la página principal del proyecto.
2.  Alojamientos: este botón nos permite ver todos los alojamientos disponibles.
3. Iniciar sesión: permite loguearse a aquellos usuarios que ya están registrados en la aplicación.
4. Registrarse: en el caso de no estar registrado, al presionar este botón se puede guardar los datos de un usuario nuevo.
5. Botón de búsqueda: aquí podemos escribir la ciudad que nos interesa y la página te filtra los resultados en base a la cadena ingresada.
6. Mi perfil: para aquellos usuarios que hayan ingresado a su cuenta, pueden acceder a una vista de su perfil, con sus respectivos datos. 
7. Sobre Mi: breve descripción de la alumna.

Modelos

- Usuario: fue creado para permitir que cada usuario publique sus alojamientos o reseñas.
- Alojamiento: corresponden al producto principal del sitio.
- Reseña: están ligadas a los alojamientos ya que permiten conocer las opiniones de otros usuarios sobre un alojamiento en específico.
- Ciudad: este modelo fue creado para brindar una cierta cantidad de opciones de ciudades a los usuarios propietarios que quieran publicar sus alojamientos.

Apartado de alojamientos

En esta sección podemos ver todos los alojamientos. En el encabezado podemos hallar un botón para añadir un alojamiento al sitio, el cual funciona como formulario. Debajo podemos visualizar todos los alojamientos disponibles, y presionando el botón de “Más información” es posible acceder al detalle de cada objeto en específico. A su vez, encontramos un botón que te permite contactar al propietario a través de correo electrónico. Por último, cuenta con una sección de reseñas sobre el alojamiento, y un formulario que permite a un usuario registrado escribir una reseña. 

CRUD - 1 por cada modelo

En el caso de mi aplicación, no considero que sea muy coherente poder agregar usuarios, reseñas y ciudades a partir de un CRUD como el de alojamientos. Sin embargo, por una cuestión de que la consigna lo requería los realicé de igual modo. Los CRUD de los modelos Review, Usuario y Ciudad están disponibles en la página principal, en sus respectivos botones de “Ver  todos los usuarios” en caso del modelo Usuario, y así con los demás modelos. Solo son visibles para los usuarios que estén autenticados.
Para el modelo Alojamiento, el CRUD está disponible en el perfil del usuario, haciendo click en el botón “Mis alojamientos”, allí se pueden hallar las opciones de agregar un alojamiento, editarlo o eliminarlo.

Mi perfil

En esta página podemos observar los datos del usuario registrado, también se puede editar los datos del usuario y ver los alojamientos (CRUD alojamientos). Al presionar “Editar mi perfil” podemos acceder a un botón para modificar el avatar del usuario.


Admin

Nombre: Camila
Contraseña: Guiffrey

Link a un Drive con el video explicativo, las pruebas unitarias y un archivo README: https://drive.google.com/drive/folders/1jOO4Cu6FdwCqB2lrRXV6xXnDEJSWfdUq?usp=drive_link
