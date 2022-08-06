/*
 * @Author: shiyun.ling shiyun.ling@flexiv.com
 * @Date: 2022-08-06 15:18:07
 * @LastEditors: shiyun.ling
 * @LastEditTime: 2022-08-06 15:22:46
 * @Description: file content
 */
use actix_web::{get, App, HttpServer, Responder};

#[get("/200")]
async fn return_200() -> impl Responder {
    "200"
}

#[actix_web::main]
async fn main() -> Result<(), std::io::Error>{
    HttpServer::new(|| App::new().service(return_200))
        .bind("0.0.0.0:8080")
        .expect("failed to bind addr")
        .run()
        .await
}
