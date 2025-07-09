FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install typer rich requests pyyaml jinja2

COPY . .

ENTRYPOINT ["python", "-m", "guardrail_ci.cli"]
