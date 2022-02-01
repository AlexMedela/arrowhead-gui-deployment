FROM alpine:3.15

RUN apk update && apk add openjdk11-jre
COPY app /gateway

CMD ["/bin/sh", "-c", "cd /gateway && java -Xms64M -Xmx128M -Dlog4j.configurationFile=log4j2.xml -jar arrowhead-gateway.jar"]