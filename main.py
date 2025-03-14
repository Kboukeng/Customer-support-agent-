from utils import get_openai_api_key
from crewai import crew
import warnings
import os

warnings.filterwarnings("ignore")

openai_api_key = get_openai_api_key
os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

inputs = {
    "customer": "DeepLearningAI",
    "person": "Andrew Ng",
    "inquiry": "I need help with setting up a Crew "
               "and kicking it off, specifically "
               "how can I add memory to my crew? "
               "Can you provide guidance?"
}
result = crew.kickoff(inputs=inputs)