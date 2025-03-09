import math;

def calculateDeterminants(matrix):
    row = len(matrix)

    if row == 1:
        return {"solution": [f"เมทริกซ์ 1x1 มีค่าดีเทอร์มิแนนต์เท่ากับสมาชิกตัวเดียวของมัน คือ {matrix[0][0]}"]}

    if row == 2:
        solution = ['เมทริกซ์ขนาด 2x2 สามารถใช้สูตรได้ โดย']
        determinant = [0, 0]

        for i in range(row):
            value = [0, 0]
            for j in range(row):
                value[j] = matrix[j][(i + j) % row]
                solution.append(f"นำสมาชิกเมทริกซ์แถวที่ {j + 1} หลักที่ {((i + j) % row) + 1} จะได้ {matrix[j][(i + j) % row]}")
            solution.append(f"นำสมาชิกทั้ง 2 มาคูณกัน จะเป็น ({value[0]} x {value[1]}) จะได้ {math.prod(value)}")
            determinant[i] = math.prod(value)
        solution.append(f"นำผลคูณทั้ง 2 มาลบกัน จะเป็น ({determinant[0]} - {determinant[1]}) จะได้ {determinant[0] - determinant[1]} ซึ่งเป็นค่าดีเทอร์มิแนนต์")

        return {"solution": solution}

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

        return {"result": [[sum(determinant)]], "solution": [f"เมทริกซ์ {row}x{row} ไม่สามารถใช้สูตรทั่วไปได้", "หาดีเทอร์มิแนนต์เมทริกซ์นี้ด้วยวิธีการกระจายตามหลัก โดย", *determinants_solution]}

def calculateMinor(matrix, i=0, j=0):
    minor_matrix = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
    determinants = calculateDeterminants(minor_matrix)

    return {"result": determinants["result"], "solution": [f"หาไมเนอร์ แถวที่ {i + 1} หลักที่ {j + 1} โดยการตัดแถวที่ {i + 1} และ ตัดหลักที่ {j + 1} ออกไป", f"จะได้เมทริกซ์:\n     " + "\n     ".join(str(row) for row in minor_matrix), f"เมทริกซ์ที่เหลือขนาด ({len(minor_matrix)}x{len(minor_matrix[0])}) จะเป็นเมทริกซ์ใหม่ที่ถูกนำไปหาดีเทอร์มิแนนต์", *determinants["solution"], f"จะได้ {determinants['result'][0][0]} ซึ่งเป็นค่าไมเนอร์แถวที่ {i + 1} หลักที่ {j + 1}"]}

def calculateCofactor(matrix, i=0, j=0):
    minor_result = calculateMinor(matrix, i, j)
    cofactor = ((i + j) % 2 == 0 and 1) or -1

    return {"result": [[cofactor * minor_result["result"][0][0]]], "solution": [f"หาโคแฟกเตอร์ แถวที่ {i + 1} หลักที่ {j + 1} จะต้องหาไมเนอร์ แถวที่ {i + 1} หลักที่ {j + 1} ก่อน", *minor_result["solution"], f"หาค่าโคแฟกเตอร์โดยการนำไมเนอร์ที่ได้มาคูณกับ ({cofactor}) จะได้ {cofactor * minor_result['result'][0][0]}"]}

##################################################################################################################################################################################

# matrix = [
#     [6]
# ]

# matrix = [
#     [3, 7], 
#     [1, 7]
# ]

# matrix = [
#     [10, 2, 10], 
#     [7, 6, 4], 
#     [5, 3, 1]
# ]
# 28 วิธี

matrix = [
    [8, 7, 10, 3], 
    [7, 10, 1, 9], 
    [6, 4, 8, 9], 
    [6, 6, 8, 5]
]
# 140+ วิธี

# matrix = [
#     [8, 5, 2, 4, 4],
#     [7, 4, 10, 3, 7], 
#     [2, 2, 3, 6, 3], 
#     [9, 4, 2, 4, 5], 
#     [7, 6, 9, 10, 9]
# ]   
# 750+ วิธี



#ไม่แนะนำสำหรับวิธีการใช้ recursive function    ----------------------------------------------------------------------------

# matrix = [
#     [8, 5, 2, 4, 4, 6], 
#     [7, 4, 10, 3, 7, 5], 
#     [2, 2, 3, 6, 3, 8], 
#     [9, 4, 2, 4, 5, 7], 
#     [7, 6, 9, 10, 9, 4], 
#     [5, 3, 7, 6, 8, 9]
# ]
# 4,500+ วิธี

# matrix = [
#     [8, 5, 2, 4, 4, 6, 9], 
#     [7, 4, 10, 3, 7, 5, 2], 
#     [2, 2, 3, 6, 3, 8, 7], 
#     [9, 4, 2, 4, 5, 7, 6], 
#     [7, 6, 9, 10, 9, 4, 8], 
#     [5, 3, 7, 6, 8, 9, 5], 
#     [4, 9, 6, 7, 3, 2, 8]
# ] 
# 31,000+ วิธี

# matrix = [
#     [8, 5, 2, 4, 4, 6, 9, 7],
#     [7, 4, 10, 3, 7, 5, 2, 6],
#     [2, 2, 3, 6, 3, 8, 7, 5],
#     [9, 4, 2, 4, 5, 7, 6, 8],
#     [7, 6, 9, 10, 9, 4, 8, 3],
#     [5, 3, 7, 6, 8, 9, 5, 2],
#     [4, 9, 6, 7, 3, 2, 8, 9],
#     [6, 3, 8, 5, 7, 9, 6, 4]
# ] 
# 256,000+ วิธี

result = calculateDeterminants(matrix)
print("------------------------------------------------------------------------------------------------------------------------------")
for index, line in enumerate(result["solution"]):
    print(f"{index + 1}. {line}")
print("------------------------------------------------------------------------------------------------------------------------------")
##################################################################################################################################################################################