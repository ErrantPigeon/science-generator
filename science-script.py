#!/usr/bin/env python3

# need this to generate randomness
import random

# defining the text lists

# list of scientific fields
fieldList = ['physics', 'biology', 'chemistry',
             'economics', 'history', 'sociology',
             'mathematics']

# list of journals
journalList = ["Journal of {}", "{} Review Letters", "Annals of {}",
               "Modern {}", "Review of {}", "{} Direct",
               "{} Chronicle", "{} Today", "Society of {}",
               "Contemporary {}", "{} Communications", "Applied {}",
               "{} Gazette", "Journal of Recent {}", "Applied {} Review",
               "Developments in {}", "Review of Recent {}", "{} Today"]

# list of months
monthList = ['Jan', 'Feb', 'Mar',
             'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep',
             'Oct', 'Nov', 'Dec']

# list of article types
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

# list of measurement tools and reports types
toolTypeGeneric = ['laboratory', 'tabletop', 'field']
toolTypePhysics = ['collider', 'accelerator', 'passive']
toolTypeChemistry = ['spectrographic', 'X-ray', 'laser']
toolTypeBiology = ['chemical', 'bioreactor', 'microscope']

toolReport = ['scan', 'probe', 'experiment',
              'study', 'measurement', 'imaging']

# other ways to address the study
addressWork = ['on', 'about', 'concerning',
               'regarding', 'reevaluating', 'addressing']

# broken down by fields for better lists
# prefix = adjectives
babblePrefixGeneric = ['repeated', 'rare', 'unique',
                       'common', 'induced', 'hypothetical',
                       'dual', 'deep', 'networked',
                       'recursive', 'layered', 'recurring',
                       'singular', 'structured', 'embedded',
                       'regular', 'artificial', 'monadic',
                       'speculative', 'convoluted', 'inferred',
                       'fabricated', 'inhibited', 'hidden',
                       'algorithmic', 'observable', 'additive',
                       'parallel', 'adversarial', 'stochastic',
                       'statistical', 'stable', 'critical',
                       'fragile', 'generative', 'dominant',
                       'material', 'affected', 'static',
                       'decayed', 'inverted', 'latent',
                       'fundamental', 'ambient', 'cyclic',
                       'recurring', 'aligned', 'separated',
                       'ordered', 'universal', 'restricted',
                       'recent', 'effective', 'apparent',
                       'balanced', 'specific', 'connected']

babblePrefixPhysics = ['massive', 'manifold', 'light',
                       'accelerated', 'subtractive', 'weak',
                       'strong', 'scalar', 'nuclear',
                       'commutating', 'bayesian', 'cosmic',
                       'degenerate', 'strange', 'symmetric',
                       'fractal', 'vectorised', 'generalised',
                       'gravitational', 'elastic', 'radiative',
                       'warped', 'energetic', 'kinematic' ]

babblePrefixBiology = ['viral', 'endemic', 'pathological',
                       'genetic', 'soluable', 'expressive',
                       'mutable', 'sequenced', 'methylated',
                       'dense', 'bacterial', 'cellular',
                       'soluable', 'suspended', 'emulsified',
                       'sustained', 'clinical', 'cultivated',
                       'living', 'vitrified', 'calcified',
                       'active', 'activated', 'tubular']

babblePrefixChemistry = ['soluable', 'suspended', 'emulsified',
                         'crystalline', 'planar', 'manifold',
                         'massive', 'light', 'symmetric',
                         'asymmetric', 'dissolved', 'fractional',
                         'bonded','computational','plastic',
                         'sustained', 'sublimated', 'vaporised',
                         'aerolised', 'frozen', 'molten',
                         'metallic', 'lathanic', 'pulverised']

babblePrefixHistory = ['medieval','european','political',
                       'national', 'global', 'local',
                       'important', 'far-reaching', 'memorial',
                       'falsified', 'verified', 'sourced',
                       'memetic', 'classical', 'ancient',
                       'sourced', 'reported', 'documented',
                       'military', 'civilian', 'recorded',
                       'coastal', 'urban', 'forgotten',
                       'pivotal', 'crucial', 'essential']

babblePrefixEconomics = ['national', 'global', 'local',
                         'fungible', 'political', 'digital',
                         'motivated', 'technical', 'visionary',
                         'sustainable', 'ethical', 'fake',
                         'memetic', 'volatile', 'predictive',
                         'trusted', 'optimal', 'leveraged',
                         'valuable', 'essential', 'key']

babblePrefixSociology = ['national', 'global', 'local',
                         'social', 'compelled', 'deliberate',
                         'political', 'fake', 'ethical',
                         'accidental', 'predictable', 'formative',
                         'memetic', 'economic', 'testable',
                         'academic', 'distributed', 'normative',
                         'developmental', 'normalised', 'creative']

babblePrefixMathematics = ['manifold', 'subtractive',
                           'geometric', 'distributed', 'factorised',
                           'commutating', 'bayesian', 'frequentist',
                           'hyperbolic', 'symmetric', 'orthogonal'
                           'fractal', 'normal', 'generalised',
                           'Gaussian', 'Laplacian', 'Riemannian',
                           'Lorentzian', 'Abelian', 'axiomatic',
                           'complex', 'finite', 'null',
                           'chaotic', 'linear', 'quadratic',
                           'higher-order', 'approximate', 'quantised',
                           'integrated', 'derivative', 'affine',
                           'random', 'functional', 'computable',
                           'warped', 'curved', 'linearised']

# first part of the noun (some sort of prefix)
babbleGeneric1 = ['meta', 'super', 'inter',
                  'omni', 'intra', 'ultra',
                  'proto', 'anti', 'hyper',
                  'un', 'mono', 'pre',
                  'poly', 'multi',
                  'co-', 'sub', 'endo',
                  'macro', 'nano',
                  'micro', 'exo', 'para',
                  'homo', 'trans', 'quasi']

babblePhysics1 = ['uni', 'radio', 'quantum ',
                  'bulk ', 'phase ', 'tensor',
                  'block ', 'cross', 'n-',
                  'z-', 's-', 'r-',
                  'holo', 'chromo', 'electro']

babbleChemistry1 = ['cryo', 'radio', 'quantum ',
                    'bulk ', 'phase ', 'hydro',
                    'nitro', 'sodium', 'n-',
                    'geo', 'litho', 'lipo']

babbleBiology1 = ['cardio', 'neuro', 'sucra',
                  'angio', 'immuno', 'oleo',
                  'myo', 'amino', 'pheno',
                  'bio', 'phyto', 'meso']

babbleHistory1 = ['war ', 'peace ', 'land ',
                  'ocean ', 'meso', 'post',
                  'state ', 'imperial ', 'royal ',
                  'forest ', 'desert ', 'city ']

babbleEconomics1 = ['socio', 'cyber', 'eco',
                    'neo', 'geo', 'market ',
                    'block-', 'cross', 'post']

babbleSociology1 = ['socio','cyber', 'eco',
                    'neo', 'retro', 'ethno',
                    'block-', 'cross', 'post']

babbleMathematics1 = ['ρ-','σ-','α-',
                      'bulk ', 'phase ', 'φ-',
                      'block ', 'ortho', 'n-',
                      'z-', 's-', 'r-',
                      'λ-', 'crypto', 'pseudo',
                      'holo', 'denso', 'chromo']

# second part of the noun
babbleGeneric2 = ['dimensions', 'points',
                  'sequences', 'devices', 'mappings',
                  'types', 'chains', 'potentials',
                  'clusters', 'actions', 'buffers',
                  'reactions', 'processes', 'patterns']

babblePhysics2 = ['particles', 'emissions', 'projections',
                  'calculations', 'cavitations', 'conductors',
                  'trajectories', 'arrays', 'cascades',
                  'bosons', 'leptons', 'hadrons',
                  'mesons', 'poles', 'quarks',
                  'rings', 'events', 'fluids',
                  'matter', 'lattices', 'remnants',
                  'surfaces', 'excitations', 'topologies',
                  'resonances', 'coefficients', 'oscillations',
                  'plasmas', 'condensates', 'states',
                  'collisions', 'impacts', 'amplitudes',
                  'dynamics', 'spectra', 'violations']

babbleChemistry2 = ['structures', 'chlorates', 'formations',
                    'rings', 'oxides', 'solvents',
                    'lubricants', 'depositions', 'growths',
                    'fluids', 'phosphates' , 'conductors',
                    'calculations', 'carbons', 'magnets',
                    'ferrites', 'solids', 'bonds',
                    'films', 'chlorides', 'fluids',
                    'filters', 'excitations', 'surfaces',
                    'resonances', 'coefficients', 'minerals',
                    'phthalates', 'glasses', 'gases',
                    'aromatics', 'solutions', 'emulsions']

babbleBiology2 = ['structures', 'rhizomes', 'formations',
                  'rings', 'oxides', 'solvents',
                  'secretions', 'depositions', 'growths',
                  'fluids', 'cavitations' , 'matrices',
                  'plasmids', 'cascades', 'ribosomes',
                  'peptides', 'solids', 'bonds',
                  'fluids', 'lattices', 'films',
                  'coefficients', 'cultures', 'scaffolds',
                  'signalling', 'saccharids', 'acids',
                  'compounds', 'toxins', 'proteins',
                  'pathways', 'organelles', 'glands']

babbleHistory2 = ['settlements', 'narratives', 'timelines',
                  'aggressions', 'trends', 'events',
                  'conflicts', 'populations', 'excavations',
                  'histories', 'protests', 'migrations',
                  'remnants', 'ruins', 'artifacts',
                  'cultures', 'societies', 'civilisations',
                  'communes', 'locations', 'museums']

babbleEconomics2 = ['investments', 'narratives', 'timelines',
                    'fluctuations', 'trends', 'predictions',
                    'events', 'populations', 'crashes',
                    'histories', 'collapses', 'movements',
                    'indicators', 'signals', 'warnings',
                    'funds', 'accounts', 'treasuries']

babbleSociology2 = ['media', 'narratives', 'timelines',
                    'fluctuations', 'trends', 'assignations',
                    'teachings', 'populations', 'linguistics',
                    'histories', 'modernism', 'movements',
                    'cultures', 'societies', 'identities',
                    'journalism', 'events', 'messaging']

babbleMathematics2 = ['metrics', 'manifolds', 'toplogies',
                      'projections', 'algebras', 'relationships',
                      'connections', 'tensors', 'vectors',
                      'scalars', 'numbers', 'primes',
                      'tuples', 'orders', 'infinities',
                      'calculus', 'integrals', 'sets']

# Loop to make several of these...
for x in range(0, 20):

    # Decide scientific field
    fieldType = random.choice(fieldList)

    # Use this to create the appropriate pools to draw from
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
    if fieldType == 'mathematics':
        workType = workTypeGeneric
        babblePrefix = babblePrefixGeneric + babblePrefixMathematics
        babble1 = babbleGeneric1 + babbleMathematics1
        babble2 = babbleGeneric2 + babbleMathematics2

    # Randomly determining the title type
    # 1: type + babble prefix + babble
    # 2: type prefix + type + babble prefix + babble
    # 3: type prefix + type + babble
    # 4: address +  babble prefix + babble
    # 5: field + of + babble prefix + babble
    # 6: type + babble1 + babble prefix + babble
    # 7: tool + work type + babble
    if fieldType == 'physics' or fieldType == 'chemistry' or fieldType == 'biology':
        titleType = random.randint(1,8)
    else:
        titleType = random.randint(1,5)

    # Build title depending on random result
    if titleType == 1:
        workTitle = ((random.choice(workType)).title() +
                     " of " + random.choice(babblePrefix).title() +
                     " " + (random.choice(babble1) + random.choice(babble2)).title())
    elif titleType == 2:
        workTitle = ((random.choice(optionalWorkPrefix) + " " + random.choice(workType)).title() +
                     " of " + random.choice(babblePrefix).title() +
                     " " + (random.choice(babble1)+random.choice(babble2)).title())
    elif titleType == 3:
        workTitle = ((random.choice(optionalWorkPrefix) + " " + random.choice(workType)).title() +
                     " of " + (random.choice(babble1)+random.choice(babble2)).title())
    elif titleType == 4:
        workTitle = ((random.choice(addressWork) +
                      " " + random.choice(babblePrefix) + " "
                      + random.choice(babble1) + random.choice(babble2)).title())
    elif titleType == 5:
        workTitle = (fieldType.title() +
                     " of " + (random.choice(babblePrefix) +
                     " " + random.choice(babble1) + random.choice(babble2)).title())
    elif titleType == 6:
        workTitle = ((random.choice(workType)).title() +
                     " of " + (random.choice(babble1) + random.choice(babblePrefix) +
                     " " + random.choice(babble2)).title())
    elif titleType == 7:
        workTitle = ((random.choice(toolType) + " " + random.choice(toolReport)).title() +
                     " of " + (random.choice(babble1) + random.choice(babble2)).title())
    elif titleType == 8:
        workTitle = ((random.choice(toolType) + " " + random.choice(toolReport)).title() +
                     " of " + (random.choice(babblePrefix) +
                     " " + random.choice(babble1) + random.choice(babble2)).title())

    #generate journal
    journalTitle = (random.choice(journalList)).format(fieldType).title()
    journalPage = str(random.randint(8,400))
    journalDate = "({} {})".format(random.choice(monthList).title(), str(random.randint(1991,2017)))

    # Print title
    fullTitle = "[{}] {}. {}, pg. {} {}.".format(x, workTitle, journalTitle, journalPage, journalDate)
    print(fullTitle)

print("\nDone")
