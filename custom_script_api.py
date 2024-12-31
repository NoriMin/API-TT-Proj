from quart import Quart, request, jsonify
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

app = Quart(__name__)

@app.route('/api/browser-use', methods=['POST'])
async def browser_use_api():
    # data = await request.json
    # task = data.get('task')
    task = await request.get_json()
    
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    )
    result = await agent.run()
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)