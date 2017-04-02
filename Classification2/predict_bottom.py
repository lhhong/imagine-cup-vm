def predict_bottom_primary_colour(bottleneck_values):

	return bottom_primary_colour


def predict_bottom_secondary_colour(bottleneck_values):

	return bottom_secondary_colour


def predict_bottom_type(bottleneck_values):

	return bottom_type


def predict_bottom_material(bottleneck_values):

	return bottom_material


def predict_denim_style(bottleneck_values):

	return denim_style


def predict_bottom_pattern(bottleneck_values):

	return bottom_pattern


def predict_bottom_fit(bottleneck_values):

	return bottom_fit


def predict_bottom(bottleneck_values):
	summary = {}
	summary['Clothing type'] = 'Bottom'

	bottom_primary_colour = predict_bottom_primary_colour(bottleneck_values)
	summary['Bottom primary colour'] = bottom_primary_colour

	bottom_secondary_colour = predict_bottom_secondary_colour(bottleneck_values)
	summary['Bottom secondary colour'] = bottom_secondary_colour

	bottom_type = predict_bottom_type(bottleneck_values)
	summary['Bottom type'] = bottom_type

	bottom_material = predict_bottom_material(bottleneck_values)
	summary['Bottom material'] = bottom_material

	if bottom_material is 'Denim':
		denim_style = predict_denim_style(bottleneck_values)
		summary['Denim style'] = denim_style

	bottom_pattern = predict_bottom_pattern(bottleneck_values)
	summary['Bottom pattern'] = bottom_pattern

	bottom_fit = predict_bottom_fit(bottleneck_values)
	summary['Bottom fit'] = bottom_fit

	return summary