FROM eclipse-temurin:17-jdk-alpine as build
WORKDIR /workspace/app

# Install build dependencies
RUN apk add --no-cache bash protobuf protobuf-dev

COPY . .
RUN chmod +x ./gradlew
RUN ./gradlew build -x test

FROM eclipse-temurin:17-jre-alpine
VOLUME /tmp
COPY --from=build /workspace/app/build/libs/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"] 