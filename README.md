# Python-OOP-Project
A comprehensive Object-Oriented Programming project implementing an employee management system. Built as part of ITI's Programming Fundamentals course, this system simulates daily work routines including sleep tracking, meal planning, car fuel management, and employee attendance monitoring.

## 📋 Table of Contents
- [Overview](#overview)
- [Class Documentation](#class-documentation)
- [OOP Concepts Demonstrated](#oop-concepts-demonstrated)

---

## Overview

This project implements a complete employee management system that tracks:
-  **Person activities**: sleep patterns, meal tracking, shopping
-  **Car management**: fuel monitoring, velocity control, distance tracking
-  **Employee operations**: work hours, commute simulation, email communication
-  **Office management**: hiring, firing, salary adjustments, attendance tracking
---

## Class Documentation

### 1. `person` Class

Base class representing a person with daily activities.

#### Attributes
| Attribute | Type | Description | Default |
|-----------|------|-------------|---------|
| `name` | str | Person's name | Required |
| `money` | float | Current money amount | Required |
| `mood` | str | Current mood state | None |
| `healthrate` | str | Health percentage | None |

#### Methods

**`sleep(hours)`**

**`eat(meals)`**

**`buy(items)`**
- Each item costs **10** units

---

### 2. `Car` Class
Represents a vehicle with fuel and velocity management.

#### Attributes
| Attribute | Type | Range | Description |
|-----------|------|-------|-------------|
| `name` | str | - | Car's name/model |
| `fuel_rate` | float | 0-100 | Fuel percentage (validated) |
| `velocity` | float | 0-200 | Speed in km/h (validated) |

#### Methods

**`run(velocity, distance)`**
- Sets velocity
- Consumes 10% fuel per 10km
- Automatically stops when fuel depletes

**`stop(remaining_distance)`**

---
### 3. `Employee` Class

Inherits from `person` and adds work-related functionality.

#### Additional Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | int | Employee ID |
| `car` | Car | Employee's vehicle |
| `email` | str | Email address |
| `salary` | float | Salary amount |
| `distance_to_work` | float | Commute distance (km) |

#### Methods

**`work(hours)`**
- Validates hours (0-24)
**`drive(distance, velocity)`**
- Delegates to car's `run()` method
  
**`refuel(gas_amount=100)`**

**`send_mail(to, subject, body)`**

---

### 4. `office` Class

Manages employees and office operations.

#### Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | str | Office name |
| `employees` | list | List of Employee objects |

#### Methods

**`hire(employee)`**

**`fire(emp_id)`**

**`get_employee(emp_id)`**

**`get_all_employees()`**

**`reward_employee(emp_id, amount)`**

**`deduct_salary(emp_id, amount)`**

**`check_lateness(emp_id, move_hour)`**
- **On time** → Reward 10
- **Late** → Deduct 10

---

## OOP Concepts Demonstrated

### 1. **Inheritance**
Employee inherits all methods from person (sleep, eat, buy).
### 2. **Encapsulation**
Uses private attributes with property decorators for validation.
### 3. **Property Decorators**
Automatic validation ensures fuel_rate stays within 0-100%.
###4 . **Aggregation**
Office manages a collection of Employee objects.

---
##  Authors

- Mariam Ankeeb - [mariam-ankeeb](https://github.com/mariam-ankeeb))

---
