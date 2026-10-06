# Datos

⚠️ **Los datos reales de la clínica son confidenciales y no se incluyen aquí.**

Los archivos `*.csv` de esta carpeta son **100% sintéticos**, generados por
[`../generate_sample_data.py`](../generate_sample_data.py) para poder reproducir
el modelo relacional sin comprometer la privacidad de ningún cliente.

## Diccionario de datos (esquema)

### `cliente.csv`
| Campo | Tipo | Descripción |
|---|---|---|
| rut_cliente | string (PK) | Identificador del cliente (sintético) |
| nombre | string | Nombre (sintético) |
| direccion | string | Dirección (sintética) |
| telefono | string | Teléfono (sintético) |
| email | string | Correo (sintético) |
| activo | bool | Si registra actividad reciente |

### `mascota.csv`
| Campo | Tipo | Descripción |
|---|---|---|
| id_mascota | int (PK) | Identificador de la mascota |
| nombre | string | Nombre de la mascota |
| especie | string | Perro / Gato |
| raza | string | Raza |
| fecha_nacimiento | date | Fecha de nacimiento |
| sexo | string | M / H |
| rut_cliente | string (FK) | Dueño |

### `veterinario.csv`
| Campo | Tipo | Descripción |
|---|---|---|
| rut_veterinario | string (PK) | Identificador del veterinario |
| nombre / apellido | string | Nombre |

### `tipo_vacuna.csv`
| Campo | Tipo | Descripción |
|---|---|---|
| id_tipo_vacuna | int (PK) | Identificador |
| nombre_vacuna | string | Nombre comercial |
| descripcion | string | Descripción |
| frecuencia_dias | int | Periodicidad recomendada |
| costo_vacuna / precio_venta | int | Costo y precio |

### `visita.csv`
| Campo | Tipo | Descripción |
|---|---|---|
| id_visita | int (PK) | Identificador |
| fecha_visita | date | Fecha |
| motivo | string | Motivo de la visita |
| diagnostico | string | Diagnóstico |
| costo / cobrado | int | Costo del servicio y monto cobrado |
| id_mascota | int (FK) | Mascota atendida |
| rut_veterinario | string (FK) | Veterinario |

### `vacunacion.csv`
| Campo | Tipo | Descripción |
|---|---|---|
| id_vacunacion | int (PK) | Identificador |
| fecha_vacuna | date | Fecha de aplicación |
| proxima_fecha | date | Próxima dosis (clave para el KPI de vencimiento) |
| observaciones | string | Notas |
| id_mascota | int (FK) | Mascota |
| id_tipo_vacuna | int (FK) | Tipo de vacuna |
| rut_veterinario | string (FK) | Veterinario |
