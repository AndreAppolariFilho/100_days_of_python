def format_mail_string_with_name(text_string, name):
    return text_string.replace("[name]", name)


assert format_mail_string_with_name("Test [name]", "Lucas") == "Test Lucas"
assert format_mail_string_with_name("Test [wrong]", "Lucas") == "Test [wrong]"

with open("Input/Names/invited_names.txt") as file:
    list_of_names = [name.strip() for name in file.readlines()]

with open("Input/Letters/starting_letter.txt") as file:
    text = file.read()
for name in list_of_names:
    with open(f"Output/ReadyToSend/email_to_{name}", "w") as output_file:
        output_file.write(format_mail_string_with_name(
            text,
            name
        ))

