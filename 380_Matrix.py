class Matrix:
    def __init__(self,lst):
        self.elements=lst

    def isMatrix(self):
        """"This method returns True or False on the basis of
          the given object"""
        if all(isinstance(x, (int, str)) for x in self.elements):
            gaps=0
            for element in self.elements:
                if element=='/n':
                    if self.elements.index(element)!=0:
                        break
                    else:
                        return False
                gaps+=1
                print(gaps)
            newstr=''
            for i in range(0,len(self.elements),gaps):
                if i=='/n':
                    newstr+='Y'
                else:
                    newstr+='N'
                    break
            print(newstr)
            if 'N' not in newstr:
                return True
            else:
                return False
        else:
            return False
        # To be continued - improve the logic...

    def Order(self):
        """This method returns the order of the matrix in a form of a string and
            Hits none when the given object is not a matrix"""
        proceed=self.isMatrix()
        if proceed:
            coulumns=0
            row=0
            flag='GREEN'
            for element in self.elements:
                if element!='/n' and flag=='GREEN':
                    coulumns+=1
                elif element=='/n':
                    flag='RED'
                    row+=1
                order=f"{row}x{coulumns}"
            return order
        else:
           return None
    def isNull(self):
        """This function will tells you if the matrix 
            is null matrix or not"""
        if self.isMatrix():
            count=''
            for element in self.elements:
                if element==0 or element=='/n':
                    count+='Y'
                else:
                    count+='N'
                    break
            if 'N' not in count:
                return True
            else:
                return False
        else:
            return False
    
    def isColumn(self):
        ends=0
        num=0
        for element in self.elements:
            if (self.elements.index(element)%2==0) and self.elements[self.elements.index(element)]=='/n':
                ends+=1
            else:
                num+=1
        print(num,ends)
        if ends==num:
            return True
        else:
            return False

matrix1 = Matrix([29,23,'/n',23,53,'/n',34,64,'/n'])
matrix2 = Matrix([0,0,0,'/n',0,0,0,'/n',0,0,0,'/n'])
matrix3 = Matrix([12,'/n',13,'/n',14,'/n'])
# order=matrix1.Order()
print(matrix3.isColumn())
# print("Order of the matrix is: ",order)