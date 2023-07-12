numbers_digits = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', 
    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', 
    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50'
]

numbers_names = [
    'agenge', 'aeng', 'somok', 'anguan', 'mut', 'lo', 'tisap', 'sisit', 'sogol', 'tamana',
    'tamanagenge', 'tamanakoeng', 'tamanaksomok', 'tamanakangwan', 'tamanagmut', 'tamanakalo', 'tamanaktisab', 'tamanagsisit', 'tamanaksogol', 'tiptem',
    'tiptemakagenge', 'tiptemakaeng', 'tiptemakasomok', 'tiptemakanguan', 'tiptemakamut', 'tiptemakalo', 'tiptemakatisap', 'tiptemakasisit', 'tiptemakasogol', 'sosom',
    'sosomakagenge', 'sosomakaeng', 'sosomakasomok', 'sosomakanguan', 'sosomakamut', 'sosomakalo', 'sosomakatisap', 'sosomakasisit', 'sosomakasogol', 'artam',
    'artamakagenge', 'artamakaeng', 'artamakasomok', 'artamakanguan', 'artamakamut', 'artamakalo', 'artamakatisap', 'artamakasisit', 'artamakasogol', 'konom'
]

element = input("Enter an element: ").lower()

if element in numbers_names:
    index = numbers_names.index(element)
    corresponding_element = numbers_digits[index]
    print("Corresponding element as a number:", corresponding_element)
elif element.isdigit() and int(element) in range(1, 51):
    index = int(element) - 1
    corresponding_element = numbers_names[index]
    print("Corresponding name for the number :", corresponding_element)
else:
    print("Element not found in either list.")
