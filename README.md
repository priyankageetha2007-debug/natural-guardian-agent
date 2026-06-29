## Natural Guardian Agent: Intelligent Botanical Consultant
## CropShield AI: 
The Natural Guardian Agent is an AI-powered diagnostic agent designed to assist farmers and gardeners in identifying crop diseases and providing instant, actionable solutions.

## 🎥 Demo Video
https://youtu.be/3qq1YX_9G8Y?si=jnXwLQmXvTCu10Rk

## 🎯 Problem Statement
Farmers often face significant crop losses due to the inability to identify plant diseases in the early stages. This agent acts as a "Natural Guardian," providing expert-level diagnosis based on symptoms.

## 🏗️ Architecture
The Natural Guardian Agent is built on a robust agentic workflow that leverages Google's Gemini Pro for logic and specific tools for domain data.
<img width="1408" height="768" alt="Gemini_Generated_Image_n1w5g1n1w5g1n1w5" src="https://github.com/user-attachments/assets/3120e682-dff0-436b-853c-1ca23e4b7579" />

### Core Components
1. **User Input:** The user provides plant symptoms or queries regarding crop health.
2. **Reasoning Engine (Gemini Pro):** The model analyzes the input and performs **Tool Invocation** to decide the best course of action.
3. **Tool Execution:**
   - **`get_remedy`**: Fetches specific medical treatments, natural remedies, and prevention tips based on the disease ID.
   - **`find_diseases_by_crop`**: Performs a database lookup to list potential threats for a given crop.
4. **Actionable Response:** The agent synthesizes the output and provides a clear, concise, and expert-level diagnosis/treatment plan.


## 🌟 Key Features
1.Disease Diagnosis: Identifies diseases based on symptoms provided by the user.

2.Actionable Advice: Provides instant treatment steps and preventive measures.

3.Agentic Workflow: Built using a structured ReAct pattern for accurate reasoning and tool execution.

## 🛠️ Technologies Used
AI Engine: Google Gemini

Framework: Python, Agent Development Kit (ADK)

Tooling: Kaggle AI Agents Tools

## How to Run
1. Clone this repository.
   ```bash
   git clone https://github.com/priyankageetha2007-debug/natural-guardian-agent.git
   cd natural-guardian-agent
2. Run the agent:
This project uses `uv` for dependency management. Execute the following command to run the agent:

```bash
uv run python app/agent.py
