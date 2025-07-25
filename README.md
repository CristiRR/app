#### 🪄Este proyecto es un sistema de gestión de empleados.
## ✨Uso
## Instrucciones de Uso

### **1. Ejecutar la aplicación**
Desde la terminal, en la carpeta raíz del proyecto:
```sh
python app/main.py
```

---

### **2. Menú Principal**

Al iniciar, verás el siguiente menú:

```
--- Menú de Gestión de Empleados ---
1. Crear empleado
2. Ver empleados por rol
3. Solicitar vacaciones
4. Pagar empleados
5. Ver historial de transacciones
0. Salir
```

---

### **3. Crear empleado**

- Selecciona `1`.
- Ingresa el nombre del empleado.
- Ingresa el rol:  
  - `intern`
  - `manager`
  - `vice_president`
  - `freelancer`
- Según el rol:
  - **Freelancer:** Se te pedirá información de proyectos.
  - **Intern:** Se te pedirá el tipo de pago (`salaried` o `hourly`), y luego el salario mensual o tarifa y horas.
  - **Otros roles:** Se te pedirá el tipo de pago (`salaried` o `hourly`), y luego el salario o tarifa y horas.

---
### **4. Ver empleados por rol**

- Selecciona `2`.
- Elige el submenú para ver managers, interns, vice presidents, freelancers o todos los empleados.

---

### **5. Solicitar vacaciones**

- Selecciona `3`.
- Elige el empleado (por índice).
- Ingresa los días de vacaciones y si deseas payout.
- Las restricciones de vacaciones se aplican según la política del empleado.

---

### **6. Pagar empleados**

- Selecciona `4`.
- El sistema calculará y mostrará el pago de cada empleado según su política.

---
### **7. Ver historial de transacciones**

- Selecciona `5`.
- Elige el empleado (por índice) para ver su historial de pagos y vacaciones.

---

### **8. Salir**

- Selecciona `0` para salir del sistema.

---

## Notas

- Los interns nunca reciben bonus, aunque sean salaried u hourly.
- Las políticas de pago y vacaciones pueden modificarse fácilmente agregando nuevas clases.
- El sistema es extensible y cumple con los principios SOLID.

---
## Estructura de Carpetas

- `models/` — Clases de empleados.
- `policies/payment/` — Políticas de pago (Strategy).
- `policies/vacation/` — Políticas de vacaciones (Strategy).
- `services/employee_factory.py` — Factory Method para empleados.
- `services/employee_manager.py` — Lógica de menú y operaciones.
- `utils/config_loader.py` — Carga de configuraciones de políticas.
- `app/main.py` — Punto de entrada.

---

## ✨Utiliza varios patrones para lograr flexibilidad, escalabilidad y fácil mantenimiento.  
A continuación se explican los principales patrones aplicados:

1. **Strategy** 🌟

El patrón **Strategy** permite definir una familia de algoritmos, encapsular cada uno y hacerlos intercambiables.  
En este sistema:

- **Políticas de pago** (`PaymentPolicy`) y **políticas de vacaciones** (`VacationPolicy`) son estrategias.
- Cada empleado tiene una política de pago y una de vacaciones que pueden variar en tiempo de ejecución.
- Ejemplo: Un intern y un manager pueden tener diferentes formas de calcular el pago o de solicitar vacaciones, pero ambos usan la misma interfaz.

**Ventaja:**  
Permite cambiar el comportamiento de pago o vacaciones de un empleado sin modificar su clase.



### 2. **Bridge** 🪴

El patrón **Bridge** desacopla una abstracción de su implementación, permitiendo que ambas evolucionen independientemente.

- **Abstracción:** La jerarquía de empleados (`Employee` y subclases).
- **Implementación:** Las políticas de pago y vacaciones.
- Un empleado no implementa directamente cómo se calcula el pago o las vacaciones, sino que delega ese comportamiento a sus políticas.
- Esto permite combinar libremente cualquier tipo de empleado con cualquier política.

**Ventaja:**  
Permite agregar nuevos tipos de empleados o nuevas políticas sin modificar las clases existentes.

---

### 3. **Factory Method** 🔧

El patrón **Factory Method** centraliza la creación de objetos complejos. 

- La clase `EmployeeFactory` es responsable de crear instancias de empleados según el tipo y rol.
- Encapsula la lógica de construcción y selección de políticas, evitando código repetido y facilitando la extensión.

**Ventaja:**  
Permite crear empleados de diferentes tipos de manera uniforme y centralizada, facilitando la extensión y el mantenimiento.

