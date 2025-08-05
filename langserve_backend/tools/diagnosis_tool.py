from langchain.tools import tool
from utils.euri_client import chat_completion


@tool
def ai_diagnosis(symptom_description):
    """uses euri to provide the diagnosis suggestion based on the symptom given by users"""
    message = [{"role":"user", "content": f"a patient reports: {symptom_description}. what are the possible diagnoses and next step and even suggest me cure for this one"}]
    
    return chat_completion(messagges=message)
