# The following is my comparison based on the questions:
Question	                    Human version	AI version
Easy to understand?	            Yes	            Yes
Runs successfully?	            Yes	            Yes
Uses only required features?	Yes	            Yes
Adds assumptions?	            Yes	            Yes
Handles errors?	                Yes	            Yes
Could I explain it?	            Yes	            Yes

# The following is my personal comparison:
The Human-Written program has multiple errors, including lack of comments, not checking for empty practioners names and appointment times. The Human-Written program does not have a menu, comparatively, CoPilot's program had a built-in menu, which makes it easier to use without programming knowledge. CoPilot's also gathers the necessary information through user inputs, which is different to the Human-Written program which has them preset in the code. Overall, CoPilot's program went further into detail than the Human-Written program, and accounted for more errors that could occur.

# Verifying Behaviour:
Normal Appointment prints in both Human-Written and CoPilot’s programs.
Blank Patient name provides a ValueError in the Human-Written program; however CoPilot has created it’s own errors, not specifying a type. CoPilot’s program prints “Error: Patient name cannot be empty.”.
Neither the Human-Written program nor the CoPilot-Written program stop the double-booking of Practitioners and Times.
If the Patient Name or Appointment Time are set to the string “None” then that will be logged as the variable, as neither the Human-Written program nor the CoPilot-Written program verify correct inputs. The only verification performed is for the null string (“”), which provides an error in it’s place.
