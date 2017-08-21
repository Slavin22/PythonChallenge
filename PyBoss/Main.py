import os
import csv
csvpath = os.path.join('Resources', 'employee_data1.csv')

abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

empid = []
firstname = []
lastname = []
dob = []
ssn = []
state = []

with open(csvpath, newline = "") as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')

	next(csvreader, None)

	for row in csvreader:
		empid.append(row[0])
		id = row[1].split(" ")
		firstname.append(id[0])
		lastname.append(id[1])
		birth = row[2].split("-")
		dob.append(birth[1] + "/" + birth[2] + "/" + birth[0])
		social = row[3].split("-")
		ssn.append("***-**-" + social[2])
		state.append(abbrev[row[4]])

info = zip(empid, firstname, lastname, dob, ssn, state)

newpath = os.path.join('Resources', 'EmployeeDataTextFile.csv')
with open(newpath, 'w') as newfile:
	csvwriter = csv.writer(newfile, delimiter = ',')

	csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
	csvwriter.writerows(info)

