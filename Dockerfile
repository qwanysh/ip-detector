FROM python:3.9-slim
RUN pip install pipenv
RUN useradd --create-pages --pages-dir /app --shell /bin/bash app
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile --dev
USER app
COPY . .
