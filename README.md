We traverse both strings from end, one by one add digits and keep track of carry. To simplify the process, we do following: 
1) Reverse both strings. 
2) Keep adding digits one by one from 0’th index (in reversed strings) to end of smaller string, append the sum % 10 to end of result and keep track of carry as sum/10. 
3) Finally reverse the result. 
