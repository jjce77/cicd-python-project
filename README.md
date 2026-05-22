# CI/CD Python Project

## Summary & Core Objectives

* Purpose: To automate the lifecycle of python applications, ensuring early-stage code quality and optimizing infrastructure costs for a laboratory environment.

This repository contains three Python programming tasks integrated with a CI/CD flow. The Python exercises are the vehicle for the pipeline; the process is the main objective.

## Project structure

- `app/`: Source code.
- `tests/`: Unit tests.
- `.github/workflows/`: CI/CD automation pipelines.
- `docs/`: Execution plan, implementation guide, and final summary.

## Tech stack

- Development: Python 3.12, FastAPI.
- Quality: Ruff, Pytest, SonarQube Cloud.
- Packaging: Docker, GitHub Container Registry.
- Automation: GitHub Actions.
- Deployment: Render, AWS EC2.

## Git workflow strategy

- `dev`: Development branch for linting, tests, coverage, and SonarQube.
- `qa`: Quality branch for Docker build, image publication, and validation in Render.
- `main`: Final integration branch and source for AWS EC2 deployment.

## Workflow overview


```mermaid
flowchart TD
    A[<b>dev branch</b> \n Triggers: Pytest + Ruff + SonarCloud] --> C([Merge / PR])
    C --> D[<b>qa branch</b> \n Triggers: Docker Bbild + Render deploy]
    D --> F([Merge / PR])
    F --> G[<b>main branch</b> \n Triggers: AWS EC2 Deploy]


    classDef dev fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111827;
    classDef qa fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111827;
    classDef main fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#111827;
    classDef step fill:#f9fafb,stroke:#6b7280,stroke-width:1.5px,color:#111827;

    class A dev;
    class B,C step;
    class D qa;
    class E,F step;
    class G main;
    class H step;
```


## Validation

- Run lint with `ruff check .`.
- Run tests with `pytest`.
- Generate coverage with `pytest --cov-report=xml`.
- Validate the health endpoint with `python -m uvicorn app.main:app --reload` and `http://127.0.0.1:8000/health` after activating the virtual environment.
- Validate the Python tasks manually from the terminal:
  - `Dictionary`.
  - `get_total`.
  - `build_word`.

## Deployment

- `qa` publishes the Docker image to GHCR and deploys it to Render.
- `main` triggers deployment to AWS EC2.
- The EC2 service exposes `/health` on port `8000`.
