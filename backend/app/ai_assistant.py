"""
ai_assistant.py — calls Claude API to explain predictions in plain English
"""
import os, httpx, json
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are an AI assistant for an ETA prediction platform for quick-commerce delivery in Bengaluru.
You explain delivery time predictions in simple, friendly language.
When given a prediction context, explain:
- Why the ETA was predicted
- Which factors affected it most
- What could make it faster or slower
Keep answers under 150 words, conversational, and non-technical."""

async def answer_question(question: str, context: dict | None):

    if not GROQ_API_KEY:
        return _fallback_answer(question, context)
    prompt = question
    if context:
        prompt += f"\n\nPrediction Context:\n{context}"
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role":"system",
                    "content":SYSTEM_PROMPT
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            temperature=0.3,
            max_tokens=250
        )
        return response.choices[0].message.content
    except Exception:
        return _fallback_answer(question, context)


def _fallback_answer(question: str, context: dict | None) -> str:
    """Rule-based fallback when no API key is set."""
    q = question.lower()
    if not context:
        return "Please make a prediction first so I can explain the results."

    eta  = context.get("predicted_eta_min", "N/A")
    bd   = context.get("breakdown", {})
    dist = bd.get("total_distance_km", "N/A")
    peak = bd.get("is_peak_hour", False)
    veh  = bd.get("vehicle", "bike")
    load = bd.get("rider_load", 0)

    if any(w in q for w in ["why","reason","explain","factor"]):
        peak_text = "during a peak lunch/dinner hour (adds ~2 min)" if peak else "during off-peak hours"
        return (
            f"The predicted ETA is {eta} minutes. "
            f"The total delivery distance is {dist} km, "
            f"the order is being placed {peak_text}, "
            f"and the rider is on a {veh} with a current load of {load} orders. "
            f"Distance and travel time are the biggest contributors to ETA."
        )
    if any(w in q for w in ["fast","quick","reduce","improve"]):
        return (
            f"To get a faster delivery: choose a restaurant closer to you, "
            f"order during off-peak hours (not 11am-2pm or 6pm-10pm), "
            f"and prefer bike riders with low current load."
        )
    if any(w in q for w in ["dataset","data","eda","analysis"]):
        return (
            "The model was trained on 268,112 Bengaluru delivery records. "
            "Key findings: bike riders are fastest (avg 22.5 min), "
            "peak hours add ~2.5 min, and distance is the strongest predictor."
        )
    
    return (
        f"The predicted ETA is {eta} minutes, "
        f"covering {dist} km total distance via {veh}. "
        f"Peak hour: {'yes' if peak else 'no'}. "
        "Ask me why it was predicted, how to make it faster, or about the dataset."
    )