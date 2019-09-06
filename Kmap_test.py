# CSE 101 - IP HW2
# K-Map Minimization 
# Name:Samarth Chauhan
# Roll Number:2018410
# Section:B
# Group:3
# Date:17-10-2018

import unittest
from HW2_2018410 import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(1,"(1)d-"),"w")
		self.assertEqual(minFunc(2,"(1,2)d-"),"w'x+ wx'")
		self.assertEqual(minFunc(2,"(1,2,3)d-"),"w+ x")	
		self.assertEqual(minFunc(3,"(1,2,3,4)d(0,5)"),"w'+ x'")
		self.assertEqual(minFunc(4,"(1,3,7,11,15)d(0,2,5)"),"w'x'+ yz OR w'z+ yz")
		self.assertEqual(minFunc(4,"(4,5,6,10,11)d(8)"),"w'xy'+ w'xz'+ wx'y")
		self.assertEqual(minFunc(4,"(0,1,2,4,5,6,8,9,12,13,14)d-"),"w'z'+ xz'+ y'")
		self.assertEqual(minFunc(4,"(0,1,2,3)d(12,13,14,15)"),"w'x'")
	
	
                
if __name__=='__main__':
	unittest.main()
