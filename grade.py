import os

def calculate_grade_percentage(input_folder, output_file):
    with open(output_file, 'w') as output:
        for filename in os.listdir(input_folder):
            if filename.endswith("_registered.txt"):
                input_file = os.path.join(input_folder, filename)
               
                module_name, promo = filename.split('_registered.txt')[0].split('][')
                module_name = module_name[1:]  
                promo = promo[:-1]  

                grade_occurrences = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'Echec': 0}

                with open(input_file, 'r') as file:
                    next(file)  
                    for line in file:
                        grade = line.strip()
                        if grade in grade_occurrences:
                            grade_occurrences[grade] += 1

               
                total_grades = sum(grade_occurrences.values())

                output.write(f"Name Module : {module_name}\n")
                output.write(f"Promo : {promo}\n\n")
                
               
                for grade, occurrences in grade_occurrences.items():
                    percentage = (occurrences / total_grades) * 100
                    output.write(f"Grade {grade} : {percentage:.2f}%\n")
                output.write('\n' + '-'*26 + '\n\n')

input_folder = ""
output_file = ""

calculate_grade_percentage(input_folder, output_file)
