def admin_only(vc):
  def wrapper(username):
    if username == "admin":
      vc(username)
    else:
      print("Access Denied")
  return wrapper


@admin_only
def dashboard(username):
  print(f"Welcome to dashboard, {username}!")
dashboard("admin")    
dashboard("user")       