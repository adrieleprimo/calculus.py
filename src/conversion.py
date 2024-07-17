unit_factors ={
    'Bytes': 1,
    'KB': 1024,
    'MB': 1024 ** 2,
    'GB': 1024 ** 3,
    'TB': 1024 ** 4
}

def convert(input_value, input_unit, output_unit):
    try:
        input_value = float(input_value)
        value_in_bytes = input_value * unit_factors[input_unit]
        output_value = value_in_bytes / unit_factors[output_unit]
        return output_value
    except ValueError:
        return 'Error: Please, enter a valid number'
    except KeyError:
        return 'Error: Invalid unit measurement'
    
def test_conversion():
            print(f"250000 KB para MB: {convert(250000, 'KB', 'MB')}") 


if __name__ == '__main__':
    test_conversion()