# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey @ilinkmpi!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/ilinkmpi/github-copilot/issues/1)

---

## Features
- View all available extracurricular activities
- See activity details and current participants
- Sign up for an activity (one registration per student per activity)
- Unregister from an activity
- Modern, responsive web UI

## Project Structure
- `src/app.py`: FastAPI backend API
- `src/static/`: Frontend files (HTML, JS, CSS)
- `tests/test_app.py`: Automated API tests
- `requirements.txt`: Python dependencies

## Running the App
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Start the server:
   ```sh
   uvicorn src.app:app --reload
   ```
3. Open your browser at [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)

## Running Tests
1. Install test dependencies:
   ```sh
   pip install pytest
   ```
2. Run tests:
   ```sh
   pytest tests/
   ```

## API Endpoints
- `GET /activities`: List all activities
- `POST /activities/{activity_name}/signup?email=...`: Sign up a student
- `POST /activities/{activity_name}/unregister?email=...`: Unregister a student

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

