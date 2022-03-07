# Short Circuiting
is_Friend = True
is_User = True

print(is_Friend and is_User)

# Short Circuiting
is_Friend = True
is_User = True

if is_Friend or is_User:
    print('best friends forever')

# Short Circuiting
is_Friend = True
is_User = True

if is_Friend or is_User:
    print('best friends forever')
    
# Short Circuiting
is_Friend = False
is_User = True

if is_Friend and is_User:
    print('best friends forever')

