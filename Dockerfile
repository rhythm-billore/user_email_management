FROM python:3.10-slim
COPY . /user_email_management
WORKDIR /user_email_management
RUN pip install -r requirements.txt
EXPOSE 8501
CMD streamlit run app_db_connection.py 