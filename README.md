# GreenDesk - IT Asset Management API

API for managing and controlling the inventory of technical equipment (Laptops, Monitors, Peripherals). The system allows registering new assets and querying the existing inventory through a REST interface.

## Technologies Used

- **FastAPI**: Primary framework for building the API
- **SQLAlchemy 2.0**: ORM for database management with modern typing
- **PostgreSQL**: Relational database engine
- **Docker & Docker Compose**: Application and service containerization
- **Pydantic**: Data validation and DTO schemas

## Installation and Execution

### Prerequisites

- Docker
- Docker Compose

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd it-asset-manager
   ```

2. **Configure environment variables:**

   Create a `.env` file at the root of the project with the following content:

   ```env
   DB_USER=****
   DB_PASSWORD=****
   DB_NAME=****
   DB_PORT==****
   PGADMIN_EMAIL==****
   PGADMIN_PASSWORD==****
   ```

3. **Start the services:**
   ```bash
   docker-compose up --build
   ```

## API Documentation

Once the containers are running, you can access the interactive documentation (Swagger UI) at:

```
http://localhost:8000/docs
```

### Main Endpoints

- **GET /devices/**: Lists all registered equipment with pagination
- **POST /devices/**: Registers a new asset in the system

## Database Management

pgAdmin 4 is included for data inspection and administration:

- **URL**: http://localhost:5050
- **Username/Password**: Defined in the `.env` file