FROM alpine:3.8

RUN apk add --no-cache python3
RUN pip3 install --upgrade pip

#RUN pip3 install --no-cache terminal-translator

#for Dev
ADD . /translate-in-terminal
WORKDIR /translate-in-terminal
RUN pip3 install -e .
#end for Dev

ENTRYPOINT ["translate"]

