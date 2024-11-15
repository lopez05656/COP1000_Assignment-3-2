#Function: This program determines if a student will be admitted or rejected.
#Input:  Interactive
#Output: Accept or Reject

# Get input and convert to correct data type for testScore and classRank
testScore = int(input("Please Enter this student's test score: "))
classRank = int(input("Now please Enter this student's class rank: "))

# Test using admission requirements and print Accept or Reject
if testScore >= 90:
  if classRank >= 25:
    print("Admission Accepted...")
  else:
    print("Admission Rejected...")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Admission Accepted...")
    else:
      print("Admission Rejected...")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Admission Accepted...")
      else:
        print("Admission Rejected...")
    else:
      print("Admission Rejected...")
