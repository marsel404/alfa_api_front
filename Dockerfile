FROM python:3.8
LABEL description='Фронтенд для данных с investing.com, ссылка на github: , Марсель Хасаншин, телеграм: @marsel_hasanshin'
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /alfa/investing_stats
COPY ./reqs.txt /alfa/reqs.txt
RUN pip install -r /alfa/reqs.txt
COPY . /alfa/investing_stats
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

