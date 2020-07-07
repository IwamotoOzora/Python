import python2_test2

def test_is_leap_year():
    # 400で割り切れるパターン
    divisible_400 = 2000
    actual = python2_test2.is_leap_year(divisible_400)
    assert actual == True
    
    # 100で割り切れるパターン
    divisible_100 = 1000
    actual = python2_test2.is_leap_year(divisible_100)
    assert actual == False

    # 4で割り切れるパターン
    divisible_4 = 2020
    actual = python2_test2.is_leap_year(divisible_4)
    assert actual == True
    
    # 上記のどれにもあてはまらないパターン
    not_apply = 1001
    actual = python2_test2.is_leap_year(not_apply)
    assert actual == False