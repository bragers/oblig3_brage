from oblig2software_testing_brage_svedbergh import isLeapYear

#dividable with 4 but not 100, this should succeed
def test_isLeapYear_Div4Not100():
    assert isLeapYear(2020)

#dividable with 400, this should succeed
def test_isLeapYearDivOnly400():
    assert isLeapYear(2000)

#not dividable with 4
def test_isLeapYearNotDivOnly4():
    assert not isLeapYear(2023)

#dividable with 100 but not 400
def test_isLeapYearDiv100Not400():
    assert not isLeapYear(1700)