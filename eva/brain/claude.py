import anthropic
import logging


log = logging.getLogger(__name__)

class Claude:

    def __init__(self, api_key: str, model: str, max_tokens: int, effort: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.effort = effort
        
    
    def ask(self, text: str) -> str:
        response = self.client.messages.create(
            model= self.model,
            max_tokens=self.max_tokens,
            output_config={"effort": self.effort},
            messages=[{"role": "user", "content": text}],
        )
        answer = "".join(b.text for b in response.content if b.type == "text")
        log.info(answer)
        return answer


