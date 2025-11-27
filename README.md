```
Modelos
  - cuidador
  - animal
  - instalacion

cuidador:
  nombre_cuidador, char, required
  animal_ids, relación one2many, es decir, un cuidador puede llegar a cuidar varios animales
  instalacion_id, relacion many2one, es decir, varios cuidadores pueden pertenecer a una instalación
  
animal
  nombre_animal, char, required
  especie, char, required
  edad, float, required
  estado, text
  cuidador_id, relacion many2one, es decir, varios animales pueden ser cuidados por un cuidador
  instalacion_id, relacion many2one, es decir, varios animales pueden pertenecer a una instalación
  
instalacion
  nombre_instalacion, char, required
  capacidad, float
  tipo, una selección con las siguientes opciones:
    - general, default
    - roedores
    - aves
    - exoticos
```
