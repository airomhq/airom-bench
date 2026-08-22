import OpenAI from "openai";

const client = new OpenAI();

export async function summarize(text) {
  const res = await client.chat.completions.create({
    model: "gpt-4o-mini",
    max_tokens: 200,
    messages: [{ role: "user", content: `Summarize:\n${text}` }],
  });
  return res.choices[0].message.content;
}
