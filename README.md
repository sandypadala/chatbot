# GenAI Chat App

A simple chat app with a FastAPI backend and a static frontend. It is prepared for deployment on Vercel.

## Features
- Chat UI served from the frontend
- Serverless API endpoints for chat and health checks
- OpenAI-powered replies via LangChain

## Local development
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI key:
   ```bash
   set OPENAI_API_KEY=your_key_here
   ```
3. Start the local API:
   ```bash
   uvicorn middleware.api:app --reload --port 8000
   ```
4. Open the frontend from the public folder or serve it with any static server.

## Vercel deployment
1. Push this project to GitHub.
2. Create a new Vercel project and import the repository.
3. In Project Settings > Environment Variables, add:
   - `OPENAI_API_KEY`
4. Deploy the project.

## API endpoints
- `GET /api/health`
- `POST /api/chat`

Example request:
```bash
curl -X POST https://your-vercel-app.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'
```
