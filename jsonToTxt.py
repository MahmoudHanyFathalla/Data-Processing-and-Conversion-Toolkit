import json

# Load JSON data from a file
with open('C:\\Users\\hp\\Downloads\\ExtractingData\\gov data\\json\العيادات الخارجيه.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def create_paragraph_for_clinic(clinic_name, services):
    paragraph = f"فيما يلي الخدمات المتوفرة في {clinic_name}:\n"
    for service in services:
        service_name = service["اسم الخدمة"]
        total_cost = service["اجمالي السعر"]
        contribution_member_family = service["المساهمة للعضو وأسرته"]
        contribution_parents = service["المساهمة للوالدين"]

        # Detailed explanation for each service
        paragraph += (f"الخدمة: {service_name}.\n"
                      f"السعر الإجمالي للخدمة هو {total_cost} جنيه. "
                      f"مساهمة العضو وأسرته تقدر بـ {contribution_member_family} جنيه، "
                      f"أما مساهمة الوالدين فهي {contribution_parents} جنيه.\n"
                      f"هذه الخدمة مقدمة من {clinic_name} وتعتبر جزءًا من "
                      f"الخدمات الصحية الضرورية لضمان الرعاية الصحية الشاملة.\n\n")
    
    # Add separator after each clinic
    paragraph += "------------------------------------------------------------------------------------------\n\n"
    return paragraph

# Create paragraphs for each clinic
paragraphs = []
for clinic, services in data.items():
    paragraphs.append(create_paragraph_for_clinic(clinic, services))

# Combine all paragraphs into one text
final_text = "\n".join(paragraphs)

# Output the generated paragraphs
print(final_text)

# Optionally, save the output to a file
with open('C:\\Users\\hp\\Downloads\\ExtractingData\\gov data\\txt\العيادات الخارجيه.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(final_text)
