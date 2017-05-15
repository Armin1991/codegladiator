FROM python:2
RUN pip install flask && \
    pip install flask_restful && \
    pip install pymongo && \
    pip install requests
VOLUME codegladiator
COPY databaseCommunicator codegladiator/dbCommunicator
CMD ["mkdir","codegladiator/dbCommunicator/logs"]
CMD ["python","codegladiator/backend/databaseCommunicator/main.py"]
