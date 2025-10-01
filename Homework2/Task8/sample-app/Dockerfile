# Use the JDK to compile java code
FROM bellsoft/liberica-openjdk-alpine:25-37 as java-build
WORKDIR /src
COPY ./MultiStageApp.java .
RUN javac MultiStageApp.java

# Use the JRE to run the compiled code
FROM bellsoft/liberica-openjre-alpine:25-37
WORKDIR /app
COPY --from=java-build /src/MultiStageApp.class ./
ENTRYPOINT ["java", "MultiStageApp"]