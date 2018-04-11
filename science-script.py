#!/usr/bin/python

# need this to generate randomness
import random

# defining the text lists
fieldList = ['physics', 'biology', 'chemistry',
'economics', 'history', 'sociology']

workTypeGeneric = ['study', 'report', 'overview',
'theory', 'analysis', 'summary',
'review', 'survey', 'investigation',
'comparison', 'model', 'foundations']
workTypeSTEM = ['technical note', 'Monte Carlo', 'simulation',
'computation', 'trial', 'document',
'test', 'determination', 'proof']
optionalWorkPrefix = ['follow-up', 'preliminary', 'improved',
'initial', 'first', 'complete',
'comprehensive', 'interim', 'concept',
'proposed', 'empirical', 'internal',
'novel', 'new', 'inductive',
'in-depth', 'final', 'revised']

toolTypeGeneric = ['laboratory', 'tabletop', 'field']
toolTypePhysics = ['collider', 'accelerator', 'passive']
toolTypeChemistry = ['UV', 'X-ray', 'laser']
toolTypeBiology = ['chemical', 'bioreactor', 'microscope']

toolReport = ['scan', 'probe', 'experiment',
'study', 'measurement', 'imaging']

addressWork = ['on', 'about', 'concerning',
'regarding', 'reevaluating', 'addressing']

# broken down by fields for better lists
babblePrefixGeneric = ['repeated', 'rare', 'unique',
'common', 'induced', 'hypothetical',
'dual', 'deep', 'networked',
'recursive', 'layered', 'recurring',
'singular', 'structured', 'embedded',
'warped', 'artificial', 'monadic',
'speculative', 'convoluted', 'inferred',
'fabricated', 'inhibited', 'hidden',
'algorithmic', 'observable', 'additive',
'parallel', 'adversarial', 'stochastic',
'statistical', 'stable', 'critical',
'fragile', 'generative', 'temporal',
'material', 'electronic', 'static',
'mobile', 'inverted', 'latent',
'fundamental', 'ambient', 'cyclic',
'recurring', 'aligned', 'separated',
'ordered', 'universal', 'restricted',
'recent', 'effective', 'apparent',
'balanced', 'specific', 'connected']

babblePrefixPhysics = ['massive', 'manifold', 'light',
'accelerated', 'subtractive', 'weak',
'strong', 'scalar', 'nuclear',
'commutating', 'bayesian', 'frequentist',
'degenerate', 'luminal', 'symmetric',
'fractal', 'vectorised', 'generalised',
'gravitational', 'elastic', 'lossless']

babblePrefixBiology = ['viral', 'endemic', 'pathological',
'genetic', 'soluable', 'expressive',
'mutable', 'sequenced', 'methylated',
'light', 'bacterial', 'cellular',
'soluable', 'suspended', 'emulsified',
'sustained', 'clinical', 'in-vitro',
'living', 'vitrified', 'calcified']

babblePrefixChemistry = ['soluable', 'suspended', 'emulsified',
'crystalline', 'planar', 'manifold',
'massive', 'light', 'symmetric',
'asymmetric', 'dissolved', 'fractional',
'bonded','computational','plastic',
'sustained', 'sublimated', 'vaporised',
'aerolised', 'frozen', 'molten']

babblePrefixHistory = ['medieval','european','political',
'national', 'global', 'local',
'important', 'far-reaching', 'visited',
'falsified', 'verified', 'sourced',
'memetic', 'classical', 'ancient',
'trusted', 'reported', 'documented']

babblePrefixEconomics = ['national', 'global', 'local',
'pecuniary', 'political', 'driven',
'motivated', 'technical', 'visionary',
'sustainable', 'ethical', 'fake',
'memetic', 'volatile', 'predictive',
'trusted', 'optimal', 'leveraged']

babblePrefixSociology = ['national', 'global', 'local',
'social', 'compelled', 'deliberate',
'political', 'fake', 'ethical',
'accidental', 'predictable', 'formative',
'memetic', 'economic', 'testable',
'academic', 'distributed', 'conclusive']

babbleGeneric1 = ['meta', 'super', 'inter',
'uni', 'intra', 'ultra',
'proto', 'anti', 'hyper',
'un', 'mono', 'pre',
'poly', 'multi',
'co-', 'sub', 'endo',
'macro', 'nano',
'micro', 'exo', 'para',
'homo', 'trans', 'quasi']

babblePhysics1 = ['cryo', 'radio', 'quantum ',
'bulk ', 'phase ', 'tensor',
'block ', 'cross', 'n-',
'z-', 's-', 'r-']

babbleChemistry1 = ['cryo', 'radio', 'quantum ',
'bulk ', 'phase ', 'hydro',
'block-', 'cross', 'n-',
'z-', 's-', 'r-']

babbleBiology1 = ['cardio', 'neuro', 'sucra',
'angio', 'immuno', 'oleo',
'telo', 'amino', 'pheno',
'bio', 'phyto', 'meso']

babbleHistory1 = ['war ', 'peace ', 'land ',
'sea ', 'space ', 'post',
'state ', 'imperial ', 'royal ']

babbleEconomics1 = ['socio', 'cyber', 'eco',
'neo', 'geo', 'market ',
'block-', 'cross', 'post']

babbleSociology1 = ['socio','cyber', 'eco',
'neo', 'retro', 'ethno',
'block-', 'cross', 'post']

babbleGeneric2 = ['events', 'dimensions', 'sources',
'collisions', 'devices', 'mappings',
'remnants', 'chains', 'potentials',
'clusters', 'actions', 'buffers',
'reactions', 'processes', 'patterns']

babblePhysics2 = ['particles', 'emissions', 'projections',
'calculations', 'cavitations', 'conductors',
'trajectories', 'arrays', 'cascades',
'bosons', 'leptons', 'hadrons',
'mesons', 'poles', 'quarks',
'rings', 'spaces', 'fluids',
'matter', 'lattices', 'remnants',
'surfaces', 'excitations', 'topologies',
'resonances', 'coefficients', 'oscillations']

babbleChemistry2 = ['structures', 'imprints', 'formations',
'rings', 'oxides', 'solvents',
'lubricants', 'depositions', 'growths',
'fluids', 'cavitations' , 'conductors',
'calculations', 'cascades', 'magnets',
'peptides', 'solids', 'bonds',
'films', 'matter', 'fluids',
'filters', 'excitations', 'surfaces',
'resonances', 'coefficients', 'minerals']

babbleBiology2 = ['structures', 'rhizomes', 'formations',
'rings', 'oxides', 'solvents',
'lubricants', 'depositions', 'growths',
'fluids', 'cavitations' , 'matrices',
'calculations', 'cascades', 'magnets',
'peptides', 'solids', 'bonds',
'fluids', 'lattices', 'films',
'coefficients', 'cultures', 'scaffolds',
'signalling', 'saccharids', 'acids']

babbleHistory2 = ['media', 'narratives', 'timelines',
'aggressions', 'trends', 'economies',
'conflicts', 'populations', 'excavations',
'histories', 'protests', 'movements',
'remnants', 'ruins', 'artifacts',
'cultures', 'societies', 'civilisations']

babbleEconomics2 = ['media', 'narratives', 'timelines',
'fluctuations', 'trends', 'predictions',
'conflicts', 'populations', 'crashes',
'histories', 'collapses', 'movements',
'indicators', 'signals', 'warnings',
'funds', 'accounts', 'treasuries']

babbleSociology2 = ['media', 'narratives', 'timelines',
'fluctuations', 'trends', 'assignations',
'teachings', 'populations', 'crashes',
'histories', 'collapses', 'movements',
'cultures', 'societies', 'identities',
'journalism', 'propaganda', 'messaging']


# Loop to make several of these...
for x in range(0, 15):

    # Decide scientific field
    fieldType = random.choice(fieldList)

    # Use this to create the appropriate pools
    if fieldType == 'physics':
        toolType = toolTypePhysics + toolTypeGeneric
        workType = workTypeGeneric + workTypeSTEM
        babblePrefix = babblePrefixGeneric + babblePrefixPhysics
        babble1 = babbleGeneric1 + babblePhysics1
        babble2 = babbleGeneric2 + babblePhysics2
    if fieldType == 'chemistry':
        toolType = toolTypeChemistry + toolTypeGeneric
        workType = workTypeGeneric + workTypeSTEM
        babblePrefix = babblePrefixGeneric + babblePrefixChemistry
        babble1 = babbleGeneric1 + babbleChemistry1
        babble2 = babbleGeneric2 + babbleChemistry2
    if fieldType == 'biology':
        toolType = toolTypeBiology + toolTypeGeneric
        workType = workTypeGeneric + workTypeSTEM
        babblePrefix = babblePrefixGeneric + babblePrefixBiology
        babble1 = babbleGeneric1 + babbleBiology1
        babble2 = babbleGeneric2 + babbleBiology2
    if fieldType == 'history':
        workType = workTypeGeneric
        babblePrefix = babblePrefixGeneric + babblePrefixHistory
        babble1 = babbleGeneric1 + babbleHistory1
        babble2 = babbleGeneric2 + babbleHistory2
    if fieldType == 'economics':
        workType = workTypeGeneric
        babblePrefix = babblePrefixGeneric + babblePrefixEconomics
        babble1 = babbleGeneric1 + babbleEconomics1
        babble2 = babbleGeneric2 + babbleEconomics2
    if fieldType == 'sociology':
        workType = workTypeGeneric
        babblePrefix = babblePrefixGeneric + babblePrefixSociology
        babble1 = babbleGeneric1 + babbleSociology1
        babble2 = babbleGeneric2 + babbleSociology2

    # Randomly determining the title type
    # 1: type + babble prefix + babble
    # 2: type prefix + type + babble prefix + babble
    # 3: type prefix + type + babble
    # 4: address +  babble prefix + babble
    # 5: field + of + babble prefix + babble
    # 6: type + babble1 + babble prefix + babble
    # 7: tool + work type + babble
    if fieldType == 'physics' or fieldType == 'chemistry' or fieldType == 'biology':
        titleType = random.randint(1,7)
    else:
        titleType = random.randint(1,5)

    # Build title depending on random result
    if titleType == 1:
        workTitle = (random.choice(workType)).title() + " of " + random.choice(babblePrefix).title() + " " + (random.choice(babble1)+random.choice(babble2)).title()
    elif titleType == 2:
        workTitle = (random.choice(optionalWorkPrefix) + " " + random.choice(workType)).title() + " of " + random.choice(babblePrefix).title() + " " + (random.choice(babble1)+random.choice(babble2)).title()
    elif titleType == 3:
        workTitle = (random.choice(optionalWorkPrefix) + " " + random.choice(workType)).title() + " of " + (random.choice(babble1)+random.choice(babble2)).title()
    elif titleType == 4:
        workTitle = (random.choice(addressWork) + " " + random.choice(babblePrefix) + " " + random.choice(babble1) + random.choice(babble2)).title()
    elif titleType == 5:
        workTitle = fieldType.title() + " of " + (random.choice(babblePrefix) + " " + random.choice(babble1) + random.choice(\
babble2)).title()
    elif titleType == 6:
        workTitle = (random.choice(workType)).title() + " of " + (random.choice(babble1) + random.choice(babblePrefix) + " " + random.choice(babble2)).title()
    elif titleType == 7:
        workTitle = (random.choice(toolType) + " " + random.choice(toolReport)).title() + " of " + (random.choice(babblePrefix) + " " + random.choice(babble2)).title()

    # Print title
    fullTitle = workTitle + " (" + fieldType.title() + ")"
    print(fullTitle)

print("\nDone")
