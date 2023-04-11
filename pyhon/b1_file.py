try:
    with open('A.txt', 'r') as file_A, open('B.txt', 'r') as file_B:
   
        for line_A, line_B in file_A, file_B:
            try:
    
                numbers_A = [int(x) for x in line_A.split()]
 
                numbers_B = [int(x) for x in line_B.split()]
                
         
                result = [a * b for a, b in numbers_A, numbers_B]
                print(result)
            except ValueError:
                # Xử lý ngoại lệ khi có dòng không phải số nguyên
                print("continue")
except FileNotFoundError:
    # Xử lý ngoại lệ khi không tìm thấy tập tin
    print("Không tìm")