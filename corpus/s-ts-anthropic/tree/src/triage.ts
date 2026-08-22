import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

export async function triage(review: string): Promise<string> {
  const msg = await client.messages.create({
    model: "claude-3-5-haiku-20241022",
    max_tokens: 150,
    messages: [{ role: "user", content: review }],
  });
  return msg.content[0].type === "text" ? msg.content[0].text : "";
}
