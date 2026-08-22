package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/sashabaranov/go-openai"
)

func main() {
	client := openai.NewClient(os.Getenv("OPENAI_API_KEY"))
	resp, err := client.CreateChatCompletion(context.Background(), openai.ChatCompletionRequest{
		Model:     "gpt-4o",
		MaxTokens: 300,
		Messages:  []openai.ChatCompletionMessage{{Role: "user", Content: "draft release notes"}},
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(resp.Choices[0].Message.Content)
}
