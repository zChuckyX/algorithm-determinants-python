import math;

def check_zero_row(matrix):
    return any(all(value == 0 for value in row) for row in matrix)

def check_zero_column(matrix):
    return any(all(matrix[row][col] == 0 for row in range(len(matrix))) for col in range(len(matrix[0])))

def check_upper_triangle(matrix):
    return all(all(matrix[i][j] == 0 for j in range(i)) for i in range(len(matrix)))

def check_lower_triangle(matrix):
    return all(all(matrix[i][j] == 0 for j in range(i + 1, len(matrix[0]))) for i in range(len(matrix)))

def calculate_determinants_from_diagonal(matrix, message):
    matrix_result = [matrix[i][i] for i in range(len(matrix))]
    matrix_solution = [f"นำสมาชิกแถวที่ {i+1} หลักที่ {i+1} จะได้ {val}" for i, val in enumerate(matrix_result)]

    if 0 in matrix_result:
        return {"result": [[0]], "solution": ["เนื่องจากมีสมาชิกในตำแหน่งใดตำแหน่งนึงเป็น 0 ในแนวทแยงมุม ค่าดีเทอร์มิแนนต์จึงเป็น 0"]}

    summary = 1
    for value in matrix_result:
        summary *= value
    matrix_solution.append(f"นำมาคูณกันจะเป็น ({' x '.join(map(str, matrix_result))}) จะได้ {summary} ซึ่งเป็นค่าดีเทอร์มิแนนต์")

    return {"result": [[summary]], "solution": [message, "ค่าดีเทอร์มิแนนต์ที่ได้จึงเป็นการคูณกันในแนวทแยงมุม", *matrix_solution]}

def calculateDeterminants(matrix):
    row = len(matrix)

    if check_zero_row(matrix):
        return {"result": [[0]], "solution": ["เนื่องจากมีแถวใดแถวนึงที่เป็นศูนย์ทั้งหมด ซึ่งค่าดีเทอร์มิแนนต์จะเท่ากับ 0"]}

    if check_zero_column(matrix):
        return {"result": [[0]], "solution": ["เนื่องจากมีหลักใดหลักนึงที่เป็นศูนย์ทั้งหมด ซึ่งค่าดีเทอร์มิแนนต์จะเท่ากับ 0"]}

    if check_upper_triangle(matrix) and row != 1:
        return calculate_determinants_from_diagonal(matrix, "เนื่องจากเมทริกซ์นี้เป็นเมทริกซ์สามเหลี่ยมบน")

    if check_lower_triangle(matrix) and row != 1:
        return calculate_determinants_from_diagonal(matrix, "เนื่องจากเมทริกซ์นี้เป็นเมทริกซ์สามเหลี่ยมล่าง")

    if row == 1:
        return {"solution": [f"เมทริกซ์ 1x1 มีค่าดีเทอร์มิแนนต์เท่ากับสมาชิกตัวเดียวของมัน คือ {matrix[0][0]}"]}

    if row == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return {"solution": [
            "เมทริกซ์ 2x2 สามารถใช้สูตรทั่วไปได้",
            f"นำสมาชิกแถวที่ 1 หลักที่ 1 จะได้ {matrix[0][0]}",
            f"นำสมาชิกแถวที่ 2 หลักที่ 2 จะได้ {matrix[1][1]}",
            f"นำคำตอบทั้ง 2 มาคูณกันจะเป็น ({matrix[0][0]} x {matrix[1][1]}) จะได้ {matrix[0][0] * matrix[1][1]}",
            f"นำสมาชิกแถวที่ 1 หลักที่ 2 จะได้ {matrix[0][1]}",
            f"นำสมาชิกแถวที่ 2 หลักที่ 1 จะได้ {matrix[1][0]}",
            f"นำคำตอบทั้ง 2 มาคูณกันจะเป็น ({matrix[0][1]} x {matrix[1][0]}) จะได้ {matrix[0][1] * matrix[1][0]}",
            f"นำผลคูณที่ได้มาลบกันจะเป็น ({matrix[0][0] * matrix[1][1]} - {matrix[0][1] * matrix[1][0]}) จะได้ {determinant} ซึ่งเป็นค่าดีเทอร์มิแนนต์"
        ]}

    if row == 3:
        solution =['เมทริกซ์ขนาด 3x3 สามารถใช้กฏSarrusได้ โดย'];
        determinant1 = [0, 0, 0]
        determinant2 = [0, 0, 0]

        for i in range(row):
            value = [0, 0, 0]
            for j in range(row):
                value[j] = matrix[j][(i + j) % row]
                solution.append(f"นำสมาชิกเมทริกซ์แถวที่ {j + 1} หลักที่ {((i + j) % row) + 1} จะได้ {matrix[j][(i + j) % row]}")
            solution.append(f"นำสมาชิกทั้ง 3 มาคูณกัน จะเป็น ({value[0]} x {value[1]} x {value[2]}) จะได้ {math.prod(value)}")
            determinant1[i] = math.prod(value)

        solution.append(f"นำผลคูณทั้ง 3 มาบวกกัน จะเป็น ({determinant1[0]} + {determinant1[1]} + {determinant1[2]}) จะได้ {sum(determinant1)}")

        for i in range(row):
            value = [0, 0, 0]
            for j in range(row):
                value[j] = matrix[j][(i - j) % row]
                solution.append(f"นำสมาชิกเมทริกซ์แถวที่ {j + 1} หลักที่ {((i - j) % row) + 1} จะได้ {matrix[j][(i - j) % row]}")
            solution.append(f"นำสมาชิกทั้ง 3 มาคูณกัน จะเป็น ({value[0]} x {value[1]} x {value[2]}) จะได้ {math.prod(value)}")
            determinant2[i] = math.prod(value)

        solution.append(f"นำผลคูณทั้ง 3 มาบวกกัน จะเป็น ({determinant2[0]} + {determinant2[1]} + {determinant2[2]}) จะได้ {sum(determinant2)}")
        solution.append(f"จากนั้นนำผลรวมที่ได้ทั้ง 2 มาลบกัน จะเป็น ({sum(determinant1)} - {sum(determinant2)}) จะได้ {(sum(determinant1)) - (sum(determinant2))} ซึ่งเป็นค่าดีเทอร์มิแนนต์")
        
        return {"result": [[(sum(determinant1)) - (sum(determinant2))]], "solution": solution}

    if (row > 3):
        determinant = []
        determinants_solution = []

        for j in range(row):
            cofactor = calculateCofactor(matrix, 0, j)
            determinant.append(matrix[0][j] * cofactor["result"][0][0])
            determinants_solution.extend(cofactor["solution"])
            determinants_solution.append(f"นำค่าโคแฟกเตอร์มาคูณกับสมาชิกเมทริกซ์แถวที่ 1 หลักที่ {j + 1} จะเป็น ({cofactor['result'][0][0]} x {matrix[0][j]}) จะได้ {matrix[0][j] * cofactor['result'][0][0]}")

        string = f"เมื่อหาค่ากระจายตามแถวตามหลักเสร็จนำผลคูณที่ได้มาบวกกัน จะเป็น ({determinant[0]}"

        for i in range(1, len(determinant)):
            string += f" + {determinant[i]}"

        string += f") จะได้ {sum(determinant)} ซึ่งเป็นค่าดีเทอร์มิแนนต์"
        determinants_solution.append(string)

        return [f"เมทริกซ์ {row}x{row} ไม่สามารถใช้สูตรทั่วไปได้", "หาดีเทอร์มิแนนต์เมทริกซ์นี้ด้วยวิธีการกระจายตามหลัก โดย", *determinants_solution]

def calculateMinor(matrix, i=0, j=0):
    minor_matrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
    determinants = calculateDeterminants(minor_matrix)

    return {"result": determinants["result"], "solution": [f"หาไมเนอร์ แถวที่ {i + 1} หลักที่ {j + 1} โดยการตัดแถวที่ {i + 1} และ ตัดหลักที่ {j + 1} ออกไป", f"เมทริกซ์ที่เหลือขนาด ({len(minor_matrix)}x{len(minor_matrix[0])}) จะเป็นเมทริกซ์ใหม่ที่ถูกนำไปหาดีเทอร์มิแนนต์", *determinants["solution"], f"จะได้ {determinants['result'][0][0]} ซึ่งเป็นค่าไมเนอร์แถวที่ {i + 1} หลักที่ {j + 1}"]}

def calculateCofactor(matrix, i=0, j=0):
    minor_result = calculateMinor(matrix, i, j)
    cofactor = ((i + j) % 2 == 0 and 1) or -1
    
    return {"result": [[cofactor * minor_result["result"][0][0]]], "solution": [f"หาโคแฟกเตอร์ แถวที่ {i + 1} หลักที่ {j + 1} จะต้องหาไมเนอร์ แถวที่ {i + 1} หลักที่ {j + 1} ก่อน", *minor_result["solution"], f"หาค่าโคแฟกเตอร์โดยการนำไมเนอร์ที่ได้มาคูณกับ ({cofactor}) จะได้ {cofactor * minor_result['result'][0][0]}"]}


##################################################################################################################################################################################

matrix1 = [
    [6]
]

matrix2 = [
    [3, 7], 
    [1, 7]
]

matrix3 = [
    [10, 2, 10], 
    [7, 6, 4], 
    [5, 3, 1]
]

matrix4 = [
    [8, 7, 10, 3], 
    [7, 10, 1, 9], 
    [6, 4, 8, 9], 
    [6, 6, 8, 5]
]

matrix5 = [
    [8, 5, 2, 4, 4], 
    [7, 4, 10, 3, 7], 
    [2, 2, 3, 6, 3], 
    [9, 4, 2, 4, 5], 
    [7, 6, 9, 10, 9]
]

result = calculateDeterminants(matrix4)
print("------------------------------------------------------------------------------------------------------------------------------")
for index, line in enumerate(result["solution"]):
    print(f"{index + 1}. {line}")
print("------------------------------------------------------------------------------------------------------------------------------")
##################################################################################################################################################################################
