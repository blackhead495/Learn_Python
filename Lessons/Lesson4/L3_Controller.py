import L1_Model_Summ as Summ
import L1_Model_Mult as Mult
import L2_View as View


def butten_click():
    value_a = View.get_value()
    value_b = View.get_value()

    Mult.init(value_a, value_b)

    #result = Summ.summ()
    result = Mult.mult()

    View.view(result, "mult")
