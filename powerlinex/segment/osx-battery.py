from __future__ import absolute_import
import os

def _get_capacity():
    return int(os.popen("pmset -g batt | tail -1 | awk '{print $2}' | sed 's/\%\;//'").read().rstrip())

def battery(pl, format='{batt:3.0%}', steps=5, gamify=False):
	'''Return battery charge status.

	:param int steps:
		number of discrete steps to show between 0% and 100% capacity
	:param bool gamify:
		measure in hearts (♥) instead of percentages

	Highlight groups used: ``battery_gradient`` (gradient), ``battery``.
	'''
	capacity = _get_capacity()
	ret = []
	denom = int(steps)
	numer = int(denom * capacity / 100)
	full_heart = '♥'
	if gamify:
		ret.append({
			'contents': full_heart * numer,
			'draw_soft_divider': False,
			'highlight_group': ['battery_gradient', 'battery'],
			'gradient_level': 99
		})
		ret.append({
			'contents': full_heart * (denom - numer),
			'draw_soft_divider': False,
			'highlight_group': ['battery_gradient', 'battery'],
			'gradient_level': 1
		})
	else:
		batt = numer / float(denom)
		ret.append({
			'contents': format.format(batt=batt),
			'highlight_group': ['battery_gradient', 'battery'],
			'gradient_level': batt * 100
		})
	return ret
