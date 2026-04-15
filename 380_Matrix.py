class Matrix:
    def __init__(self,lst):
        self.elements=lst

    def isMatrix(self):
        """"This method returns True or False on the basis of
          the given object """
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
            if 'n' not in newstr.lower():
                return True
            else:
                return False
        else:
            return False
        # Almost done improve the logic

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
                

matrix1 = Matrix([29,23,'/n',23,53,34,64,'/n'])
order=matrix1.isMatrix()
print("Order of the matrix is: ",order)