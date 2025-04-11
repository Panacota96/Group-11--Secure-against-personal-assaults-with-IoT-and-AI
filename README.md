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
o	PineTime Smartwatch
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
________________________________________









11. Project Budget (Cost Table in EUR)
Item	Quantity	Unit Cost (€)	Total Cost (€)	Notes
PineTime Smartwatch	1	32	32	Open-source, programmable
Twilio SMS Service (Trial or 5€ credit)	1	5	5	To send SMS alerts
Bluetooth USB Dongle (if needed)	1	8	8	Optional if laptop doesn’t support BLE
Miscellaneous (cables, adapters, etc.)	1	5	5	Basic hardware setup
Total Estimated Budget			50 EUR	Most economic solution for rapid prototyping
________________________________________
12. Python Development Guide – PineTime Safety Alert System
1.	Initial Setup:
o	Install firmware on PineTime (e.g., InfiniTime).
o	Ensure BLE connectivity between PineTime and PC.
2.	Python BLE Setup:
o	Use the bleak library to connect and read heart rate.
3.	Signal Analysis:
o	Use Python logic or machine learning to detect anomalies.
4.	Alert Trigger:
o	When heart rate anomaly is detected, use Twilio API to send an SMS.
o	Play voice alert using play sound with pre-recorded message.
5.	Division of Labor:
Member	Task
Electronic Engineer	Configure smartwatch and BLE connections.
Cybersecurity Engineer	Secure communication, signal analysis
IoT & Industrial Engineer 	Python integration, alerts, and system logic

 



Features and Specifications
	
Display	Square 1.3-inch 240×240 IPS capacitive touch display
SoC	Low-power Nordic Semiconductor nRF52832
64 MHz + Floating Point
Software	Any open-source operating systems built on top of numerous RTOSes
Body	Dimensions: 37.5mm x 40mm x 11mm
Weight: 38 grams
Made with Zinc alloy and plastic
Dustproof and water-resistant up to 1m (rated at IP67)
Health Tracking	Step Counting (with Accelerometer)
Heart rate detection
Notification features	Notification access
Wrist vibration
Quick glance via lift-to-wake.
Connectivity	Bluetooth 5 and Bluetooth Low Energy
Compatible with almost any device
Over-the-air update
Storage	4 MB of User Storage 0.5 MB of OS Storage
Battery	All-week 180 mAh battery
2-pin USB charging dock


