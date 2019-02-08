FROM alpine:3.8

RUN apk add --no-cache python3
RUN pip3 install --upgrade pip

#RUN pip3 install --no-cache terminal-translator

#for Dev
ADD . /translate-in-terminal
WORKDIR /translate-in-terminal
RUN pip3 install wheel
RUN python3 setup.py bdist_wheel
RUN pip3 install dist/terminal_translator-1.0.1-py3-none-any.whl -I
#end for Dev

ENTRYPOINT ["translate"]

