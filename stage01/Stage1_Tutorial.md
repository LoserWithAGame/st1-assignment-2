Stage 1 Tutorial Activity
 - Why Software Engineering Still Matters
Stage 1 | Introducing Software Technology Case Study with Python and Guided AI use
Learning goals
•	Explain why software engineering is broader than coding.
•	Identify stakeholders in a simple software problem.
•	Recognise missing requirements.
•	Critically evaluate AI-generated feature suggestions.
•	Explain why AI output should not automatically be treated as correct.
Activity 1 - Think-Pair-Share (10 minutes)
If ChatGPT or Copilot can produce a 100-line Python application very quickly, what knowledge does a software engineer still need?
1. The ability to read and interpret code, as the AI could make mistakes which need correcting.
2. The ability to maintain and test the program, as the system could have faults that only show up further into the future.
3. To specify what the program must perform, as AI cannot write code without a prompt. The Software Engineer must understand the problem and know how the solution will work so they can generate a prompt for the AI.
Activity 2 - Is This Software Engineering? (10 minutes)
Scenario A: A student writes a 50-line Python calculator.
Scenario B: A team develops a payroll system used by 5,000 employees.
Scenario C: An AI assistant generates a simple appointment application from one prompt.
Scenario	Programming?	Software engineering?	Why?
A	Yes	Maybe	The student is writing code in Python to perform a given task (Of a calculator). This is programming because it’s writing a program. This might be software engineering depending on the context, as if the student is continuing to develop, maintain, and test the calculator then it is software engineering, otherwise it is not.
B	Yes	Yes	This scenario is a team of developers creating a payroll system to be used by 5,000 employees, which is why this is both programming and software engineering. This is programming because it uses code to create a solution. And this is software engineering because a system of that size would require constant maintenance, testing, and continued development past the initial creation.
C	No	Maybe	In this situation the Artificial Intelligence is generating the program, hence the user is not programming. However, this could potentially be software engineering, depending on if the person using the AI reads through the generated program and adjusts it whenever needed. Furthermore, this would only be software engineering if this wasn’t a one-off situation, and the program generated would be continually monitored and maintained.
Activity 3 - SmartCare Problem Analysis (20 minutes)
Client statement: SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The clinic wants new software to improve these processes.
Task 1 - Identify stakeholders
Stakeholder	What do they need?
Management	Simple software system to initially support the patient, practitioner, and appointment management. 
Organisation	Not a complex hospital information system, able to be manageable for a small clinic. This would be a simple program to assist the clinic in scheduling appointments.
SmartCare Clinic	The clinic has problems with:
-	Duplicate appointment bookings
-	Difficulty locating patient records
-	Inconsistent appointment status information
-	Limited visibility of practitioner availability
-	Manual cancellation process
-	Lack of reliable appointment history
-	Difficulty producing basic operational reports
	
Task 2 - Identify current problems
1. Appointment scheduling (Duplicate appointment bookings, inconsistent appointment status, limited visibility of practitioner availability) 
2. Records and history Management (Difficulty locating patient records, lack of reliable appointment history) 
3. Report Generating (Difficulty producing basic operational reports) 
4. Cancellation Process (Manual cancellation processes) 
Task 3 - Ask client questions
1. You have specified you do not want a large-scale hospital information system, what would the scope of the project be? As the Operational Report Generating and Records and History Management are different issues entirely to the appointment scheduling, which may make the simple software application seem more like a large-scale hospital information system.
2. Which issue is the main priority to generate a solution for? In other words, what problem should the project be focusing on first?
3. How many different patient records must be stored?
4. 
5. ______________________________________________________________
Activity 4 - Critique an AI Response (15 minutes)
An AI assistant suggests: appointment management; facial-recognition login; AI diagnosis recommendations; patient search; online payment; practitioner schedule view; insurance processing; automatic treatment-plan generation.
Suggestion	Client evidence?	In scope?	Decision
Appointment management	Client is having difficulty with appointment scheduling.	Yes	This will be included in the system.
Facial recognition login	None, the client has mentioned nothing about securing the system with facial recognition.	No	This will be excluded from the system.
AI diagnosis recommendations	None, the system is designed to manage appointments and patient history. There is no mention of assistance in diagnosis.	No	This will be excluded from the system.
Patient search	Client has been having difficulties with locating patient records, and limited reliable appointment history documentation.	Yes	This will be included in the system.
Online payment	None, there is no mention of difficulty with receiving payment.	No	This will be excluded from the system.
Practitioner schedule view	The client has been having difficulty with limited visibility of practitioner availability.	Yes	This will be included in the system.
Insurance processing	None, the client has not mentioned any difficulty with insurance processing.	No	This will be excluded from the system
Treatment-plan generation	None, the client has not mentioned any difficulty with generating a treatment plan.	No	This will be excluded from the system.
Exit question
Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.
Managing the system/Providing the initial information. The healthcare clinic deals with sensitive user information, which cannot be released to an Artificial Intelligence, hence why the Software Engineer would need to modify, test, and maintain the patient records section after any amount of information has been entered.
