from pyflowchart import *

st = StartNode('Начало')
io1 = InputOutputNode(InputOutputNode.INPUT, 'buff')
cond1 = ConditionNode('len(buff) < 1')
cond2 = ConditionNode('buff[0] == В')
cond3 = ConditionNode('buff[0] == З')
cond4 = ConditionNode('buff[0] == М')
cond5 = ConditionNode('buff[0] == С')
io2 = InputOutputNode(InputOutputNode.OUTPUT, "Вы ничего не ввели!")
io3 = InputOutputNode(InputOutputNode.OUTPUT, "Военно-транспортный")
io4 = InputOutputNode(InputOutputNode.OUTPUT, "Заочный")
io5 = InputOutputNode(InputOutputNode.OUTPUT, "Механический")
io6 = InputOutputNode(InputOutputNode.OUTPUT, "Строительный")
io7 = InputOutputNode(InputOutputNode.OUTPUT, "Такого факультета не существует")
io8 = InputOutputNode(InputOutputNode.OUTPUT, "Press button to close")
e = EndNode("Конец")

st.connect(io1)
io1.connect(cond1)
cond1.connect_yes(io2)
cond1.connect_no(cond2)
cond2.connect_yes(io3)
cond2.connect_no(cond3)
cond3.connect_yes(io4)
cond3.connect_no(cond4)
cond4.connect_yes(io5)
cond4.connect_no(cond5)
cond5.connect_yes(io6)
cond2.connect_no(io7)
io2.connect(io8)
io3.connect(io8)
io4.connect(io8)
io5.connect(io8)
io6.connect(io8)
io7.connect(io8)
io8.connect(e)

fc = Flowchart(st)
print(fc.flowchart())

buff = input("Введите первую букву факультета(Остальные буквы не считываются) = ")
if len(buff) < 1:
    print("Вы ничего не ввели!")
elif buff[0] == 'В':
    print("Военно-транспортный")
elif buff[0] == 'З':
    print("Заочный")
elif buff[0] == 'М':
    print("Механический")
elif buff[0] == 'С':
    print("Строительный")
else:
    print("Такого факультета не существует")
print("press button to close")
