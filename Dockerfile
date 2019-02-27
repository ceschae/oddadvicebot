FROM python:3
ADD tweetbot.py /
RUN pip install twython
CMD [ "python", "./tweetbot.py" ]