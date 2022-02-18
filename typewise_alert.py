breach_values = {1:'NORMAL',2:'TOO_HIGH',3:'TOO_LOW'}

cooling_types = {'PASSIVE_COOLING':{'lower_limit':0,'upper_limit':35},
'HI_ACTIVE_COOLING':{'lower_limit':0,'upper_limit':45},
'MED_ACTIVE_COOLING':{'lower_limit':0,'upper_limit':40}}


def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return breach_values[3]
  if value > upperLimit:
    return breach_values[2]
  return breach_values[1]


def classify_temperature_breach(coolingType, temperatureInC):
  return infer_breach(temperatureInC, cooling_types[coolingType]['lower_limit'], cooling_types[coolingType]['upper_limit'])


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
