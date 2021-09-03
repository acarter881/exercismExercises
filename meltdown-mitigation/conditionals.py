def is_criticality_balanced(temperature, neutrons_emitted):
    '''

    :param temperature: int
    :param neutrons_emitted: int
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    '''
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    '''

    :param voltage: int
    :param current: int
    :param theoretical_max_power: int
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient

    These percentage ranges are calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    '''
    if (voltage * current) / theoretical_max_power >= 0.80 and (voltage * current) / theoretical_max_power <= 1:
        return 'green'
    elif (voltage * current) / theoretical_max_power >= 0.60 and (voltage * current) / theoretical_max_power < 0.80:
        return 'orange'
    elif (voltage * current) / theoretical_max_power >= 0.30 and (voltage * current) / theoretical_max_power < 0.60:
        return 'red'
    else:
        return 'black'
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    '''

    :param temperature:
    :param neutrons_produced_per_second:
    :param threshold:
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 40% of threshold == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    '''
    if (temperature * neutrons_produced_per_second) < (0.40 * threshold):
        return 'LOW'
    elif (temperature * neutrons_produced_per_second) >= (0.90 * threshold) and (temperature * neutrons_produced_per_second) <= (1.10 * threshold):
        return 'NORMAL'
    else:
        return 'DANGER'
