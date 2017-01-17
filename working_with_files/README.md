# Working with files


File can be open with "open" function provided by python standard library, 
the following would be sequence of steps for a basic file operation  
  - open the file in read mode 
  - iterate through each line in the file
  - process the line of text
  - close the file 

You can also use a context manager :
  - open the file using "with" 
  - iterate through each line in the file
  - process the file 

Context managers will hep you in avoiding boilerplate code like closing the file 
> in the context manger for for file open 
> the file will be closed implicitly after the iteration

> with open
```python
csv_file = open("MOCK_DATA.csv")
for line in csv_file:
    print line
csv_file.close()
```
> With context manager
```python
with open("MOCK_DATA.csv")
    for line in csv_file:
        print line
```