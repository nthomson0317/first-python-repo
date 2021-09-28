### Methods
### functions that are built into objects

mylist = [1,2,3]

mylist.append(4)
#==> [1,2,3,4]

mylist.pop()
#==> 4
print(mylist)
#==> [1,2,3]

# help(mylist.insert)
#==> insert(index, object, /) method of builtins.list instance
    #==> Insert object before index.


### Functions

def name_of_function(name):
    '''
    Docstring explains function.
    '''
    print("Hello" + ', ' + name)

name_of_function('Jose')