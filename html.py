import csv

with open ("info.csv","r",encoding="utf-8")as f:
    customers=list(csv.DictReader(f))

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Customer Information Portal</title>
</head>

<body>

<h1>Customer Information Portal</h1>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>City</th>
    </tr>
"""

for customer in customers:
     html += f"""
    <tr>
        <td>{customer['id']}</td>
        <td>{customer['name']}</td>
        <td>{customer['email']}</td>
        <td>{customer['city']}</td>
    </tr>
    """

html += """
</table>

</body>
</html>
""" 
with open("index.html","w",encoding="utf-8") as f:
     f.write(html)

