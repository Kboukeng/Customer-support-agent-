from crewai import Crew
from agents import support_quality_assurance_agent, support_agent
from tasks import inquiry_resolution, quality_assurance_review

crew = Crew(
  agents=[support_agent, support_quality_assurance_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=2,
  memory=True
)