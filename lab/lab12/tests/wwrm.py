test = {
  'name': 'wwrm',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '37de428eeea5d0a4af75ab3e75a3f0e5',
          'choices': [
            'Only fizzbuzz',
            'Only fizz',
            'Only fizzbuzz, fizz, and buzz',
            'Only fizzbuzzbuzz',
            'Only fizzbuzz or buzz'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '(fizz(buzz|)|buzz)'
        },
        {
          'answer': '00e233a218fc57a529dc7afe14773c13',
          'choices': [
            'Signed or unsigned numbers like +1000, -1.5, .051',
            'Only unsigned numbers like 0.051',
            'Only signed numbers like +1000, -1.5',
            'Only signed or unsigned integers like +1000, -33'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '[-+]?\\d*\\.?\\d+'
        },
        {
          'answer': 'db80a09ec6a93dc615e88380fb253ed0',
          'choices': [
            'Numbers that are both greater than 5 and divisible by 5 like 10, 25, 800',
            'Numbers that are divisible by 5 like 5, 20, 6325',
            'Any positive number',
            'Numbers that are divisible by 5 but do not have the digits 0 and 5 adjacent to each other as the last 2 digits'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '[1-9]+[05]+'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
