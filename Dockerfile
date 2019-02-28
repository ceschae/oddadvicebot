FROM python:3
ADD tweetbot.py /
ADD generatetweets.py /
ADD secrets.json /
ADD tweets.json /
ADD advice.txt /
RUN pip install twython
CMD [ "python", "./tweetbot.py" ]