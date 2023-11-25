FROM python:3
WORKDIR /usr/src/bot-client-app
COPY . ./
RUN pip install python-dotenv
RUN pip install discord && pip install requests && pip install pymongo
COPY *.py .
CMD [ "python", "./bot.py" ]