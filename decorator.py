# def login(login_page):
#   def wrapper(user,password):
#     if user == 'admin' and password == '123456':
#       print('Login successful')
#       return login_page(user,password)
#     else:
#       print('Login failed')
#   return wrapper
# @login
# def login_page(user,password):
#   print('Welcome to the dashboard,',user)
# login_page('admin','123456')

def excecution_time(main):
  def wrapper(n):
    import time
    start_time = time.time()
    main(n)
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")
  return wrapper

@excecution_time
def main(n):
  sum=0
  for i in range(1,n+1):
    sum+=1
  print("sum is",sum) 

main(1000000)
