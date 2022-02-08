def getMinCost(crew_id, job_id):
    crew = []
    job = []
    for i in range(crew_id):
        crew.append(int(input()))
    for i in range(job_id):
        job.append(int(input()))
    crew.sort()
    job.sort()
    output = 0
    for c,j in zip(crew,job):
        output += abs(c-j)
    print(output)

if __name__ == '__main__':
    crew_id = int(input("Enter crewid : "))
    job_id = int(input("Enter jobid : "))
    getMinCost(crew_id,job_id)