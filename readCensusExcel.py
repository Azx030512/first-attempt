#!python3
# readCensusExcel.py -- Tabulates population and number of Census tracts for each country
import openpyxl,pprint
print('opening workbook...')
print('Enter the absolute path to the xlsx')
address=input()
wb=openpyxl.load_work(address)
sheet=wb['population by Census Tract']
countyData={}
#Todo:Fill in countyDatawith each county's population and tracts.
print('Reading rows...')
for row in range(2,sheet.max_row+1):
    #each row in the spreadsheet has data for one census tract.
    state=sheet['B'+str(row)].value
    county=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value
    #Todo:Open a new text file and write the contents of countyData to it.
    #Make sure the keys for this state exist.
    countyData.setdefault(state,{})
    #Make sure the  key  for this county in this state exists.
    countyData[state].setdefault(county,{'tracts':0,'pop':0})
    #each row represents one census tract, so  increment by one
    countyData[state][county]['tracts']+=1
    #Increase the county pop by the pop in  this census tract.
    countyData[state][county]['pop']+=pop
    #Todo:Open a new text file and write the contents of countyDatato it.
print('Writing results...')
resultFile=open('census2010.py','w')
resultFile.write('allData='+pprint.format(countyData))
resultFile.close()
print('Done')
