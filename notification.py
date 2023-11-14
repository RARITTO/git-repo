from plyer import notification
folder = 'beer.ico'
if __name__ == "__main__":
    
    
    notification.notify(
        title="Please Drink Alcohol Daily",#heading data 
        message="It makes you happy and also provides relief from the pain of anxiety, so please drink alcohol daily, time to time.", #what kind of data your wanted to enter 
        app_icon= "C:\Users\Lalit\Downloads\beer.ico", # choose the icon location carefullu
        timeout=10
    )

print('You got the notification successfully')
