from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests
import json

NLP_MODEL_ENDPOINT= "http://127.0.0.1:5000/get_completion"
class Request(Model):
    text: str


class Error(Model):
    text: str


class Data(Model):
    data: str

# Send a prompt and context to the AI model and return the content of the completion
def send_request_to_nlp_model(text: str):
    try:
        response = requests.post(NLP_MODEL_ENDPOINT, data={"text": text})
        response_data = response.text
        return response_data
    except Exception as ex:
        print(f"Error communicating with the NLP model: {ex}")
        return Error(text="Sorry, there was an error processing your request.")


alice = Agent(
    name = "alice",
    port = 8000,
    seed = "alice new recovery phrase",
    endpoint= ["http://127.0.0.1:8000/submit"],
    )
# Message handler for data requests sent to this agent

print("uAgent address", alice.address)

@alice.on_message(model=Request)
async def handle_request(ctx: Context, sender: str, request: Request):
    ctx.logger.info(f"Got request from user")
    response = send_request_to_nlp_model(request.text)
    await ctx.send(sender, Data(data=response))

if __name__  == "__main__":
    alice.run()
