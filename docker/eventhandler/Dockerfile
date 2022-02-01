FROM alpine:3.15

RUN apk update && apk add openjdk11-jre
COPY app /eventhandler

CMD ["/bin/sh", "-c", "cd /eventhandler && java -Xms64M -Xmx128M -Dlog4j.configurationFile=log4j2.xml -jar arrowhead-eventhandler.jar"]