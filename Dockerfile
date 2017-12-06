FROM frolvlad/alpine-python3
COPY . .
WORKDIR app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
ENTRYPOINT [ "flask", "run" , "--host", "0.0.0.0", "--port", "1905"]