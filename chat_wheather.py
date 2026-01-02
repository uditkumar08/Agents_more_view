import json
import requests
from groq import Groq

from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city: str):
    print(f"Tool called: get_weather({city})")

    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to fetch weather data"

    data = response.json()

    current = data["current_condition"][0]
    temp = current["temp_C"]
    desc = current["weatherDesc"][0]["value"]

    return f"{temp}°C, {desc}"

available_tool = {
    "get_weather":{
        "fn":get_weather,
        "description":"Takes a city name as an input and returns the current weather for the city"
    }
}

system_prompt = """
   
    You are help full AI Assistant who is specialized in resolving user query.
    You work on start , plan , action , observe mode.
    For the given user query and available tools, plan the step by step execution , based on the planning,
    select the relevant tool from the available tool. And based on the tool selection you perform an action to call the tool.
    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    -Follow the Output JSON Format.
    -Always perform one step at a time and wait for next input
    -Carefully analyse the user query.

    Output JSON Format:
    {{
    
        "step":"string",
        "content":"string",
        "function":"THe name of function if the step is action",
        "input":"The input parameter for the function"
    
    }}

    Available Tools:
    -get_weather : Takes a city name as an input and returns the current weather for the city

    Example:
    User Query: What is the weather of new york?
    Output: {{"steps": "plan","content" : "The user is interested int he weather data of new york"}}
    Output: {{"steps": "plan","content" :"From the available tools I should call get_weather"}}
    Output: {{"steps": "action","function" : "get_weather": "input":"new york"}}
    Output: {{"steps": "observe","output" : "12 Degree Cel"}}
    Output: {{"steps": "output","content" : "The weather for new york seems to be 12 degrees"}}

"""
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

messages = [
    {"role":"system","content":system_prompt}
]

user_query = input('> ')
messages.append({"role":"user","content":user_query})
while(True):
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    response_format={"type":"json_object"},
    messages=messages
    )
    
    parsed_output = json.loads(response.choices[0].message.content)
    messages.append({"role":"assistant","content":json.dumps(parsed_output)})

    if parsed_output.get("step") == "plan":
        print(f"🧠: {parsed_output.get('content')}")
        continue

    if parsed_output.get("step") == "action":
        tool_name = parsed_output.get("function")
        tool_input = parsed_output.get("input")

        if available_tool .get(tool_name,False)!=False:
            output = available_tool[tool_name].get("fn")(tool_input)
            messages.append({"role":"assistant","content":json.dumps({"step":"observer","output":output})})
            continue
    
    if parsed_output.get("step") == "output":
                print(f"🤖: {parsed_output.get('content')}")
                break
                




## chain thought in t.txt  above are organized automated type
