# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:48:24 2024

@author: Saad Saboor

"""




import math as math

class TranspositionCipher(object):
        
    def __init__(self, key):
        self.key = key
        
    def encrypt_message(self, message):
        message_characters = list(message.lower())
        message_length = len(message_characters)
        # print(message_length)
        encrypted_msg = ''
        
        for col in range(self.key):
            # print(col)
            for row in range(math.ceil(message_length / self.key)):
                # print(row)
                index = col + row * self.key
                # print(index)
                
                if index < message_length:
                    encrypted_msg += message_characters[index]  
        
        return encrypted_msg
                        
    def decrypt_message(self,message):
        message_characters = list(message.lower())
        message_length = len(message_characters)
        message_ceil = math.ceil(message_length / self.key)
        
        decrypted_msg = ''
        calculate_empty_cells = self.key * message_ceil - message_length
        message_grid = [['' for _ in range(message_ceil)] for _ in range(self.key)]
        iterator = iter(message_characters)
        
        
        for i in range(self.key):
            if i < self.key - calculate_empty_cells:
                columns = message_ceil
            else:
                columns = message_ceil - 1 
                
            for j in range(columns):
                message_grid[i][j] = next(iterator , None)
            
            
            
        for j in range(message_ceil):
          for i in range(self.key):
              decrypted_msg += message_grid[i][j]
              
        
        return decrypted_msg
    
x = TranspositionCipher(6)

plain_text_message = "Learning Python is fun"
encrypted_msg = x.encrypt_message(plain_text_message)
print('encrypted Message' , encrypted_msg)


decrypt = x.decrypt_message(encrypted_msg)
print('decrypt_message ' , decrypt)



        
        
        