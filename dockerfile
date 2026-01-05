FROM python:3.12
WORKDIR / docker_student_detils
COPY . .
CMD ["python", "student_detils.py"]