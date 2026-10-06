"""
Genera un dataset SINTÉTICO que replica el modelo de datos del proyecto,
sin ningún dato real de clientes. Útil para ejecutar/demostrar el modelo
relacional y los KPIs sin comprometer privacidad.

Uso:
    python generate_sample_data.py
Genera CSVs en ./data/
"""
import csv, os, random
from datetime import date, timedelta

random.seed(42)
OUT = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT, exist_ok=True)

ESPECIES = ["Perro", "Gato"]
RAZAS = {"Perro": ["Quiltro", "Labrador", "Poodle", "Bulldog", "Pastor"],
         "Gato": ["Común europeo", "Siamés", "Persa", "Angora"]}
SEXOS = ["M", "H"]
COMUNAS = ["Peñalolén", "La Reina", "Ñuñoa", "Macul", "La Florida"]
VACUNAS = [("Óctuple", 365, 12000, 25000), ("Antirrábica", 365, 8000, 18000),
           ("Triple felina", 365, 10000, 22000), ("Bordetella", 180, 9000, 20000),
           ("Leucemia felina", 365, 15000, 30000)]
MOTIVOS = ["Control preventivo", "Vacunación", "Consulta", "Cirugía", "Urgencia"]

def rand_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

N_CLIENTES, N_MASCOTAS, N_VISITAS, N_VACUNAS, N_VETS = 300, 420, 500, 200, 6

# CLIENTE (sintético, sin PII real)
clientes = []
for i in range(1, N_CLIENTES + 1):
    rut = f"{random.randint(5,25)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(0,9)}"
    clientes.append({"rut_cliente": rut, "nombre": f"Cliente{i:04d}",
                     "direccion": f"Calle Ejemplo {random.randint(1,9999)}, {random.choice(COMUNAS)}",
                     "telefono": f"+569{random.randint(10000000,99999999)}",
                     "email": f"cliente{i:04d}@example.com", "activo": random.random() > 0.3})

# VETERINARIO
vets = [{"rut_veterinario": f"{random.randint(10,20)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(0,9)}",
         "nombre": f"Vet{i}", "apellido": f"Apellido{i}"} for i in range(1, N_VETS + 1)]

# MASCOTA
mascotas = []
for i in range(1, N_MASCOTAS + 1):
    esp = random.choice(ESPECIES)
    mascotas.append({"id_mascota": i, "nombre": f"Mascota{i:04d}", "especie": esp,
                     "raza": random.choice(RAZAS[esp]),
                     "fecha_nacimiento": rand_date(date(2012,1,1), date(2024,1,1)).isoformat(),
                     "sexo": random.choice(SEXOS),
                     "rut_cliente": random.choice(clientes)["rut_cliente"]})

# TIPO_VACUNA
tipos = [{"id_tipo_vacuna": i+1, "nombre_vacuna": v[0], "descripcion": f"Vacuna {v[0]}",
          "frecuencia_dias": v[1], "costo_vacuna": v[2], "precio_venta": v[3]}
         for i, v in enumerate(VACUNAS)]

# VISITA
visitas = []
for i in range(1, N_VISITAS + 1):
    costo = random.choice([15000, 20000, 25000, 40000, 60000])
    visitas.append({"id_visita": i, "fecha_visita": rand_date(date(2025,3,1), date(2026,3,1)).isoformat(),
                    "motivo": random.choice(MOTIVOS), "diagnostico": "N/A",
                    "costo": costo, "cobrado": costo if random.random() > 0.15 else 0,
                    "id_mascota": random.randint(1, N_MASCOTAS),
                    "rut_veterinario": random.choice(vets)["rut_veterinario"]})

# VACUNACION
vacs = []
for i in range(1, N_VACUNAS + 1):
    f = rand_date(date(2025,3,1), date(2026,3,1))
    t = random.choice(tipos)
    vacs.append({"id_vacunacion": i, "fecha_vacuna": f.isoformat(),
                 "proxima_fecha": (f + timedelta(days=t["frecuencia_dias"])).isoformat(),
                 "observaciones": "", "id_mascota": random.randint(1, N_MASCOTAS),
                 "id_tipo_vacuna": t["id_tipo_vacuna"],
                 "rut_veterinario": random.choice(vets)["rut_veterinario"]})

def dump(name, rows):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"  {name}: {len(rows)} filas")

print("Generando dataset sintético en ./data/ ...")
dump("cliente.csv", clientes); dump("veterinario.csv", vets); dump("mascota.csv", mascotas)
dump("tipo_vacuna.csv", tipos); dump("visita.csv", visitas); dump("vacunacion.csv", vacs)
print("Listo. Datos 100% sintéticos, sin información real de clientes.")
