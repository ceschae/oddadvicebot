FROM python:3
ADD tweetbot.py /
ADD secrets.json /
ADD tweets.json /
RUN pip install twython
CMD [ "python", "./tweetbot.py" ]