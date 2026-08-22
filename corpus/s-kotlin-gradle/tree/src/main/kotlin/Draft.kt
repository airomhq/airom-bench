import com.aallam.openai.api.chat.ChatCompletionRequest
import com.aallam.openai.api.model.ModelId
import com.aallam.openai.client.OpenAI

suspend fun draft(openAI: OpenAI, notes: String): String {
    val request = ChatCompletionRequest(
        model = ModelId("gpt-4o-mini"),
        messages = listOf(),
    )
    return openAI.chatCompletion(request).choices.first().message.content.orEmpty()
}
