class Category:
  def __init__(self,name):
    self.name=name
    self.ledger=[]

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
  
  def get_balance(self):
    balance=sum([entry["amount"] for entry in self.ledger])
    return balance
  
  def check_funds(self, amount):
    if self.get_balance()>=amount:
      return True
    else:
      return False

  def withdraw(self,amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def transfer(self, amount, other_cat):
    if self.check_funds(amount):
      desc=f"Transfer to {other_cat.name}"
      self.withdraw(amount, description=desc)
      desc=f"Transfer from {self.name}"
      other_cat.deposit(amount, description=desc)
      return True
    else:
      return False
  
  def __str__(self):
    n_asterisks=(30-len(self.name))//2
    string=n_asterisks*"*"+self.name+n_asterisks*"*"+"\n"

    for entry in self.ledger:
      string+=f"{entry['description']:<23.23}{entry['amount']:>7.2f}\n"
    string+=f"Total: {self.get_balance()}"
    return string 

def create_spend_chart(categories):
  fundict={}
  for category in categories:
    amnt=0
    for entry in category.ledger:
      if entry["amount"]<0:
        amnt+=-entry["amount"]
    fundict[category.name]=amnt
  
  total=sum(fundict.values())
  width=1+(3*(len(fundict)))
  for cat in fundict:
    fundict[cat]=((fundict[cat]/total)*100 - (fundict[cat]/total)*100%10)
  
  string="Percentage spent by category\n"

  percentages=range(100,-1,-10)
  for percentage in percentages:
    string+=f"{percentage:>3}|"
    for cat in fundict:
      if percentage<=int(fundict[cat]):
        string+=" o "
      else:
        string+=" "*3
    string+=" \n"
  string+=f"{' '*4}{width*'-':>}\n"
  for i in range(len(max(fundict.keys(),key=len))):
    string+=5*" "
    for key in fundict.keys():
      if len(key)>i:
        string+=key[i]+"  "
      else:
        string+="   "
    string+="\n"
  string=string.rstrip("\n")
  return string