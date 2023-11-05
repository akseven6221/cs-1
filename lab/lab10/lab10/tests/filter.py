test = {
  'name': 'my-filter',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (my-filter even? '(1 2 3 4))
          f6d93158137814c549d98372b81a6666
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? '(1 3 5))
          2b642a9b7568a2206bdc1a3d944f1dc2
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? '(2 4 6 1))
          2c988a84918e0b2958168830ef8b7391
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter even? '(3))
          5d4e7085bcd945f8a26f87865c684069
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (my-filter odd? nil)
          5d4e7085bcd945f8a26f87865c684069
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (my-filter even? '(1 2 3 4)) ; checks you dont use builtin filter
          f6d93158137814c549d98372b81a6666
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (define filter nil)
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
