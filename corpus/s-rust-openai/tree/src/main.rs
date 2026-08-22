use async_openai::{types::CreateChatCompletionRequestArgs, Client};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();
    let request = CreateChatCompletionRequestArgs::default()
        .model("gpt-4o-mini")
        .max_tokens(256u32)
        .build()?;
    let response = client.chat().create(request).await?;
    println!("{}", response.choices[0].message.content.clone().unwrap_or_default());
    Ok(())
}
