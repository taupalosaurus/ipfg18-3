test = {
  'name': 'question 3.7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(prime_list(10)) == list
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': "",
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(prime_list(20), [2, 3, 5, 7, 11, 13, 17, 19])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(prime_list(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
