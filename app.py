from flask import Flask, render_template, request, redirect, url_for, flash
from models.paciente import (crear_paciente, obtener_paciente, listar_pacientes,
                              actualizar_paciente, eliminar_paciente)
from models.cita     import (crear_cita, consultar_cita, obtener_cita_por_id,
                              actualizar_cita, eliminar_cita, listar_todas)

app = Flask(__name__)
app.secret_key = 'eps_citas_secret_2024'
import traceback

@app.route('/debug')
def debug():
    from config import Config
    return {
        'host': Config.MYSQL_HOST,
        'user': Config.MYSQL_USER,
        'db': Config.MYSQL_DB,
        'port': Config.MYSQL_PORT
    }
# ─── INICIO ────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

# ─── PACIENTES ─────────────────────────────────────────────────────────────────
@app.route('/pacientes')
def pacientes():
    lista = listar_pacientes()
    return render_template('pacientes.html', pacientes=lista)

@app.route('/registrar', methods=['GET', 'POST'])
def registrar_paciente():
    if request.method == 'POST':
        doc      = request.form['documento'].strip()
        nombre   = request.form['nombre'].strip()
        apellido = request.form['apellido'].strip()
        tel      = request.form['telefono'].strip()
        correo   = request.form['correo'].strip()
        eps      = request.form['eps'].strip()

        if not doc or not nombre or not apellido:
            flash('Documento, nombre y apellido son obligatorios.', 'error')
            return render_template('registro_paciente.html')

        if obtener_paciente(doc):
            flash(f'Ya existe un paciente con el documento {doc}.', 'error')
            return render_template('registro_paciente.html')

        crear_paciente(doc, nombre, apellido, tel, correo, eps)
        flash(f'Paciente {nombre} {apellido} registrado exitosamente.', 'success')
        return redirect(url_for('pacientes'))

    return render_template('registro_paciente.html')

@app.route('/editar_paciente/<documento>', methods=['GET', 'POST'])
def editar_paciente(documento):
    paciente = obtener_paciente(documento)
    if not paciente:
        flash('Paciente no encontrado.', 'error')
        return redirect(url_for('pacientes'))

    if request.method == 'POST':
        actualizar_paciente(
            documento,
            request.form['nombre'].strip(),
            request.form['apellido'].strip(),
            request.form['telefono'].strip(),
            request.form['correo'].strip(),
            request.form['eps'].strip()
        )
        flash('Paciente actualizado correctamente.', 'success')
        return redirect(url_for('pacientes'))

    return render_template('registro_paciente.html', paciente=paciente, editar=True)

@app.route('/eliminar_paciente/<documento>')
def eliminar_paciente_ruta(documento):
    eliminar_paciente(documento)
    flash('Paciente eliminado.', 'info')
    return redirect(url_for('pacientes'))

# ─── CITAS ─────────────────────────────────────────────────────────────────────
@app.route('/citas')
def citas():
    lista = listar_todas()
    return render_template('citas.html', citas=lista)

@app.route('/reservar', methods=['GET', 'POST'])
def reservar_cita():
    pacientes_lista = listar_pacientes()
    if request.method == 'POST':
        doc          = request.form['documento'].strip()
        medico       = request.form['medico'].strip()
        tipo_cita    = request.form['tipo_cita']
        fecha        = request.form['fecha']
        hora         = request.form['hora']
        direccion    = request.form['direccion_eps'].strip()

        if not obtener_paciente(doc):
            flash('No existe un paciente con ese documento. Regístralo primero.', 'error')
            return render_template('reservar_cita.html', pacientes=pacientes_lista)

        crear_cita(doc, medico, tipo_cita, fecha, hora, direccion)
        flash('Cita reservada exitosamente.', 'success')
        return redirect(url_for('citas'))

    return render_template('reservar_cita.html', pacientes=pacientes_lista)

@app.route('/consultar', methods=['GET', 'POST'])
def consultar_cita_ruta():
    citas_resultado = []
    documento = ''
    if request.method == 'POST':
        documento = request.form['documento'].strip()
        citas_resultado = consultar_cita(documento)
        if not citas_resultado:
            flash('No se encontraron citas para ese documento.', 'info')
    return render_template('consulta_cita.html', citas=citas_resultado, documento=documento)

@app.route('/editar_cita/<int:cita_id>', methods=['GET', 'POST'])
def editar_cita(cita_id):
    cita = obtener_cita_por_id(cita_id)
    if not cita:
        flash('Cita no encontrada.', 'error')
        return redirect(url_for('citas'))

    if request.method == 'POST':
        actualizar_cita(
            cita_id,
            request.form['medico'].strip(),
            request.form['tipo_cita'],
            request.form['fecha'],
            request.form['hora'],
            request.form['direccion_eps'].strip()
        )
        flash('Cita actualizada correctamente.', 'success')
        return redirect(url_for('citas'))

    return render_template('reservar_cita.html',
                           cita=cita,
                           pacientes=listar_pacientes(),
                           editar=True)

@app.route('/eliminar_cita/<int:cita_id>')
def eliminar_cita_ruta(cita_id):
    eliminar_cita(cita_id)
    flash('Cita eliminada.', 'info')
    return redirect(url_for('citas'))
import logging
logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    app.run(debug=True)
