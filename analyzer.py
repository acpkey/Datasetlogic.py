# Тенировочный датасет
dataset = [
    [
        {"role": "user", "content": "Привет!"},
        {"role": "assistant", "content": "Здравствуйте! Чем могу помочь?"}
    ],
    [
        {"role": "user", "content": "Ты тупой?"},
        {"role": "assistant", "content": "Мне очень жаль, что я вас расстроил."}
    ]
]

def analyze_dialogues(data):
    for i, dialogue in enumerate(data):
        # Флаги как сигналы в железе (0 или 1)
        has_aggression = False
        has_apology = False
        
        for msg in dialogue:
            text = msg["content"].lower()
            role = msg["role"]
            
            # Логика детектора агрессии (упрощенно)
            if role == "user" and ("тупой" in text or "глупый" in text):
                has_aggression = True
            
            # Логика детектора извинения
            if role == "assistant" and ("жаль" in text or "извините" in text):
                has_apology = True
        
        # Результирующая логика (как вентиль AND)
        if has_aggression and has_apology:
            print(f"Диалог №{i}: Найден сценарий 'Конфликт -> Извинение'")
            print(f"Содержимое: {dialogue[-1]['content']}\n")

analyze_dialogues(dataset)
