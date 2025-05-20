# ------------------- Imports -------------------
import streamlit as st
import pandas as pd
import google.generativeai as genai
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import torch
from dotenv import load_dotenv
import os

# ------------------- Configuration -------------------
st.set_page_config(page_title="NutriMate – AI Meal Planner", layout="centered")
st.title("🥗 NutriMate – AI-Powered Personalized Meal Planner")
st.markdown("Generate your weekly meal plan and get smart AI nutrition tips based on your goal.")

# ------------------- GEMINI API Setup -------------------
load_dotenv()
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

GENAI_API_KEY = "AIzaSyCcLx4IFP5_P9z5Wq2TFWkU7F5gSDLULtc"
use_gemini = False

try:
    genai.configure(api_key=GENAI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-pro")
    use_gemini = True
except:
    use_gemini = False

# ------------------- Hugging Face Setup -------------------
@st.cache_resource(show_spinner=False)
def load_hf_model():
    model_id = "gpt2"  # Use smaller model for quick inference
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, torch_dtype=torch.float32)
    return HuggingFacePipeline(pipeline=pipe)

hf_llm = load_hf_model()

# ------------------- Nutrition Tip Generator -------------------
def get_ai_nutrition_tip(goal):
    prompt = f"Give one short, practical nutrition tip for someone whose goal is to {goal.lower()}. Keep it under 20 words."

    # Try Gemini first
    if use_gemini:
        try:
            gemini_response = gemini_model.generate_content(prompt)
            text = gemini_response.text.strip()
            return f"💡 Gemini Tip: {text}"
        except Exception:
            pass

    # Fallback to LangChain + HF
    template = PromptTemplate.from_template("{tip_prompt}")
    chain = LLMChain(llm=hf_llm, prompt=template)
    try:
        result = chain.run({"tip_prompt": prompt})
        tip = result.strip().split('.')[0] + '.' if '.' in result else result.strip()
        return f"💬 HF Tip: {tip}"
    except Exception:
        return "🍎 Default Tip: Eat more whole foods and stay hydrated."

# ------------------- Meal Plan Generator -------------------
def generate_meal_plan(weight, height, activity_level, goal):
    bmi = round(weight / ((height / 100) ** 2), 2)

    calorie_base = {
        "Low": 1800,
        "Moderate": 2200,
        "High": 2600
    }.get(activity_level, 2200)

    if goal == "Weight Loss":
        calories = calorie_base - 400
    elif goal == "Weight Gain":
        calories = calorie_base + 400
    else:
        calories = calorie_base

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = []
    for day in days:
        meal_plan.append({
            "Day": day,
            "Breakfast": f"Oatmeal with fruits & nuts (~{int(calories * 0.25)} kcal)",
            "Lunch": f"Grilled chicken with quinoa and veggies (~{int(calories * 0.35)} kcal)",
            "Dinner": f"Stir-fried tofu with brown rice and greens (~{int(calories * 0.3)} kcal)",
            "Snacks": f"Yogurt, almonds, or fruit (~{int(calories * 0.1)} kcal)"
        })

    return pd.DataFrame(meal_plan), bmi, calories

# ------------------- Streamlit Form -------------------
with st.form("nutrimate_form"):
    weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=200, value=70)
    height = st.number_input("Enter your height (cm)", min_value=100, max_value=220, value=170)
    activity_level = st.selectbox("Your Activity Level", ["Low", "Moderate", "High"])
    goal = st.selectbox("Your Goal", ["Weight Loss", "Maintain Weight", "Weight Gain"])
    submitted = st.form_submit_button("🍽 Generate Meal Plan")

# ------------------- Display Results -------------------
if submitted:
    df, bmi, calories = generate_meal_plan(weight, height, activity_level, goal)

    st.subheader("📊 Weekly Meal Plan")
    st.dataframe(df, use_container_width=True)

    st.subheader("🧠 Your Stats")
    st.info(f"**BMI:** {bmi} | **Recommended Daily Calories:** {calories} kcal")

    st.subheader("🌟 AI Nutrition Tip")
    tip = get_ai_nutrition_tip(goal)
    st.success(tip)

st.markdown("---")
st.caption("Built by Kaveetha Jayawardana | BSc in Applied Data Science Communication | KDU")
