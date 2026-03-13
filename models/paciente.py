from database import get_connection

def crear_paciente(documento, nombre, apellido, telefono, correo, eps):
    conn = get_connection()
    cur  = conn.cursor()
    sql  = """
        INSERT INTO pacientes (documento, nombre, apellido, telefono, correo, eps)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (documento, nombre, apellido, telefono, correo, eps))
    conn.commit()
    cur.close()
    conn.close()

def obtener_paciente(documento):
    conn = get_connection()
    cur  = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM pacientes WHERE documento = %s", (documento,))
    paciente = cur.fetchone()
    cur.close()
    conn.close()
    return paciente

def listar_pacientes():
    conn = get_connection()
    cur  = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM pacientes ORDER BY apellido, nombre")
    pacientes = cur.fetchall()
    cur.close()
    conn.close()
    return pacientes

def actualizar_paciente(documento, nombre, apellido, telefono, correo, eps):
    conn = get_connection()
    cur  = conn.cursor()
    sql  = """
        UPDATE pacientes
        SET nombre=%s, apellido=%s, telefono=%s, correo=%s, eps=%s
        WHERE documento=%s
    """
    cur.execute(sql, (nombre, apellido, telefono, correo, eps, documento))
    conn.commit()
    cur.close()
    conn.close()

def eliminar_paciente(documento):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("DELETE FROM pacientes WHERE documento = %s", (documento,))
    conn.commit()
    cur.close()
    conn.close()
