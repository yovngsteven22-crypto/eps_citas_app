-- ============================================================
--  Script SQL – Sistema de Gestión de Citas Médicas EPS
--  Ejecutar en MySQL Workbench: Abrir pestaña Query y correr
-- ============================================================

CREATE DATABASE IF NOT EXISTS eps_citas
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE eps_citas;

-- ── Tabla pacientes ──────────────────────────────────────────
CREATE TABLE IF NOT EXISTS pacientes (
    id        INT           AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(15)   NOT NULL UNIQUE,
    nombre    VARCHAR(80)   NOT NULL,
    apellido  VARCHAR(80)   NOT NULL,
    telefono  VARCHAR(20),
    correo    VARCHAR(100),
    eps       VARCHAR(100)
);

-- ── Tabla citas ──────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS citas (
    id            INT           AUTO_INCREMENT PRIMARY KEY,
    documento     VARCHAR(15)   NOT NULL,
    medico        VARCHAR(100)  NOT NULL,
    tipo_cita     VARCHAR(50)   NOT NULL,
    fecha         DATE          NOT NULL,
    hora          TIME          NOT NULL,
    direccion_eps VARCHAR(150),
    CONSTRAINT fk_paciente
        FOREIGN KEY (documento)
        REFERENCES pacientes(documento)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- ── Datos de prueba ──────────────────────────────────────────
INSERT INTO pacientes (documento, nombre, apellido, telefono, correo, eps) VALUES
('1023456789', 'Carlos',  'Ramírez',  '3001234567', 'carlos@email.com',  'Sura'),
('9876543210', 'Lucía',   'Herrera',  '3109876543', 'lucia@email.com',   'Nueva EPS'),
('4567891230', 'Andrés',  'Morales',  '3204567890', 'andres@email.com',  'Compensar');

INSERT INTO citas (documento, medico, tipo_cita, fecha, hora, direccion_eps) VALUES
('1023456789', 'Dr. Martínez',  'General',     '2024-12-20', '09:00:00', 'Calle 72 # 10-30, Bogotá'),
('9876543210', 'Dra. Gómez',    'Odontología', '2024-12-21', '14:30:00', 'Av. El Dorado # 85-42, Bogotá'),
('4567891230', 'Dr. Jiménez',   'Especialista','2024-12-22', '11:00:00', 'Carrera 15 # 93-47, Bogotá');

-- ── Consulta de verificación ─────────────────────────────────
SELECT
    p.nombre, p.apellido, p.eps,
    c.medico, c.tipo_cita, c.fecha, c.hora, c.direccion_eps
FROM pacientes AS p
INNER JOIN citas AS c ON p.documento = c.documento
ORDER BY c.fecha;
