#Little Theorem of Queue is used for this exercise to predict agent availability
#Waiting time in queue= Rho/(Mue(1-Rho))
#Rho <- Lambda/Mue
#Lambda <- arriavl rate
#Mue <- service rate

from datetime  import datetime
import csv

issue=[] 
start_time=[]
end_time=[] 
def read_csv():
    """ Read a CSV into a list. """
    with open('Test.csv', 'r') as file:
        fields=file.readline().strip().split(',')
        issues=csv.DictReader(file,',')
        issues.fieldnames=fields
        for row in issues:
            issue.append(row['issue'])
            start_time.append(datetime.strptime(row['start_time'],"%Y-%m-%d %H:%M:%S"))
            if(row['status']=='Resolved'):
                end_time.append(datetime.strptime(row['answer_time'],"%Y-%m-%d %H:%M:%S"))
    return issue,start_time,end_time

def getRate(s_time):
    d=(s_time[-1]-s_time[0]).seconds
    d=d/3600
    return len(s_time)/d

def getAvgWait(Lambda, Mue):
    """Calculate average waiting time in seconds"""
    Rho = Lambda/(Mue*1.0)
    if Rho!=0:
         wait=(Rho/(Mue*(1-Rho)))*60
         if wait<0:
            wait=wait*(-1)

    else:
        exit()
    return wait

def main():
    issue,start_time,end_time=read_csv()
    #print(issue,start_time,end_time)
    Lambda = getRate(start_time)
    Mue = getRate(end_time)
    
    avg_wait = getAvgWait(Lambda,Mue)
    print "Predicted waiting time for a new issue is approx. ",avg_wait," minutes"


if __name__=="__main__":
    main()