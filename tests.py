def main():
    '''
    This function tests the classes and methods for the final project.
    param list: none
    returns: none
    '''
    print("####### Testing Mallet Model #######")
    test_mallet = mallet.Mallet()

    print("####### Testing Mallet Image #######")
    test_mallet.mouse.set_cursor()
    test_mallet.mouse.get_cursor()
    assert test_mallet.mouse.set_visible() == True

    print("=====Standard Input Test=====")
    test_mallet.mouse.set_pos(5)
    assert test_mallet.get_pos() == (5,0)

    print("=====Zero Input Test=====")
    test_mallet.mouse.set_pos(0)
    assert test_mallet.get_pos() == (0,0)

    print("=====Negative Input Test=====")
    test_mallet.mouse.stet_pos(-1)
    assert test_mallet.get_pos() == (-1,0)

    print("####### Testing Mole Model #######")
    test_mole = mole.Mole()

    print("=====Testing Mole Position=====")
    test_mole.sprite.Sprite()
    assert test_mole.sprite.Sprite() == True

    print("=====Testing if Mole is Hit=====")
    test_mole.sprite.spritecollideany(mallet)
    assert test_mole.sprite.spritecollideany(mallet) == True

main()
