using Microsoft.SemanticKernel;

var builder = Kernel.CreateBuilder();
builder.AddOpenAIChatCompletion(modelId: "gpt-4o-mini", apiKey: Environment.GetEnvironmentVariable("OPENAI_API_KEY")!);
var kernel = builder.Build();
Console.WriteLine(await kernel.InvokePromptAsync("Summarize the sprint."));
