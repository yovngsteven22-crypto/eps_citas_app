from database import get_connection

def crear_cita(documento, medico, tipo_cita, fecha, hora, direccion_eps):
    conn = get_connection()
    cur  = conn.cursor()
    sql  = """
        INSERT INTO citas (documento, medico, tipo_cita, fecha, hora, direccion_eps)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (documento, medico, tipo_cita, fecha, hora, direccion_eps))
    conn.commit()
    cur.close()
    conn.close()

def consultar_cita(documento):
    conn = get_connection()
    cur  = conn.cursor(dictionary=True)
    sql  = """
        SELECT
            p.nombre, p.apellido, p.eps,
            c.id AS cita_id,
            c.medico, c.tipo_cita, c.fecha, c.hora, c.direccion_eps
        FROM pacientes AS p
        INNER JOIN citas AS c ON p.documento = c.documento
        WHERE p.documento = %s
        ORDER BY c.fecha DESC, c.hora DESC
    """
    cur.execute(sql, (documento,))
    citas = cur.fetchall()
    cur.close()
    conn.close()
    return citas

def obtener_cita_por_id(cita_id):
    conn = get_connection()
    cur  = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM citas WHERE id = %s", (cita_id,))
    cita = cur.fetchone()
    cur.close()
    conn.close()
    return cita

def actualizar_cita(cita_id, medico, tipo_cita, fecha, hora, direccion_eps):
    conn = get_connection()
    cur  = conn.cursor()
    sql  = """
        UPDATE citas
        SET medico=%s, tipo_cita=%s, fecha=%s, hora=%s, direccion_eps=%s
        WHERE id=%s
    """
    cur.execute(sql, (medico, tipo_cita, fecha, hora, direccion_eps, cita_id))
    conn.commit()
    cur.close()
    conn.close()

def eliminar_cita(cita_id):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("DELETE FROM citas WHERE id = %s", (cita_id,))
    conn.commit()
    cur.close()
    conn.close()

def listar_todas():
    conn = get_connection()
    cur  = conn.cursor(dictionary=True)
    sql  = """
        SELECT
            p.nombre, p.apellido, p.documento,
            c.id AS cita_id,
            c.medico, c.tipo_cita, c.fecha, c.hora, c.direccion_eps
        FROM pacientes AS p
        INNER JOIN citas AS c ON p.documento = c.documento
        ORDER BY c.fecha DESC, c.hora DESC
    """
    cur.execute(sql)
    citas = cur.fetchall()
    cur.close()
    conn.close()
    return citas
