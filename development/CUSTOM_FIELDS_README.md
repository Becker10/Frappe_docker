# Custom Fields para Employee - Gestión de Herramientas

## Objetivo
Agregar información de activos (herramientas) de la empresa dentro del formulario de Empleado usando Custom Fields en Frappe/ERPNext.

## Campos Agregados

### 1. Herramienta Asignada
- **Tipo:** Link
- **Opciones:** Item
- **Descripción:** Permite seleccionar una herramienta de la lista de productos
- **Posición:** Después de "employee_name"
- **Obligatorio:** No

### 2. Fecha de Entrega  
- **Tipo:** Date
- **Descripción:** Registra la fecha en que se entregó la herramienta
- **Posición:** Después de "Herramienta Asignada"
- **Obligatorio:** No

### 3. Estado de la Herramienta
- **Tipo:** Select
- **Opciones:**
  - Nuevo
  - Usado
  - Dañado
- **Descripción:** Registra el estado actual de la herramienta asignada
- **Posición:** Después de "Fecha de Entrega"
- **Obligatorio:** Dinámico - Solo cuando se selecciona una herramienta
- **Condición:** `eval: doc.herramienta_asignada`

## Cómo Implementar

### Opción 1: Usando el Script de Python
```bash
cd /path/to/frappe-bench
bench execute development.custom_fields_employee.create_employee_custom_fields
```

### Opción 2: Manual en la UI de Frappe
1. Ir a **Customize Form** en el DocType Employee
2. Agregar los tres campos según las especificaciones arriba
3. Guardar y hacer Ctrl+Shift+R para refresh

### Opción 3: Importar desde JSON
Usar la herramienta de importación de Frappe con el archivo `employee_custom_fields.json`

## Archivos Incluidos
- `custom_fields_employee.py` - Script Python para crear los campos
- `employee_custom_fields.json` - Archivo JSON con la definición de campos
- `CUSTOM_FIELDS_README.md` - Este archivo de documentación

## Validación
Después de implementar, verifica que:
- ✓ Los tres campos aparecen en el formulario de Employee
- ✓ El campo "Estado de la Herramienta" solo es obligatorio cuando hay una herramienta asignada
- ✓ El campo "Herramienta Asignada" permite buscar en la lista de Items
- ✓ El campo "Fecha de Entrega" acepta fechas

## Notas
- La condición `eval: doc.herramienta_asignada` hace que el campo "Estado" sea obligatorio solo cuando existe una herramienta
- Los campos están posicionados después del nombre del empleado para mejor UX
- Los tipos de datos corresponden exactamente a lo especificado en los requisitos

---
**Fecha de creación:** 2026-02-26
**Versión:** 1.0
