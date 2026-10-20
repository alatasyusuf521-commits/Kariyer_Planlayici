from agents.carrer_goal_agent import CarerGoalAgent
from agents.task_scheduler_agent import TaskSchedulerAgent
from tools.suggestion_tool import SuggestionTool
from memory.user_memory import UserMemory
from dotenv import load_dotenv
import json
import os


load_dotenv()

if __name__ == "__main__":

    print("kariyer planlayıcısı")

    user_memory = UserMemory()

    goal = input("Hedef mesleğiniz nedir?")

    user_memory.update_goal(goal)

    # yol haritası oluştur
    goal_agent = CarerGoalAgent()
    roadmap = goal_agent.ask_career_goal(goal)

    print("Yol haritanız: \n")
    print(json.dumps(roadmap, indent=2, ensure_ascii=False))

    # zamanlama yap
    num_week = 4
    scheduler = TaskSchedulerAgent(weeks=num_week)
    schedule = scheduler.create_schedule(roadmap)
    scheduler.save_schedule(schedule)

    print(f"\n {num_week} Haftalık plan: ")
    print(json.dumps(schedule, indent=2, ensure_ascii=False))

    # kaynak önerisi
    suggestor = SuggestionTool()
    topic = input("Bir beceri başlığı girin (kaynak önerisi için)")
    results = suggestor.search_resources(topic)

    print("kaynak önerileri")

    for r in results:
        title = r.get("title", "Başlık yok")
        link = r.get("link") or r.get("href") or r.get("url", "")
        snippet = r.get("snippet") or r.get("body") or r.get("content", "")
        print(f" - {title} \n {link} \n {snippet} \n")