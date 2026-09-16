# ⚛️ Mini Hexagonal Physics API

A tiny project built to understand **Hexagonal Architecture** in a simple and practical way.

The application calculates kinetic energy:

$$
E_k = \frac{1}{2}mv^2
$$

and stores previous calculations using an in-memory repository.

The main goal of this repository is not the physics calculation itself, but to understand how **Domain, Application, Ports and Adapters** interact.

---

## 🎯 Project Goal

This project was intentionally kept small to isolate the architectural concepts.

The core idea is:

```text
External World
      ↓
Adapters
      ↓
Ports
      ↓
Application
      ↓
Domain
```

The most important rule is:

```text
Dependencies point toward the core.
```

The domain does not know anything about:

* FastAPI
* Docker
* PostgreSQL
* Cloud Run
* HTTP

It only contains the business rules.

---

## 🧠 Architecture

```text
HTTP Request
     ↓
FastAPI Adapter
     ↓
Application / Use Case
     ↓
Domain
     ↓
Repository Port
     ↓
InMemory Repository Adapter
```

Conceptually:

```text
┌─────────────────────────────────────┐
│           Infrastructure            │
│                                     │
│   FastAPI              Repository   │
│      ↓                     ↑        │
│      └──── Application ────┘        │
│                ↓                    │
│              Domain                 │
│                                     │
└─────────────────────────────────────┘
```

---

## 📁 Project Structure

```text
mini-hexagonal-physics/
│
├── app/
│   ├── domain/
│   │   └── energy.py
│   │
│   ├── application/
│   │   ├── ports.py
│   │   └── use_cases.py
│   │
│   ├── infrastructure/
│   │   ├── repository.py
│   │   └── api.py
│   │
│   └── main.py
│
├── tests/
│   └── test_use_case.py
│
├── pyproject.toml
├── uv.lock
└── Dockerfile
```

---

## 🧩 Components

### Domain

Contains the fundamental business rule:

```text
energy.py
```

Responsible for calculating:

$$
E_k = \frac{1}{2}mv^2
$$

The domain is independent from frameworks and infrastructure.

---

### Application

Contains the use cases.

Examples:

```text
CalculateKineticEnergy
ListEnergyCalculations
```

The application coordinates the domain and the external dependencies.

---

### Ports

Ports define what the application needs from the outside world.

Example:

```python
class EnergyRepository(Protocol):

    def save(self, calculation: EnergyCalculation) -> None:
        ...

    def list_all(self) -> list[EnergyCalculation]:
        ...
```

The application knows the abstraction:

```text
EnergyRepository
```

but it does not know if the implementation uses:

```text
Memory
PostgreSQL
SQLite
Firestore
Cloud SQL
```

---

### Adapters

Adapters provide concrete implementations of ports.

This project uses:

```text
InMemoryEnergyRepository
```

Internally, calculations are stored in:

```python
list[EnergyCalculation]
```

A future implementation could replace it with:

```text
PostgresEnergyRepository
```

without modifying the domain or the use cases.

---

## 🚀 Run Locally

Install dependencies:

```bash
uv sync
```

Start the API:

```bash
uv run uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 🔬 Example

Request:

```http
POST /energy
```

```json
{
  "mass_kg": 10,
  "speed_m_s": 3
}
```

Response:

```json
{
  "mass_kg": 10,
  "speed_m_s": 3,
  "energy_j": 45.0
}
```

Because:

$$
E_k =
\frac{1}{2}(10)(3^2)
=
45\ J
$$

---

## 📜 Calculation History

```http
GET /history
```

Example:

```json
[
  {
    "mass_kg": 10,
    "speed_m_s": 3,
    "energy_j": 45.0
  }
]
```

---

## 🧪 Tests

Run:

```bash
uv run pytest
```

The use case can be tested without starting FastAPI.

This is one of the advantages of separating the application core from external infrastructure.

---

## 🐳 Docker

Build the image:

```bash
docker build -t mini-hexagonal-physics .
```

Run the container:

```bash
docker run \
  -p 8080:8080 \
  mini-hexagonal-physics
```

Open:

```text
http://localhost:8080/docs
```

Inside the container, the project structure is approximately:

```text
/app
├── pyproject.toml
├── uv.lock
└── app
    ├── domain
    ├── application
    ├── infrastructure
    └── main.py
```

---

## ☁️ Cloud-ready

Because the application is containerized, the same Docker image can later be built using:

```text
Cloud Build
```

stored in:

```text
Artifact Registry
```

and deployed to:

```text
Cloud Run
```

Conceptually:

```text
GitHub
   ↓
Cloud Build
   ↓
Docker Image
   ↓
Artifact Registry
   ↓
Cloud Run
   ↓
Container
   ↓
FastAPI
   ↓
Hexagonal Application
```

---

## 🧠 Mental Model

A useful way to remember Hexagonal Architecture is to ask four questions:

| Question                                         | Component |
| ------------------------------------------------ | --------- |
| What are the fundamental business rules?         | Domain    |
| What does the application want to do?            | Use Cases |
| What does the application need from the outside? | Ports     |
| How is that dependency actually implemented?     | Adapters  |

In this project:

```text
Physics equation
      ↓
Domain

Calculate and save energy
      ↓
Application

Need something capable of storing calculations
      ↓
Port

Python list
      ↓
Adapter
```

---

## 🔑 Main Lesson

Hexagonal Architecture is fundamentally about **decoupling**.

Instead of making the business logic depend directly on technologies such as PostgreSQL, FastAPI or cloud services, the application depends on abstractions.

```text
Concrete technology
        ↓
     Adapter
        ↓
      Port
        ↓
  Application
        ↓
     Domain
```

This makes external technologies replaceable while keeping the core logic stable.

---

## 🛠️ Technologies

* Python 3.12
* FastAPI
* Uvicorn
* uv
* pytest
* Docker

---

## 📚 Possible Next Step

Replace:

```text
InMemoryEnergyRepository
```

with:

```text
PostgresEnergyRepository
```

while keeping the following unchanged:

```text
domain/
application/
```

If that replacement can be made without changing the core logic, the architectural separation is working correctly.
