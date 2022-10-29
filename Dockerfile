FROM python:3.10.6

WORKDIR /Flask-dataScience

COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install openpyxl

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]