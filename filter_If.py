import re

def extract_conditions(file_path, define_condition):
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Flags for state tracking
    is_in_function = False
    brace_count = 0
    is_in_condition = False
    current_condition = None

    extracted_code = []
    function_code = []
    macro_stack = []

    for line in lines:
        stripped_line = line.strip()

        # Detect function start and end
        if stripped_line.startswith("int case4("):  # Replace with dynamic function detection if needed
            is_in_function = True

        if is_in_function:
            function_code.append(line)
            brace_count += line.count("{") - line.count("}")
            if brace_count == 0:
                is_in_function = False

        # Process macro conditions only inside the function
        if is_in_function:
            if stripped_line.startswith("#if (defined"):
                macro_stack.append(stripped_line)
                current_condition = stripped_line.split("(")[1].split(")")[0]
                is_in_condition = current_condition == define_condition
            elif stripped_line.startswith("#elif (defined"):
                current_condition = stripped_line.split("(")[1].split(")")[0]
                is_in_condition = current_condition == define_condition
            elif stripped_line.startswith("#endif"):
                if macro_stack:
                    macro_stack.pop()
                is_in_condition = len(macro_stack) == 0 or macro_stack[-1] == define_condition
            elif is_in_condition:
                extracted_code.append(line)

    return "".join(extracted_code)


if __name__ == "__main__":
    # Path to the file
    file_path = "main.c"
    define_conditions = ["CCL_2", "CCL_1"]  # Add more conditions as needed

    for condition in define_conditions:
        print(f"\nCode for {condition}:\n")
        result = extract_conditions(file_path, condition)
        print(result)
