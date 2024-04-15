from mypackage import myModule

def test_top_n():
    """ Testing function top_n """
    assert myModule.tp_n([8,3,2,7,4],3) == [8,7.4]
    assert myModule.tp_n([10,1,12,9,2],2) == [12,10]
    assert myModule.tp_n([1,2,3,4,5],5) == [5,4,3,2,1]    