package app;

import dev.langchain4j.model.openai.OpenAiChatModel;

public final class FaqBot {
    private final OpenAiChatModel model = OpenAiChatModel.builder()
            .modelName("gpt-4o-mini")
            .temperature(0.2)
            .build();

    public String answer(String question) {
        return model.generate(question);
    }
}
