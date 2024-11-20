st={10,20,30,40}
st.add(50)
# a.update([1]) #works
# a.add(1) #works
# a.update([1,2])#works
# a.add([1,2])#fails
st.update([1,4,5,5,5,10,40,40,30,5,6,13,25,50])
print(st)

#remove delete single element ==> Has return type
#discard deletes an elements  ==> does not have return type
#pop deletes a random element

st.remove(5)
print(st)
st.d