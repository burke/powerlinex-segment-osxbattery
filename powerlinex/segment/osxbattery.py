from __future__ import absolute_import
import os

def _get_capacity():
    return int(os.popen("pmset -g batt | tail -1 | awk '{print $2}' | sed 's/\%\;//'").read().rstrip())

def battery(pl):
	'''Return battery charge status.

	Highlight groups used: ``battery_gradient`` (gradient), ``battery``.
	'''
	capacity = _get_capacity()
	ret = []
	ret.append({
		'contents': str(capacity) + "%",
		'highlight_group': ['battery_gradient', 'battery'],
		'gradient_level': 100 - capacity
	})
	return ret
