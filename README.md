# Group-11--Secure-against-personal-assaults-with-IoT-and-AI
Group 11- Secure against personal assaults with IoT and AI

Smart Bracelet Project Plan: Child Safety Monitoring (V-Model Methodology)
________________________________________
1. Project Purpose and Objectives
General Objective: To develop a smart bracelet that monitors children’s vital signs, detects falls, and activates an emergency response system to increase safety during their commute from home to school, following the V-model methodology.
Specific Objectives:
•	Measure blood pressure and heart rate to detect physiological changes that may indicate stress or danger.
•	Detects falls using motion sensors.
•	Trigger an adult voice alert when emergency indicators are detected.
•	Ensure secure wireless communication for emergency alerting.
•	Validate the device through iterative testing and user simulations.
________________________________________
2. Project Scope
•	Included: Design and prototype a wearable device for children aged 12 to 18 that includes sensors for vital signs, fall detection, basic Bluetooth connectivity, and a voice-based emergency response system.
•	Excluded: Full mobile app development, production manufacturing, and medical certifications.
________________________________________
3. Work Breakdown Structure (WBS)
1.	Determine Project Goals and Objectives
o	Define safety monitoring needs during the school commute.
2.	Establish Project Scope
o	Identify deliverables, constraints, and exclusions.
3.	Work Breakdown
o	Researched and selected components
o	Electronics and enclosure design
o	Assembly and programming
o	Testing and documentation
4.	Set Deadlines
o	Weekly planning aligned with the V-model steps.
5.	Identify and Plan Resources
o	Human: Divide tasks among engineers based on expertise (electronic, cybersecurity, IoT/industrial)
o	Technical: List and acquire sensors, microcontrollers, 3D printing materials
6.	Estimate Time Budget
o	Allocate estimated hours per phase and member
7.	Risk and Limitations Assessment
o	Technical, logistical, and scheduling risks
o	Mitigation strategies
8.	Organize Communication
o	Define communication channels and meeting frequency
9.	Create Quality Control and Assurance Plans
o	Defined testing strategy and code review procedures
________________________________________
4. V-Model Methodology Application
•	Requirement Analysis: Define the safety needs of children (done in Objectives and Scope)
•	System Design: Selection of sensors, microcontroller, and communication protocols
•	Architecture Design: Layout of system components (bracelet structure, internal wiring, microcontroller interfacing)
•	Module Design: Software and firmware planning (vital sign processing, alert system)
•	Implementation: Code development, prototype assembly
•	Unit Testing: Individual component testing (sensor readings, audio playback)
•	Integration Testing: Combined system testing with all modules
•	System Testing: Full device validation in simulated environments
•	User Acceptance Testing (UAT): Trial runs with real users or test subjects
________________________________________
5. Timeline / Gantt Chart
Week	Tasks
Week 1	Define objectives, finalise scope, and assign roles.
Week 2	Research components, design circuits and 3D housing
Week 3	Assemble prototype, begin programming, test sensors.
Week 4	Finalise programming, conduct system testing
Week 5	Document results, perform user testing, prepare demo.
________________________________________
6. Resources Planning
•	Human Resources:
o	Electronic Engineer with Cybersecurity focus
o	Cybersecurity Engineer
o	IoT & Industrial Engineer (you)
•	Technical Resources:
o	PC with Bluetooth
o	Twilio account (SMS service)
o	Audio recordings of family voice
________________________________________
7. Time Budget Estimated total project duration: 5 weeks, 10-15 hours/week/member
•	Research: 10 hours
•	Design: 15 hours
•	Prototyping: 20 hours
•	Testing: 15 hours
•	Documentation: 10 hours
________________________________________
8. Risk Assessment
Risk assessment is essential to identify potential problems early in the project and prepare appropriate mitigation strategies. It helps ensure the successful completion of the project by minimizing disruptions and avoiding delays.
•	Technical Risk: Signal reading accuracy, BLE disconnections
•	Logistical Risk: Compatibility issues with software libraries
•	Mitigation: Early hardware testing, backup smartwatch available, dataset simulation
________________________________________
9. Communication Plan
•	Weekly video calls Teams
•	WhatsApp group for quick updates
•	Shared Google Drive for documents and designs
•	GitHub for version control of code
________________________________________
10. Quality Assurance Plan
•	Daily testing of BLE data and alert logic
•	Peer review of signal processing and alert trigger code
•	Realistic test scenarios using sample datasets
•	Alerts simulation: sound and SMS under test conditions
•	Video giving the set-up of the work we are going to do

11. Project Budget (Cost Table in EUR)
Item	Quantity	Unit Cost (€)	Total Cost (€)	Notes
Miscellaneous (cables, adapters, etc.)	1	5	5	Basic hardware setup
Total Estimated Budget			50 EUR	Most economic solution for rapid prototyping
________________________________________

## Required Python Libraries

To run the modules in this project, you need the following Python libraries:

- numpy
- pandas
- scikit-learn
- opencv-python
- tensorflow
- keras
- tf-keras
- flask
- requests
- sounddevice
- scipy
- pygame
- python-dotenv
- twilio
- speechrecognition
- pyannote.audio
- sentence-transformers
- librosa
- torch
- torchaudio
- transformers

Install all dependencies at once with:

```sh
pip install -r src/requirements.txt
```

## Module Summaries

### Audio Sample Module (`src/audioSample.py`)
Enables audio recording from the default microphone and saves the captured audio as a WAV file. Uses the `sounddevice` library for audio capture and `scipy` for saving the file. Useful for collecting audio samples for further analysis, such as speaker verification or speech recognition.

### Audio Alert Module (`src/audioAlert.py`)
Plays pre-recorded audio alerts (such as emergency messages) using the `pygame` library. Essential for delivering audible alerts in emergency situations as part of the safety monitoring system.

### Send Message Module (`src/sendMessage.py`)
Sends notifications via SMS (using Twilio) and email (using Gmail SMTP). Loads configuration from a `.env` file, sets up logging, and defines utility functions for sending messages. Designed for integration into alerting or monitoring systems where timely notifications are critical.

### Voice Recognition Module (`src/voiceRecognition.py`)
Provides advanced voice analysis capabilities using pre-trained models from torchaudio and Hugging Face Transformers. Features include speaker verification, speech quality assessment, speech-to-text transcription, and safe word detection. Essential for robust voice authentication, emergency keyword detection, and audio quality monitoring.

### Threat Detection Module (`src/threatDetection.py`)
Detects threat-related content in text using sentence embeddings and semantic similarity. Leverages the `sentence-transformers` library to encode both input text and a set of predefined threat phrases. Useful for automated detection of potentially dangerous or threatening language, such as safety monitoring, moderation, or alert systems.