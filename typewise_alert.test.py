import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
  
  def test_infers_breach_as_high_limits(self):
    self.assertTrue(typewise_alert.infer_breach(110,50, 100)=='TOO_HIGH')
  
  def test_infers_breach_as_normal_limits(self):
    self.assertTrue(typewise_alert.infer_breach(75,50, 100)=='NORMAL')

  def test_classify_temperature_breach_PASSIVE_COOLING_NORMAL(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',30)=='NORMAL')
  
  def test_classify_temperature_breach_PASSIVE_COOLING_HIGH(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',40)=='TOO_HIGH')
  
  def test_classify_temperature_breach_PASSIVE_COOLING_LOW(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',-40)=='TOO_LOW')


if __name__ == '__main__':
  unittest.main()
