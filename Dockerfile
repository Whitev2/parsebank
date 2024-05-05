# Отдельный сборочный образ, чтобы уменьшить финальный размер образа
FROM python:3.11 as compile-image
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY app/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Окончательный образ
FROM python:3.11
COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /bankparser

COPY ./app ./app


EXPOSE 80

ENTRYPOINT ["uvicorn", "app.server:app", "--reload", "--host", "0.0.0.0", "--port", "80", "--access-log"]
#ENTRYPOINT ["ls"]
