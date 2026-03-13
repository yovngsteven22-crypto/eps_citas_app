# 🩺 EPS Citas – Sistema de Gestión de Citas Médicas
### SENA · Análisis y Desarrollo de Software (ADSO)
### Tecnologías: Python · Flask · MySQL Workbench · Bootstrap 5

---

## ⚙️ Instalación paso a paso

### 1. Requisitos previos
- Python 3.10 o superior
- MySQL Workbench 8.x + MySQL Server
- (opcional) Visual Studio Code

### 2. Instalar dependencias Python
```bash
pip install -r requirements.txt
```

### 3. Crear la base de datos en MySQL Workbench
1. Abre MySQL Workbench y conéctate a localhost.
2. Ve a **File → Open SQL Script** y selecciona `eps_citas.sql`.
3. Haz clic en el rayo (⚡ Execute All) para ejecutar.
4. Verifica que se creó la base de datos `eps_citas` con las tablas `pacientes` y `citas`.

### 4. Configurar la conexión (si tienes contraseña en MySQL)
Edita `config.py`:
```python
MYSQL_PASSWORD = 'tu_contraseña_aqui'
```

### 5. Ejecutar la aplicación
```bash
python app.py
```

### 6. Abrir en el navegador
```
http://127.0.0.1:5000
```

---

## 📁 Estructura del Proyecto
```
eps_citas_app/
├── app.py               ← Rutas Flask (controlador)
├── config.py            ← Configuración MySQL
├── database.py          ← Conexión a la base de datos
├── requirements.txt     ← Dependencias
├── eps_citas.sql        ← Script SQL para MySQL Workbench
│
├── models/
│   ├── paciente.py      ← CRUD pacientes
│   └── cita.py          ← CRUD citas
│
└── templates/
    ├── base.html
    ├── index.html
    ├── pacientes.html
    ├── registro_paciente.html
    ├── citas.html
    ├── reservar_cita.html
    └── consulta_cita.html
```

## 🔧 Funcionalidades
- ✅ Registrar, editar y eliminar pacientes
- ✅ Reservar, editar y eliminar citas médicas
- ✅ Consultar citas por número de documento (INNER JOIN)
- ✅ Validaciones en formularios
- ✅ Mensajes de éxito/error con Flash
- ✅ Diseño responsivo con Bootstrap 5
