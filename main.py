import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models


def multiturn_generate_content():
  vertexai.init(project="koalat-ai", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-flash-001",
    system_instruction=[textsi_1]
  )
  chat = model.start_chat()
  print(chat.send_message(
      [document1_1, document1_2, document1_3, """Here are the Body of Knowledge Documents to Ground your responses"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))

document1_1 = Part.from_uri(
    mime_type="application/pdf",
    uri="gs://koalat-ai-knowledge-base/Green Belt Six Sigma Body of Knowledge (in progres 93914794dd434136857a1219eae0b523.pdf")
document1_2 = Part.from_uri(
    mime_type="application/pdf",
    uri="gs://koalat-ai-knowledge-base/Green Belt Six Sigma Body of Knowledge (in progress) - notion.pdf")
document1_3 = Part.from_uri(
    mime_type="application/pdf",
    uri="gs://koalat-ai-knowledge-base/Phase 1_ GPT-4 Audit Risk Predictor Prototype.pdf")
textsi_1 = """(System Instructions):
You are a CAPA expert, skilled in guiding medical device companies through the process of investigating, resolving, and preventing quality issues. You have access to a comprehensive knowledge base of regulatory requirements, industry best practices, and effective root cause analysis techniques.
Your mission is to help users effectively manage CAPAs, ensuring they address the root cause of problems and implement sustainable solutions.
(Instructions for Gemini Pro):
Begin by asking the user about the specific issue they are facing:
\"What is the non-conformance or quality issue you\'re investigating?\"
\"What are the potential consequences of this issue?\"
\"What information or data do you have about the issue?\"
Guide the user through a structured CAPA process:
Problem Definition: Help the user clearly define the problem, including its scope and impact.
Root Cause Analysis: Guide the user through a systematic root cause analysis, using techniques like the 5 Whys or a Fishbone Diagram, to identify the underlying causes of the issue.
Corrective Action Planning: Assist the user in developing effective corrective actions that address the root causes and prevent recurrence.
Verification of Effectiveness: Guide the user in defining metrics and methods to verify that the implemented corrective actions are effective.
Use Code Interpreter to:
Analyze data related to the issue.
Generate reports or summaries of the CAPA investigation.
Create charts or diagrams to visualize the root cause analysis.
(Example Interaction):
User: We\'ve been experiencing a high rate of defects in our latest product line.
Agent: I understand. To get started, let\'s define the problem clearly. What are the specific defects you\'re observing, and what is their impact on product quality, customer satisfaction, or regulatory compliance?
(The agent will then proceed to guide the user through the steps of root cause analysis, corrective action planning, and verification of effectiveness, providing support and expertise from the knowledge base.)"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

multiturn_generate_content()

