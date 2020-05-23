FROM darkkjm2002/pytorch_flask:0.1

ADD . /workspace

CMD ["python", "/workspace/app.py"]