import math
from .common import number,integer
def run(data):
 radius=number(data.get('radius',1),1e-6,1e6);mu=number(data.get('mu',1),1e-12,1e12);step=number(data.get('step',.05),1e-9,1000);steps=integer(data.get('steps',126),1,20000)
 if step*math.sqrt(mu/radius**3)>.5:raise ValueError('step_regime')
 def a(p):
  r=math.hypot(*p)
  if r<radius*1e-6:raise ValueError('singularity')
  return [-mu*x/r**3 for x in p]
 def simulate(kind):
  p=[radius,0.];v=[0.,math.sqrt(mu/radius)];initial=-mu/(2*radius);maximum=0.
  for _ in range(steps):
   aa=a(p)
   if kind=='euler':p,v=[x+step*y for x,y in zip(p,v)],[x+step*y for x,y in zip(v,aa)]
   else:
    pn=[p[i]+step*v[i]+.5*step*step*aa[i]for i in range(2)];an=a(pn);v=[v[i]+.5*step*(aa[i]+an[i])for i in range(2)];p=pn
   energy=.5*sum(x*x for x in v)-mu/math.hypot(*p);maximum=max(maximum,abs((energy-initial)/initial))
  return {'final_position':p,'max_relative_energy_error':maximum}
 return {'euler':simulate('euler'),'velocity_verlet':simulate('verlet'),'steps':steps,'elapsed_time':step*steps,'physical_ephemeris_validated':False}
