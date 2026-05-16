# epam-python-cicd-tasks
This repository contains a series of Python programming tasks integrated with continuous integration and continuous delivery (CI/CD) workflows. 

## Project Structure

- `app/`: Source code.
- `tests/`: unit tests.
- `.github/workflows/`:  CI/CD automation pipelines

## Git Workflow Strategy


- `dev`: Everyday development branch where new tasks and code features are written.
- `qa`: Testing and quality assurance branch.
- `main`: Production-ready branch. 


*Note: Direct pushes to `main` and `QA` are restricted. Code can only enter `main` via a Pull Request originating strictly from the `QA` branch.*


