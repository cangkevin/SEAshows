# SEAshows

![Mainline status](https://github.com/cangkevin/SEAshows/actions/workflows/main.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/cangkevin/SEAshows/badge.svg?branch=main)](https://coveralls.io/github/cangkevin/SEAshows?branch=main)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/568adf9d5c824379aa087f1b54dcb565)](https://app.codacy.com/app/cangkevin/SEAshows?utm_source=github.com&utm_medium=referral&utm_content=cangkevin/SEAshows&utm_campaign=Badge_Grade_Settings)

## What is SEAshows?

SEAshows is a small project that serves as a hub for east-asian shows and programming.

Current content that is supported:

- HK Dramas
- HK Variety and News
- HK Movies
- Chinese Dramas
- Chinese Movies
- Korean Dramas
- Korean Movies
- Taiwanese Dramas

SEAshows's user experience is targeted towards a particular demographic, particularly those who are not computer-savvy. There is future work planned to make the site more feature-rich for navigation and searching.

## Local development

### Environment setup

This projects uses `pipenv`. It is recommended to install `pipenv` via `pipx`.

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install pipenv
```

Once `pipenv` is installed, install the project's virtual environment and dependencies.

```bash
pipenv install --dev
```

Install the project's `pre-commit` hooks.

```bash
pipenv run pre-commit install
```

Create a `.env` file at the root of the project with the following:

```text
FLASK_APP=seashows.py
FLASK_ENV=development
SECRET_KEY=dev
BASE_URL=<SOURCE URL>
ELASTICSEARCH_URL=http://localhost:9200
```

where `<SOURCE_URL>` is the remote data source.

Finally, activate the virtual environment.

```bash
pipenv shell
```

### Running the project

To run the development server

```bash
flask run
```

### Conventions

This project adheres to [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/#specification) for the commit message. This is intended to drive the automated versioning strategy for the application based on the messages in the commit history.
