FROM python:3.7-alpine3.10 as builder

RUN apk --no-cache upgrade && apk --no-cache add build-base tar musl-utils openssl-dev && pip3 install --upgrade pip
RUN pip3 install setuptools appdirs packaging cx_Freeze

COPY . .
RUN ln -s /lib/libc.musl-x86_64.so.1 ldd
RUN ln -s /lib /lib64
RUN pip3 install -r requirements.txt
RUN python3 setup.py build_exe

FROM alpine:3.10
RUN apk --no-cache upgrade && apk --no-cache add wget libffi expat
COPY --from=builder build/exe.linux-x86_64-3.7 /graviteeio/
RUN mkdir /graviteeio/config && chown -R nobody:nobody /graviteeio
USER nobody:nobody
ENV LC_ALL=en_US.utf8
ENV LD_LIBRARY_PATH=/graviteeio/lib
ENV GRAVITEEIO_CONF_FILE=/graviteeio/config/.graviteeio
VOLUME [ "/graviteeio/config/" ]
ENTRYPOINT ["/graviteeio/gio"]
