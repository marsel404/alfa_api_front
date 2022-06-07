FROM python:3.9.3
LABEL description='Фронтенд для данных с investing.com, ссылка на github: https://github.com/marsel404, Марсель Хасаншин, телеграм: @marsel_hasanshin'
WORKDIR /investing_stats
COPY reqs.txt .
RUN pip install -r reqs.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
