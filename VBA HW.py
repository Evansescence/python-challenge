Sub VBAexample()
    'sets a variable to hold total per ticker
    Dim Vol As Double
    Vol = 0
    ' sets an initial variable for \keeping track of each ticker
    Dim Total_vol As Double
    Total_vol = 2
    'efficiency improvements
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual
   ' loop through all data points
    For i = 2 To 60000
    'Check if ticker is the same as the one in the row above.
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
   'set ticker name
    ticker = Cells(i, 1).Value
   'add to the total volume
    Vol = Vol + Cells(i, 7).Value
   'print the ticker in column H
    Range("H" & Total_vol).Value = ticker
   ' Print the Volume in column I
    Range("I" & Total_vol).Value = Vol
   'add a row to the Total stock volume
    Total_vol = Total_vol + 1
   'Reset Ticker Total
    Vol = 0
    'If the cell immediately following a row is the same ticker...
    Else
    'Add to the ticker total
   Vol = Vol + Cells(i, 7).Value
       
     End If
   
   Next i
