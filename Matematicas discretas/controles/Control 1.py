from docplex.mp.model import Model

mdl = Model(name='Modelo')

x1= mdl.continous_var(name='x1')
x2= mdl.continous_var(name='x2')

mdl.add_constraint(x1 + x2 <= 80)
mdl.add_constraint(2*x1 + x2 <= 100)
mdl.add_constraint(x1 <= 40)

mdl.maximize(27*x1 + 21*x2-1*x1-9*x2-14*x1-10*x2)
