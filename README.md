# QZ -- Modular Language Learning Platform (Django REST API)

QZ is a scalable backend platform for managing learning modules,
flashcards, topics, folders, and user interactions.\
Built with **Django + Django REST Framework** using clean architecture
and policy-based permissions.

------------------------------------------------------------------------

## 🚀 Features

### Core Learning System

-   Modules, topics, folders
-   Flashcards with translations
-   Language system
-   Tags and visibility (public/private)

### User Interactions

-   Save cards and modules
-   Learning progress tracking
-   Generic status system

### Advanced Permissions

-   Policy registry per action
-   Object-level ACL (owner, editor, viewer, admin)
-   Chain-of-responsibility queryset filtering

### Infrastructure

-   Celery background tasks
-   Scheduled task system
-   Docker support
-   Swagger / OpenAPI docs
-   Filtering & pagination
-   Demo fixtures

------------------------------------------------------------------------

## 🏗 Project Structure

    qz/
    ├── abstracts/
    ├── cards/
    ├── common/
    ├── folders/
    ├── generic_status/
    ├── interactions/
    ├── languages/
    ├── modules/
    ├── topics/
    ├── users/
    ├── users_auth/
    ├── qz/

------------------------------------------------------------------------

## 🧠 Architecture Highlights

### Policy-Based Permissions

Each ViewSet registers policies dynamically:

``` python
FolderViewSet.policies.register("retrieve", RETRIEVE_POLICY)
```

### Query Access Chains

Dynamic queryset filtering based on user:

``` python
OwnerIncludedLink -> PublicIncludedLink -> RoleLink
```

### Repository & Service Layers

Business logic separated from views.

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   Django 5.x
-   Django REST Framework
-   PostgreSQL
-   Celery + Redis + RabbitMQ
-   Docker
-   drf-spectacular (Swagger)
-   django-filter
-   taggit

------------------------------------------------------------------------

## 🐳 Installation

### Clone

``` bash
git clone https://github.com/Sp-line/<repo>.git
cd <repo>
```

### Create env

``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run services

``` bash
docker-compose up -d
```

### Migrate & run

``` bash
python manage.py migrate
python manage.py loaddata */fixtures/*.json
python manage.py runserver
```

------------------------------------------------------------------------

## 🔧 Celery

``` bash
celery -A qz worker -l info
celery -A qz beat -l info
```

------------------------------------------------------------------------

## 📑 API Docs

    /api/schema/
    /api/docs/

------------------------------------------------------------------------

## 📌 Key Concepts Implemented

-   Domain-driven modular apps
-   Policy registry pattern
-   Generic interaction system
-   Repository + Service layers
-   Clean DRF ViewSet architecture
-   Advanced queryset annotations
-   Scheduled background tasks

------------------------------------------------------------------------

## 🧪 Testing

``` bash
pytest
```

------------------------------------------------------------------------

## 📜 License

MIT License
