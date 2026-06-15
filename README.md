# 📊 DataAgent: End-to-End AutoML & AI Analyst

DataAgent is an interactive, automated Data Science platform that combines a robust data-cleaning pipeline, AutoML capabilities, and an AI-powered conversational analyst. It allows users to upload raw tabular datasets (CSV/Excel), perform instant quality checks, automatically train optimal machine learning models, and interact with their data in real-time through a chat interface.

---

## 🚀 Key Features

### 🧹 1. Automated Data Cleaning Pipeline
* **Smart Imputation:** Automatically detects numeric vs. categorical columns. Fills numeric missing values using the **median** and categorical missing values using the **mode**.
* **Duplicate Resolution:** Automatically identifies and drops duplicate rows.
* **Outlier Filtering:** Detects and removes statistical outliers in numerical columns using **IQR limits** (Interquartile Range, Q1/Q3 ± 1.5 × IQR).

### 🔍 2. Interactive Data Quality Inspection
* Runs a diagnostics check on upload:
  * Flags missing value counts.
  * Tallies duplicates.
  * Detects constant/redundant features (single unique value) that do not add predictive value.
  * Tallies outlier distributions.

### 🤖 3. AutoML Model Training & Prediction
* **Auto-Task Classification:** Automatically classifies the ML task into **Regression** or **Classification** based on the target column cardinality and data type.
* **FLAML AutoML Engine:** Harnesses Microsoft's **FLAML** library to train multiple models and perform hyperparameter tuning within a 30-second budget.
* **Prediction Endpoint:** Exposes a `/predict` endpoint that allows loading the trained model `.pkl` file and serving live predictions for new input payloads.

### 💬 4. AI Data Analyst Chatbot ("Your Analyst")
* **Conversational Q&A:** Chat naturally with your dataset using an LLM model (`llama-3.1-8b-instant` via Groq) integrated with LangChain and LangGraph.
* **Interactive Tool Executions:** Ask the chatbot to clean data, train models, or check statistics, and it will execute the appropriate Python tool in the background.
* **Thread Memory:** Uses LangGraph checkpointers to maintain thread context, allowing you to ask follow-up questions referencing previous answers.
* **Real-time Streaming:** Token streaming via FastAPI's `StreamingResponse` for a lag-free conversational experience.

### 📊 5. Automated Reports & Visualizations
* **Visual Recommendations:** Recommends appropriate chart mappings (heatmaps, histograms, scatter plots) based on column datatypes.
* **PDF/Markdown Reports:** Automatically generates and saves a downloadable markdown report summarizing the dataset's characteristics, quality recommendations, cleaning actions, and trained model metrics.

### 🔒 6. Privacy & Session Management
* **Active Session Cleanup:** Assigns unique UUIDs to uploads. When clearing a session, the app cleans up all files associated with that session (uploads, clean datasets, models, and reports) to keep disk space optimized.
* **Frontend State Persistence:** Automatically preserves active upload states, model details, and selected columns in the browser's `localStorage` to prevent data loss on page refreshes.

---

## 🛠️ Technology Stack

### Backend
* **FastAPI:** High-performance web framework for APIs and file downloads.
* **LangChain & LangGraph:** Orchestrates the agent workflow, tool bindings, and state memory.
* **FLAML:** Fast and Lightweight AutoML library by Microsoft.
* **Scikit-Learn & Pandas:** Used for data preprocessing, splitting, and tabular operations.
* **ChatGroq (Llama-3.1-8B):** Serves as the cognitive engine for reasoning and conversational replies.

### Frontend
* **React (Vite):** Modern, fast single-page frontend.
* **Tailwind CSS:** Responsive utility-first styling.
* **Axios:** Handles asynchronous HTTP client communication.

---

## 💻 Getting Started

### 1. Setup Backend
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and install dependencies (using `uv` or `pip`):
   ```bash
   uv venv
   .venv/Scripts/activate
   uv pip install -r requirements.txt
   ```
3. Create a `.env` file in the `backend` folder and add your Groq API Key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
4. Start the server:
   ```bash
   uv run uvicorn main:app --reload
   ```

### 2. Setup Frontend
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install npm dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
