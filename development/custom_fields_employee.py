"""
Script para agregar Custom Fields al DocType Employee
Campos solicitados:
1. Herramienta Asignada (Link a Item)
2. Fecha de Entrega (Date)
3. Estado de la Herramienta (Select: Nuevo, Usado, Dañado)
"""

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def create_employee_custom_fields():
    """Crea los custom fields para Employee"""
    
    custom_fields = {
        "Employee": [
            {
                "fieldname": "herramienta_asignada",
                "label": "Herramienta Asignada",
                "fieldtype": "Link",
                "options": "Item",
                "insert_after": "employee_name",
                "mandatory": 0,
            },
            {
                "fieldname": "fecha_entrega",
                "label": "Fecha de Entrega",
                "fieldtype": "Date",
                "insert_after": "herramienta_asignada",
                "mandatory": 0,
            },
            {
                "fieldname": "estado_herramienta",
                "label": "Estado de la Herramienta",
                "fieldtype": "Select",
                "options": "Nuevo\nUsado\nDañado",
                "insert_after": "fecha_entrega",
                "mandatory": 0,
                "mandatory_depends_on": "eval: doc.herramienta_asignada",
            },
        ]
    }
    
    create_custom_fields(custom_fields)
    frappe.db.commit()
    print("✓ Custom fields agregados exitosamente a Employee")

if __name__ == "__main__":
    create_employee_custom_fields()
