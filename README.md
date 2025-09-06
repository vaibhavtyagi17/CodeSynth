# 🚀 CodeSynth - AI Code Generator

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6+-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Transform your ideas into code with AI!** CodeSynth generates complete software projects from natural language descriptions using a multi-agent AI system.

## ✨ Features

- 🤖 **AI Code Generation**: Uses Groq's LLM for intelligent code creation
- 🏗️ **Multi-Agent System**: Planner → Architect → Coder workflow
- 🌐 **Web Interface**: Beautiful, responsive UI with real-time progress
- 📁 **File Management**: Automatically creates and organizes project files
- 🚀 **Easy Deployment**: Ready for Vercel deployment
- ⚡ **Fast**: Generate complete projects in 30-60 seconds

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.11+
- **AI**: LangGraph, LangChain, Groq LLM
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Vercel

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Groq API key ([Get one here](https://console.groq.com))

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/vaibhavtyagi17/codesynth.git
   cd codesynth
   ```

2. **Set up virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8000`

### 🌐 Vercel Deployment

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit - CodeSynth AI platform"
   git push origin main
   ```

2. **Deploy to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Add environment variable: `GROQ_API_KEY`
   - Deploy! 🎉

## 💡 Usage Examples

- "Create a modern calculator with HTML, CSS, and JavaScript"
- "Build a todo app with local storage"
- "Make a weather dashboard with API integration"
- "Design a portfolio website with animations"

## 📁 Project Structure

```
codesynth/
├── agent/                 # AI Agent System
│   ├── graph.py          # LangGraph workflow
│   ├── prompts.py        # AI prompts
│   ├── states.py         # Data models
│   └── tools.py          # File operations
├── templates/            # Web Interface
│   └── index.html        # Main UI
├── generated_project/    # AI-generated code output
├── app.py               # FastAPI application
├── main.py              # Entry point
└── requirements.txt     # Dependencies
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main web interface |
| `POST` | `/api/generate` | Generate code from prompt |
| `GET` | `/api/health` | Health check |

## 🎯 How It Works

1. **📝 Planning**: AI analyzes your prompt and creates a project plan
2. **🏗️ Architecture**: Breaks down the plan into implementation tasks
3. **💻 Coding**: Multi-agent system generates code files
4. **📁 Output**: Complete project files saved in `generated_project/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/vaibhavtyagi17/codesynth/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/vaibhavtyagi17/codesynth/discussions)
- 📧 **Email**: vaibhav707tyagi@gmail.com

---

<div align="center">

**Built with ❤️ by [Vaibhav Tyagi](https://github.com/vaibhavtyagi17)**

*Transform ideas into code with the power of AI*

</div>