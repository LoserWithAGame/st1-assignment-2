# This is the Human Written Prototype, Stage_1_Lab_Student_Handout.docx, Part B - Build a Human-Written Prototype: AI OFF
#task 1
# Create and run a simple Python file with basic input,output statements

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. John Doe'
appointment2_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")


#task1enhanced
# Use lists, dictionaries and functions to enhance the Python file

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. John Doe', '2024-07-20 10:00 AM')
display_appointments()


# ^ Now, run  both programs , and identify at least five limitations.
# In these programs, both of them do not allow the user to input any appointments, as the appointments are booked in through the program. With input functions this could be fixed. 
# Task 1 is quite bulky, there is no list to store the data in, and requires all variables to be declared separately, which is unnecessary and will waste time when accessing the appointments in the future.
# Task 1 Enhanced only checks if the Patient’s name is entered, not the practitioner’s name or the time of the appointment. This will cause issues in the records in future appointment bookings, as it can cause double booking times and practitioners without proper documentation.
# Task 1 prints each variable and appointment separately, partially due to the lack of a list, however with proper formatting of the print function the variables can all be printed with a single print statement inside a for loop. This would save time in typing out each print statement and reduce the number of errors that could occur with a misspelled variable.
# There is no documentation in Task 1 Enhanced, whilst the program is better, there are no comments to provide context. Maybe comments are not needed because of the helpful names of the variables, but comments would help explain the code better.