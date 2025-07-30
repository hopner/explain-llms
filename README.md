# Interactive LLM Mediation Website

An interactive website explaining how large language models (LLMs) work through scrollytelling and hands-on experimentation.

Built with:
- **Backend**: Django REST Framework serving Markdown content and AI model endpoints
- **Frontend**: Vue 3 + Vite + TypeScript with Scrollama for scroll-driven animations

## Project Structure
- **Backend**: `llm-backend/`
  - Contains Django app with REST API endpoints for model explanations and interactions.
- **Frontend**: `llm-frontend/`
  - Vue.js application with pages for model explanations and interactive AI model building.

## Getting Started
### Backend Setup
1. Navigate to the `llm-backend/` directory.
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```

### Frontend Setup
1. Navigate to the `llm-frontend/` directory.
2. Install dependencies:
    ```bash
    npm install
    ```
3. Start the development server:
    ```bash
    npm run dev
    ```
