FROM python:3.8.6

COPY . /housingpricingprediction

WORKDIR /housingpricingprediction

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "HPP:app", "--host", "0.0.0.0", "--port", "80"]