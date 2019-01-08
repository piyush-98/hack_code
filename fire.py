from urllib import request
from firebase import firebase
firebase=firebase.FirebaseApplication("https://lifesaver-18f28.firebaseio.com/")
res=firebase.put("/dir","count","forward")  
