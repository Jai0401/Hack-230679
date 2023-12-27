from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
# This Agent can ask a question to the AI model Agent and display the answer.

# Paste your resume Text
RESUME = """WORK EXPERIENCE
Gametime - Mid-Level Front-End Developer
January 2019 - current Remote
Worked with design, product, and back-end teams to create 12 web products.
Created 3 efficient and reusable front-end systems to drive web applications to the marketplace.
Participated in product releases and code reviews with 5 senior developers and team leads.
Supervised, led, and mentored 11 junior team members to achieve high performance and meet goals.
Kaiser Permanente - Front-End Developer
August 2017 - January 2019 Walnut Creek, CA
Collaborated with 6 other team members and 4 stakeholders to develop 16 new user-facing features.
Assisted in building 100% reusable code and libraries for future use.
Ensured the technical feasibility of 150+ UI/UX designs.
Optimized 15+ applications for maximum speed and scalability.
Validated 100% of user input before submitting to the back-end.
PLACE - Junior Front-End Developer
June 2015 - August 2017 Remote
Delivered 30+ projects of all sizes, creating solutions for consumer services.
Wrote 40+ automated tests for every new feature to identify and rectify bugs.
Evaluated 100+ end-to-end designs for performance complexity, scalability, quality, and security.
SKILLS
HTML
CSS
JavaScript
React.js
CERTIFICATIONS
AWS
EDUCATION
University of the Pacific - Bachelor of Science, Computer Science"""


AI_MODEL_AGENT_ADDRESS = "agent1qghqvn2eg6x9mdprk7m449rg95pd5tgqcy56c48tknl2gcultky37es4076"


class Request(Model):
    text: str


class Error(Model):
    text: str


class Data(Model):
    data: str

bob= Agent(
    name = "bob",
    port = 8001,
    seed = "bob new recovery phrase",
    endpoint= ["http://127.0.0.1:8001/submit"],
    )

@bob.on_interval(3600)
async def ask_question(ctx: Context):
    ctx.logger.info(f"Sending resume data to AI bob")
    await ctx.send(AI_MODEL_AGENT_ADDRESS, Request(text=RESUME))

@bob.on_message(model=Data)
async def handle_data(ctx: Context, sender: str, data: Data):
    ctx.logger.info(f"Your resume has been evaluated, and the score is determined comparing with our job description {data}. This score reflects an assessment based on various factors and criteria.")

@bob.on_message(model=Error)
async def handle_error(ctx: Context, sender: str, error: Error):
    ctx.logger.info(f"Got error from AI model bob: {error}")

if __name__  == "__main__":
    bob.run()
