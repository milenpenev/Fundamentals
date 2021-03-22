number_of_atoms = int(input())
electrons = []
shell_number = 1

while number_of_atoms > 0:
    max_electrons_in_current_shell = 2 * shell_number ** 2
    if max_electrons_in_current_shell > number_of_atoms:
        electrons.append(number_of_atoms)
    else:
        electrons.append(max_electrons_in_current_shell)
    number_of_atoms -= max_electrons_in_current_shell
    shell_number += 1
print(electrons)