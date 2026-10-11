
from eva.brain.claude import Claude
import logging


log = logging.getLogger(__name__)

def run_chat(brain: Claude):
    while True:
        try:
            query = input("ты: ").strip()
        except (KeyboardInterrupt, EOFError) as e:
            log.info("Действие отменено пользователем")
            break
       
        if not query:
            continue
        if query.lower() in ("выход", "exit"):
            break
        try:
            answer = brain.ask(query)
        except Exception as e:
            log.exception("Не удалось получить ответ")
            print("Ева: какая-то ошибка, попробуй еще раз.")
            continue
        print(f"Ева: {answer}")