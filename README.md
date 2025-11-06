### Tabla de endpoints

| Método | Ruta                                 | Descripción                 | Body | Auth | Autor | 
| -----: | ------------------------------------ | --------------------------- | ---- | ---- | ------|
|    GET | `/obtenerCancion/<id>/`              | Devuelve una canción por id | —    | —    | Juan  |
|   POST | `/addCancion/`                       | Crea una nueva canción      | JSON | —    |       |
|    GET | `/obtenerCanciones/`                 | Lista todas las canciones   | —    | —    |       |


<h3>Ejemplo de Json</h3>

```json
{
  "nombre": "Cancion de Francisco con autor",
  "duracion": 354,
  "ano_lanzamiento": 1992,
  "autor_id": 2
}
```
<h3>Ejemplo de crear carta</h3>

```bash
api/addCard/
```
El json de ejemplo para añadir una carta es:

```json
"carta" {
  "nombre" : "Fran"
}


<img width="380" height="192" alt="image" src="https://github.com/user-attachments/assets/426643ba-8fce-4002-8d91-3d2c6b67ac2a" />

