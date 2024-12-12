# Python Virtual Assistant Project

## Overview
This project is a Python-based virtual assistant that provides voice-based interaction and automates tasks such as searching Wikipedia, opening websites, sending emails, and more. The assistant listens to user commands, processes them, and performs the requested actions seamlessly.

---

## Features
1. **Voice Interaction**: 
   - Uses text-to-speech (`pyttsx3`) for verbal responses.
   - Employs speech-to-text (`speech_recognition`) for processing user commands.

2. **Task Automation**:
   - Opens commonly used websites such as YouTube, Google, and ChatGPT.
   - Fetches summaries from Wikipedia for specified topics.
   - Reports the current time.
   - Opens local applications like Visual Studio Code.

3. **Email Functionality**:
   - Automates sending emails using the SMTP protocol with `smtplib`.

4. **Time-Based Greetings**:
   - Responds with appropriate greetings based on the time of day.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `pyttsx3`: Text-to-speech synthesis.
  - `speech_recognition`: For converting speech to text.
  - `pyaudio`: Captures audio input through the microphone.
  - `datetime`: Handles time-based operations.
  - `wikipedia`: Fetches topic summaries from Wikipedia.
  - `webbrowser`: Automates opening web pages.
  - `smtplib`: Sends emails programmatically.
  - `os`: For system-level interactions such as opening applications.

---

## How It Works
1. **Initialization**:
   - The assistant initializes with a greeting based on the current time.
2. **Listening for Commands**:
   - Captures user input through the microphone and processes it with `speech_recognition`.
3. **Executing Tasks**:
   - Based on the user's command, the assistant performs actions like searching Wikipedia, sending emails, opening websites, or reporting the time.

---

## Setup and Installation
### Prerequisites:
- Python 3.x installed on your system.
- Install required Python libraries:
  ```bash
  pip install pyttsx3 SpeechRecognition pyaudio wikipedia
  ```

### Steps to Run:
1. Clone or download the project files.
2. Replace placeholders for email and password in the `sendEmail` function:
   ```python
   server.login('yourgmail@gmail.com', 'yourpassword')
   ```
3. Run the script:
   ```bash
   python assistant.py
   ```
4. Speak commands into the microphone as prompted.

---

## Example Commands
- "Search [topic] on Wikipedia."
- "Open YouTube."
- "Open Google."
- "What is the time?"
- "Send an email."

---

## Future Enhancements
- Add support for playing music from a local directory.
- Integrate with APIs for more advanced features (e.g., weather, news updates).
- Implement enhanced error handling and fallback responses.

---

## Disclaimer
- Ensure microphone and speaker are properly configured on your system.
- Use secure email credentials and avoid hardcoding sensitive information.
