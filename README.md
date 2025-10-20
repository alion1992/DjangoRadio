Tabla de endpoints

| Método | Ruta                                 | Descripción                 | Body | Auth |
| -----: | ------------------------------------ | --------------------------- | ---- | ---- |
|    GET | `/obtenerCancion/<id>/`              | Devuelve una canción por id | —    | —    |
|   POST | `/addCancion/`                       | Crea una nueva canción      | JSON | —    |
|    GET | `/obtenerCanciones/`                 | Lista todas las canciones   | —    | —    |


Ejemplo de Json

'''json
{
  "nombre": "Cancion de Francisco con autor",
  "duracion": 354,
  "ano_lanzamiento": 1992,
  "autor_id": 2
}
{"nombre": "Imagine", "duracion": 183}
