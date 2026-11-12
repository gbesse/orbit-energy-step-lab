import unittest,copy,json
from orbit_energy_step_lab import run
DEMO={'radius': 1, 'mu': 1, 'step': 0.05, 'steps': 126}
class DomainTests(unittest.TestCase):
 def test_conservation_difference(self):
  x=run(DEMO);self.assertLess(x['velocity_verlet']['max_relative_energy_error'],1e-5);self.assertGreater(x['euler']['max_relative_energy_error'],.1)
 def test_finer_step_improves_verlet(self):
  a=run(DEMO);b=run(dict(DEMO,step=.025,steps=252));self.assertLess(b['velocity_verlet']['max_relative_energy_error'],a['velocity_verlet']['max_relative_energy_error'])
 def test_unstable_step_rejected(self):
  with self.assertRaises(ValueError):run(dict(DEMO,step=2))
