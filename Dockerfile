FROM python:3.9

WORKDIR /bcfm-api
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]