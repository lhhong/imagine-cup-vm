from collections import OrderedDict

# COLORS = [
#     "white",
#     "beige",
#     "black",
#     "brown",
#     "grey",
#     "blue",
#     "navy",
#     "teal",
#     "green",
#     "olive",
#     "pink",
#     "red",
#     "maroon",
#     "purple",
#     "orange",
#     "yellow",
# ]

# PATTERNS = [
#     "animal-print",
#     "argyle",
#     "horizontal-stripe",
#     "vertical-stripe",
#     "checkered",
#     "dotted",
#     "floral",
#     "plaid"
# ]

# # ADD MORE MATERIALS?
# TOP_MATERIAL = [
#     "denim",
#     "dry-fit",
#     "cotton"
# ]

# TOP_TYPES = [
#     "short sleeve T-shirt",
#     "long sleeve T-shirt",
#     "Short sleeve shirt",
#     "long sleeve shirt",
#     "singlet",
#     "polo T-shirt",
# ]

# #this is more specific to t-shirts
# TSHIRT_FIT = [
#     "slim-fit",
#     "longline",
#     "baggy"
# ]

# SHIRT_FIT = [
#     "slim-fit",
#     "regular-fit"
# ]

# #should we split into t-shirt and shirt style?
# SHIRT_STYLE = [
#     "oxford",
#     "dress",
#     "graphic",
#     "pocket",
#     "granddad-collar",
# ]

# TSHIRT_STYLE = [
#     "graphic-text",
#     "graphic-image",
#     "round-neck",
#     "henley",
#     "pocket",
# ]


# BOTTOM_TYPE = [
#     "long pants",
#     "shorts",
# ]

# BOTTOM_MATERIAL = [
#     "denim/jeans",
#     "cotton",
#     "dry-fit"
# ]


# BOTTOM_STYLE = [
#     "cargo",
#     "dress",
#     "chinos",
#     "sweatpants",
# ]

# BOTTOM_FIT = [
#     "skinny-fit",
#     "slim-fit",
#     "regular-fit",
#     "baggy"
# ]

# DENIM_STYLE = [
#     "ripped",
#     "acid-wash",
#     "washed"
# ]

# SHOE_TYPE = [
#     "boat/loafer",
#     "boots",
#     "sneakers",
#     "sport",
#     "sandals",
#     "dress-shoes",
#     "casual-shoes",
# ]

# SHOE_MATERIAL = [
#     "leather",
#     "canvas",
#     "suede",
#     "rubber"
# ]

# SHOE_OTHERS = [
#     "toe-cap",
#     "gum-sole",
#     "with-logo",
#     "high-cut"

# ]

# TOPS = OrderedDict()
# TOPS["top-primary-color"] = COLORS
# TOPS["top-secondary-color"] = COLORS
# TOPS["top-type"] = TOP_TYPES
# TOPS["t-shirt-style"] = TSHIRT_STYLE
# TOPS["shirt-style"] = SHIRT_STYLE
# TOPS["t-shirt-fit"] = TSHIRT_FIT
# TOPS["shirt-fit"] = SHIRT_FIT
# TOPS["top-patterns"] = PATTERNS
# TOPS["top-material"] = TOP_MATERIAL

# BOTTOMS = OrderedDict()
# BOTTOMS["bottom-primary-color"] = COLORS
# BOTTOMS["bottom-secondary-color"] = COLORS
# BOTTOMS["bottom-type"] = BOTTOM_TYPE
# BOTTOMS["bottom-material"] = BOTTOM_MATERIAL
# BOTTOMS["denim-style"] = DENIM_STYLE
# BOTTOMS["bottom-patterns"] = PATTERNS
# BOTTOMS["bottom-style"] = BOTTOM_STYLE
# BOTTOMS["bottom-fit"] = BOTTOM_FIT


# SHOES = OrderedDict()
# SHOES["shoes-primary-color"] = COLORS
# SHOES["shoes-secondary-color"] = COLORS
# SHOES["shoes-type"] = SHOE_TYPE
# SHOES["shoes-others"] = SHOE_OTHERS
# SHOES["shoes-materials"] = SHOE_MATERIAL




### for use in classifier. as keys required for the labelled data.
shoe_primary_colours = [
    "shoes-primary-color-white",
    "shoes-primary-color-beige",
    "shoes-primary-color-black",
    "shoes-primary-color-brown",
    "shoes-primary-color-grey",
    "shoes-primary-color-blue",
    "shoes-primary-color-navy",
    "shoes-primary-color-teal",
    "shoes-primary-color-green",
    "shoes-primary-color-olive",
    "shoes-primary-color-pink",
    "shoes-primary-color-red",
    "shoes-primary-color-maroon",
    "shoes-primary-color-purple",
    "shoes-primary-color-orange",
    "shoes-primary-color-yellow",
]

shoe_secondary_colours = [
    "shoes-secondary-color-white",
    "shoes-secondary-color-beige",
    "shoes-secondary-color-black",
    "shoes-secondary-color-brown",
    "shoes-secondary-color-grey",
    "shoes-secondary-color-blue",
    "shoes-secondary-color-navy",
    "shoes-secondary-color-teal",
    "shoes-secondary-color-green",
    "shoes-secondary-color-olive",
    "shoes-secondary-color-pink",
    "shoes-secondary-color-red",
    "shoes-secondary-color-maroon",
    "shoes-secondary-color-purple",
    "shoes-secondary-color-orange",
    "shoes-secondary-color-yellow",
    "shoes-secondary-color-none" 
]

top_primary_colours = [
    "top-primary-color-white",
    "top-primary-color-beige",
    "top-primary-color-black",
    "top-primary-color-brown",
    "top-primary-color-grey",
    "top-primary-color-blue",
    "top-primary-color-navy",
    "top-primary-color-teal",
    "top-primary-color-green",
    "top-primary-color-olive",
    "top-primary-color-pink",
    "top-primary-color-red",
    "top-primary-color-maroon",
    "top-primary-color-purple",
    "top-primary-color-orange",
    "top-primary-color-yellow",
]

top_secondary_colours = [
    "top-secondary-color-white",
    "top-secondary-color-beige",
    "top-secondary-color-black",
    "top-secondary-color-brown",
    "top-secondary-color-grey",
    "top-secondary-color-blue",
    "top-secondary-color-navy",
    "top-secondary-color-teal",
    "top-secondary-color-green",
    "top-secondary-color-olive",
    "top-secondary-color-pink",
    "top-secondary-color-red",
    "top-secondary-color-maroon",
    "top-secondary-color-purple",
    "top-secondary-color-orange",
    "top-secondary-color-yellow",
    "top-secondary-color-none"
]

bottom_primary_colours = [
    "bottom-primary-color-white",
    "bottom-primary-color-beige",
    "bottom-primary-color-black",
    "bottom-primary-color-brown",
    "bottom-primary-color-grey",
    "bottom-primary-color-blue",
    "bottom-primary-color-navy",
    "bottom-primary-color-teal",
    "bottom-primary-color-green",
    "bottom-primary-color-olive",
    "bottom-primary-color-pink",
    "bottom-primary-color-red",
    "bottom-primary-color-maroon",
    "bottom-primary-color-purple",
    "bottom-primary-color-orange",
    "bottom-primary-color-yellow",
]

bottom_secondary_colours = [
    "bottom-secondary-color-white",
    "bottom-secondary-color-beige",
    "bottom-secondary-color-black",
    "bottom-secondary-color-brown",
    "bottom-secondary-color-grey",
    "bottom-secondary-color-blue",
    "bottom-secondary-color-navy",
    "bottom-secondary-color-teal",
    "bottom-secondary-color-green",
    "bottom-secondary-color-olive",
    "bottom-secondary-color-pink",
    "bottom-secondary-color-red",
    "bottom-secondary-color-maroon",
    "bottom-secondary-color-purple",
    "bottom-secondary-color-orange",
    "bottom-secondary-color-yellow",
    "bottom-secondary-color-none"
]

shoe_types = [
    "shoes-type-boat/loafer",
    "shoes-type-boots",
    "shoes-type-sneakers",
    "shoes-type-sport",
    "shoes-type-sandals",
    "shoes-type-dress-shoes",
    "shoes-type-casual-shoes",
]

shoe_materials = [
    "shoes-materials-leather",
    "shoes-materials-canvas",
    "shoes-materials-suede",
    "shoes-materials-rubber"
]

shoe_features = [
    "shoes-others-toe-cap",
    "shoes-others-gum-sole",
    "shoes-others-with-logo",
    "shoes-others-high-cut"

]

bottom_types = [
    "bottom-type-long pants",
    "bottom-type-shorts",
]

bottom_materials = [
    "bottom-material-denim/jeans",
    "bottom-material-cotton",
    "bottom-material-dry-fit"
]


bottom_styles = [
    "bottom-style-cargo",
    "bottom-style-dress",
    "bottom-style-chinos",
    "bottom-style-sweatpants",
    "bottom-style-none"
]

bottom_fits = [
    "bottom-fit-skinny-fit",
    "bottom-fit-slim-fit",
    "bottom-fit-regular-fit",
    "bottom-fit-baggy"
]

denim_styles = [
    "denim-style-ripped",
    "denim-style-acid-wash",
    "denim-style-washed"
]

bottom_patterns = [
    "bottom-patterns-animal-print",
    "bottom-patterns-argyle",
    "bottom-patterns-horizontal-stripe",
    "bottom-patterns-vertical-stripe",
    "bottom-patterns-checkered",
    "bottom-patterns-dotted",
    "bottom-patterns-floral",
    "bottom-patterns-plaid"
]

top_patterns = [
    "top-patterns-animal-print",
    "top-patterns-argyle",
    "top-patterns-horizontal-stripe",
    "top-patterns-vertical-stripe",
    "top-patterns-checkered",
    "top-patterns-dotted",
    "top-patterns-floral",
    "top-patterns-plaid"
]

top_materials = [
    "top-material-denim",
    "top-material-dry-fit",
    "top-material-cotton"
]

top_types = [
    "top-type-short-sleeve-t-shirt",
    "top-type-long-sleeve-t-shirt",
    "top-type-short-sleeve-shirt",
    "top-type-long-sleeve-shirt",
    "top-type-singlet",
    "top-type-polo",
]

#this is more specific to t-shirts
t_shirt_fits = [
    "t-shirt-fit-slim-fit",
    "t-shirt-fit-longline",
    "t-shirt-fit-baggy",
    "t-shirt-fit-regular"
]

shirt_fits = [
    "shirt-fit-slim-fit",
    "shirt-fit-regular-fit"
]

#should we split into t-shirt and shirt style?
shirt_styles = [
    "shirt-style-oxford",
    "shirt-style-dress",
    "shirt-style-graphic",
    "shirt-style-pocket",
    "shirt-style-granddad-collar",
]

t_shirt_styles = [
    "t-shirt-style-graphic-text",
    "t-shirt-style-graphic-image",
    "t-shirt-style-round-neck",
    "t-shirt-style-henley",
    "t-shirt-style-pocket",
]

KEYS = {}

KEYS['Top_primary_colours'] = top_primary_colours
KEYS['Top_secondary_colours'] = top_secondary_colours
KEYS['Top_types'] = top_types
KEYS['T-shirt_styles'] = t_shirt_styles
KEYS['Shirt_styles'] = shirt_styles
KEYS['T-shirt_fits'] = t_shirt_fits
KEYS['Shirt_fits'] = shirt_fits
KEYS['Top_patterns'] = top_patterns
KEYS['Top_materials'] = top_materials

KEYS['Bottom_primary_colours'] = bottom_primary_colours
KEYS['Bottom_secondary_colours'] = bottom_secondary_colours
KEYS['Bottom_types'] = bottom_types
KEYS['Bottom_materials'] = bottom_materials
KEYS['Denim_styles'] = denim_styles
KEYS['Bottom_patterns'] = bottom_patterns
KEYS['Bottom_fits'] = bottom_fits
KEYS['Bottom_styles'] = bottom_styles

KEYS['Shoe_primary_colours'] = shoe_primary_colours
KEYS['Shoe_secondary_colours'] = shoe_secondary_colours
KEYS['Shoe_types'] = shoe_types
KEYS['Shoe_materials'] = shoe_materials
KEYS['Shoe_features'] = shoe_features

# with proper names
KEYS2 = {}