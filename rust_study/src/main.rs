use futures;
use futures::stream::{StreamExt};
#[tokio::main]
async fn main(){

    let paths = vec![
        "https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/102/52/1/1.json".to_string(),
    ];
    let fetches = futures::stream::iter(
        paths.into_iter().map(|path| {
            async move {
                match reqwest::get(&path).await {
                    Ok(resp) => {
                        match resp.text().await {
                            Ok(text) => {
                                println!("RESPONSE: {} bytes from {}", text.len(), path);
                                println!("RESPONSE TEST: {} ", text);
                            }
                            Err(_) => println!("ERROR reading {}", path),
                        }
                    }
                    Err(_) => println!("ERROR downloading {}", path),
                }
            }
        })
    ).buffer_unordered(8).collect::<Vec<()>>();
    println!("Waiting...");
    fetches.await;
}
// let url = "https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/102/52/1/1.json";


    