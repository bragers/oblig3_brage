
def isLeapYear(year: int):
    if year % 400 == 0:
        print("{0} is a leap year".format(year))
        return True

    elif year % 4 == 0 and year % 100 != 0:
        print("{0} is a leap year".format(year))
        return True
    
    else:
        print("{0} is not a leap year".format(year))
        return False

isLeapYear(2022)
{
    "github-actions.workflows.pinned.workflows": [".github/workflows/build.yml", ".github/workflows/create.yml"],
    "github-actions.workflows.pinned.refresh.enabled": true,
    "github-actions.workflows.pinned.refresh.interval": 65,
}