import anthropic
import json
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

# Реальна функція
def get_weather(city: str) -> str:
    # Симулюємо відповідь (без реального API)
    weather_data = {
        "Kyiv": "Rainy, 12°C",
        "London": "Cloudy, 15°C",
        "Lviv": "Sunny, 18°C"
    }
    return weather_data.get(city, "Unknown city")


def search_documents(query: str) -> str:
    docs = {
        "return policy": "Items can be returned within 30 days with receipt.",
        "shipping": "Free shipping on orders over $50. Standard delivery 3-5 days.",
        "warranty": "All products have 1 year manufacturer warranty."
    }
    for key, value in docs.items():
        if key in query.lower():
            return value
    return "No relevant documents found."


def create_ticket(issue: str, priority: str) -> str:
    ticket_id = f"TKT-{hash(issue) % 10000:04d}"
    return f"Ticket {ticket_id} created. Issue: {issue}. Priority: {priority}"

# Опис інструменту для Claude
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["city"]
        }
    },
    {
        "name": "search_documents",
        "description": "Search company knowledge base for policies, shipping info, warranty details and other business information",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "document type"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "create_ticket",
        "description": "Ticket creating",
        "input_schema": {
            "type": "object",
            "properties": {
                "issue": {
                    "type": "string",
                    "description": "The ticket receiving reason"
                },
                "priority": {
                    "type": "string",
                    "description": "The ticket priority"
                }
            },
            "required": ["issue", "priority"]
        }
    }
]




def run_agent(user_message: str):
    messages = [{"role": "user", "content": user_message}]
    
    while True:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            tools=tools,
            messages=messages
        )
        
        if response.stop_reason == "end_turn":
            print(f"\nFinal answer: {response.content[0].text}")
            break
            
        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"Calling: {block.name}({block.input})")
                    
                    if block.name == "get_weather":
                        result = get_weather(**block.input)
                    elif block.name == "search_documents":
                        result = search_documents(**block.input)
                    elif block.name == "create_ticket":
                        result = create_ticket(**block.input)
                    
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            
            messages.append({"role": "user", "content": tool_results})

run_agent("What is your return policy?")
run_agent("I can't find my order and need urgent help")
run_agent("What's the weather in London and what's your shipping policy?")