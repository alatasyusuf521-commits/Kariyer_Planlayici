from pathlib import Path
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import json
import os

# .env dosyasını yükle (proje kökünde, agents klasörünün bir üstünde)
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


# kariyer planlama ajanı sınıfı tanımla
class CarerGoalAgent:
    # constructor fonksiyonu
    def __init__(self, model_name="openai/gpt-oss-120b"):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=0.5,
            openai_api_key=os.environ["GROQ_API_KEY"],
            openai_api_base="https://api.groq.com/openai/v1",
        )

    # kullanıcıdan gelen hedef meslek bilgisine göre kariyer yol haritası oluşturma
    def ask_career_goal(self, user_input):
        messages = [
            SystemMessage(content=(
                "Sen bir kariyer planlama asistanısın. Kullanıcı bir meslek söylediğinde, "
                "bu mesleğe ulaşmak için adım adım bir yol haritası üret. "
                "Sonuçları *sadece* aşağıdaki formatta JSON olarak döndür:\n\n"
                "{\n \"adımlar\": [\"...\", \"...\", ...]\n}"
            )),
            HumanMessage(content=f"Hedef mesleğim: {user_input}.")
        ]

        response = self.llm.invoke(messages)

        return self.parse_response(response.content)

    def parse_response(self, response_text):
        text = response_text.strip()
        # Model cevabı ```json ... ``` bloğu içinde verirse temizle
        if text.startswith("```"):
            text = text.strip("`")
            text = text.removeprefix("json").strip()
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"Hata": "Modelden gelen yanıt JSON formatında değil.", "ham_yanit": response_text}