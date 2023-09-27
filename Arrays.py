# # Word one
# def getValidWord(s, dictionary):
#     dictionary.sort()  # Sort the dictionary in lexicographical order
#     result = None

#     for word in dictionary:
#         i = 0
#         j = 0
#         while i < len(s) and j < len(word):
#             if s[i] == word[j]:
#                 j += 1
#             i += 1

#         if j == len(word) and (result is None or word < result):
#             result = word

#     return result if result is not None else "-1"
# # Example usage:
# s = "hgferyjkllkop"
# dictionary = ["coffee", "coding", "happy", "hello", "hop"]
# result = getValidWord(s, dictionary)
# print(result)




# # Machines one
# def getMinMachines(start, end):
#     n = len(start)
    
#     # Create lists to store the start and end times separately
#     events = []
#     for i in range(n):
#         events.append((start[i], 1))  # 1 represents the start of a task
#         events.append((end[i], -1))   # -1 represents the end of a task
    
#     # Sort the events by time and type (start before end)
#     events.sort(key=lambda x: (x[0], -x[1]))
    
#     machines_in_use = 0
#     min_machines_required = 0
    
#     for event in events:
#         time, event_type = event
#         machines_in_use += event_type
#         min_machines_required = max(min_machines_required, machines_in_use)
    
#     return min_machines_required

# # Example usage
# start = [1, 8, 3, 9, 6]
# end = [7, 9, 6, 14, 7]
# print(getMinMachines(start, end))  # Output: 3



