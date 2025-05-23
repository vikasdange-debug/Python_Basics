myinfo = {
    "name":"vikas",        
    "studying":"python",
    "From_channel":"Apna_college",
    "10th std marks":87.2,
    "12th std marks":83.83,
}
print(myinfo.keys())    #returns all keys of dictionary
print(myinfo.values())     #returns all values of dictionary
print(list(myinfo.items()))  #returns all key value pairs in form of tuples
print(myinfo.get("name"))  #myinfo.get("key")#returns the value acc. to key
myinfo.update({"surname":"dange"})
print(myinfo)