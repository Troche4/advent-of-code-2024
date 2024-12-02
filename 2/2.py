file = open("/Users/trey/advent-of-code-2024/2/input.txt", "r")

reports = []
for line in file.read().split("\n"):
    levels = list(map(int, line.split(" ")))
    reports.append(levels)


def validateReport(report):
    safe = True
    if len(set(report)) != len(report):
        safe = False

    decreases = False
    increases = False
    for i in range(0, len(report)-1):
        if (report[i] > report[i+1]):
            decreases = True
        if (report[i] < report[i+1]):
            increases = True
        diff = abs(report[i] - report[i+1])
        if diff > 3:
            safe=False
        
    if increases and decreases:
        safe = False

    return safe

    
safeReports = []
for report in reports:
    if validateReport(report):
        safeReports.append(report)


print("part one:", len(safeReports))

safeDampenedReports = []
for report in reports:
    if validateReport(report):
        safeDampenedReports.append(report)
    else:
        hasDampenedReport = False
        for i in range(0, len(report)):
            dampenedReport = list(report)
            del dampenedReport[i]
            if validateReport(dampenedReport):
                hasDampenedReport = True

        if (hasDampenedReport):
            safeDampenedReports.append(report)

print("part two:", len(safeDampenedReports))


