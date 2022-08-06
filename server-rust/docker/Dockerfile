FROM rust:slim-buster

USER root

WORKDIR /app

COPY ./server-rust /app

RUN cargo build --release

CMD ["/app/target/release/server-rust"]