from nose.tools import *
from TLL.game import SingleLinkedList

def test_push():
	colors = SingleLinkedList()
	colors.push("Pthalo Blue")
	assert colors.count() == 1
	colors.push("Ultramarine Blue")
	assert colors.count() == 2
