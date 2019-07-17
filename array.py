
class Array_:
    def __init__(self):
        """create array"""
        self.data = []

    def insert_element(self,element): 
        self.data.append(element)

    def remove_element(self,element):
        if element in self.data:
            self.data.remove(element)
        raise Exception('element not in array')    
                   
    def update_array(self,index, new_element):
        if new_element in self.data:
            self.data[index] = new_element
        raise Exception('element not in array')    
