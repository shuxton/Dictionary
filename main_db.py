import mysql.connector


con=mysql.connector.connect(
    user = "ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor=con.cursor()

def search(word):
    query=cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' "%word)
    results=cursor.fetchall()
    if results:
        return results
    else:
        word.lower()
        query=cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' "%word)
        results=cursor.fetchall()
        if results:
            return results
        else:
            return "Word doesn't exist"

    
    



while(True):
    word=input("Enter a word: ")
    if(word=="0"):
        break
    results=search(word)
    if type(results)==list:
        for result in results:
            print(result)
    else:
        print(results)