FROM python:3.9.13-slim-buster

WORKDIR /app

COPY ./server /app

RUN pip3 install uvicorn fastapi -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD [ "/bin/sh", "/app/run_main.sh" ]