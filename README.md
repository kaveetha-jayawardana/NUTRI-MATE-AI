
<h1 align = "center"> <b> 🥗 Nutri-Mate : Your Smart AI-Powered Weekly Meal Planner 🍽️ </b> </h1>

<div align="center">
  <img height="200" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExazE5bjhvM2twYjV5czZ2MDAydWgxN2xpNTQ4bm1tMzhoODU3bWpkdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RltQlCSRa2UMg/giphy.gif"  />
</div>
<br> 
<p align="justify"> <b>Nutri-Mate</b> is a smart AI agent that generates personalized weekly meal plans based on your physical attributes and dietary goals. Whether you're trying to lose weight, gain muscle, or maintain your health, NutriMate offers a balanced meal schedule, calorie breakdown, and even an AI-generated nutrition tip tailored to you.</p>

<p align="justify"> This is an AI-powered web application built with <b>Python + Streamlit</b>, that creates personalized weekly meal plans based on your body metrics, goals, and preferences. NutriMate is perfect for individuals who want a health-conscious and goal-oriented diet tailored just for them.</p>

<br>

## 🚀 Features

- 📥 Input your <b>height, weight, age, gender, activity level, and goal</b> (e.g., weight loss, weight gain, maintenance)

- 📊 Automatically calculates your **BMI** and **daily caloric needs**

- 🍽️ Generates a **complete weekly (7-day) meal plan (Breakfast, Lunch, Dinner and Snacks)** according to your inputs

- 💡 Provides an **AI-generated Nutrition Tip** based on your personal data

- 💬 Interactive, smart and dynamic user interface

<br>

## 🛠️ Technologies Used

- `Streamlit` for the user interactive frontend UI

- `Google Generative AI (Gemini)` for intelligent planning and AI-driven tips

- `Hugging Face Transformers` as an AI fallback engine

- `LangChain` for prompt management and response chaining

- `Python`, `Pandas` for backend logic, data processing and meal calculations

- `Torch` for model inference on Hugging Face pipelines

<br>

## 🎥 Demo Video
Watch how NutriMate works in action : [Click Here for the video](https://youtube.com/shorts/DrHyST4d9-8)

<br>

## 💡 How to Run Locally

1. Clone the repository

2. Set your Gemini API key as an environment variable:

```bash
export GOOGLE_API_KEY=your-key
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```
4. Install dependencies

5. Run the application :

```bash
streamlit run nutrimate_ai_app.py
```
<br>

## 📌 Notes

* The AI tip generator uses Gemini first. If the API fails or quota exceeds, it switches to Hugging Face.
* The LangChain interface structures and cleans up Hugging Face prompts.
* Tips are short and customized. If the BMI or goal does not require tips, the section will be blank or skipped.

---

Built by **KS Jayawardana** | BSc in Applied Data Science and Communication | KDU
