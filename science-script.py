#!/usr/bin/python

# need this to generate randomness
import random

# defining the text lists
workType = ['study', 'trial', 'test',
            'determination', 'proof', 'simulation',
            'report', 'overview', 'theory',
            'analysis', 'summary', 'review',
            'survey', 'investigation', 'comparison',
            'computation', 'model', 'Monte Carlo',
            'foundations', 'technical note', 'document']
optionalWorkPrefix = ['follow-up', 'preliminary', 'improved',
                      'initial', 'first', 'complete',
                      'comprehensive', 'interim', 'concept',
                      'proposed', 'empirical', 'internal',
                      'novel', 'new', 'inductive',
                      'in-depth', 'final', 'revised']
addressWork = ['on', 'about', 'concerning',
               'regarding', 'reevaluating', 'addressing']
babblePrefix = ['massive', 'fine', 'historic',
                'repeated', 'rare', 'unique',
                'common', 'induced', 'hypothetical',
                'manifold', 'vectorised', 'generalised',
                'dual', 'deep', 'light',
                'convolved', 'networked', 'recursive',
                'layered', 'recurring', 'singular',
                'crystalline', 'structured', 'embedded',
                'warped', 'fake', 'artificial',
                'monadic', 'speculative', 'trusted',
                'convoluted', 'fabricated', 'accelerated',
                'retarded', 'inhibited', 'hidden',
                'nuclear', 'algorithmic', 'expressive',
                'market', 'observable', 'transducive',
                'ablative', 'additive', 'subtractive',
                'commutating', 'parallel', 'orthogonal',
                'national', 'global', 'local',
                'soluable', 'suspended', 'emulsified',
                'adversarial', 'bayesian', 'frequentist',
                'stochastic', 'statistical', 'organic',
                'scalar', 'stable', 'critical',
                'ethical', 'sustainable', 'fragile',
                'generative', 'degenerate', 'planar',
                'luminal', 'temporal', 'material',
                'electronic', 'static', 'mutable',
                'genetic', 'soluable', 'moving',
                'symmetric', 'fractal', 'inverted',
                'viral', 'endemic', 'pathological',
                'memetic', 'latent', 'fundamental',
                'weak', 'strong', 'ambient',
                'cyclic', 'recurring', 'aligned',
                'decimal', 'analogue', 'digital',
                'ordered', 'universal', 'restricted']
babble1 = ['meta', 'super', 'inter',
           'uni', 'intra', 'ultra',
           'proto', 'post', 'anti',
           'hyper', 'neuro', 'z-',
           'un', 'radio', 'cryo',
           'mono', 'n-', 'tensor',
           'eco', 'pre', 'neo',
           'poly', 'cardio', 'p-',
           'multi', 'co-', 'cross-',
           'socio', 'sub', 'endo',
           'cyber', 'hydro', 'quantum ',
           'macro', 'nano', 'micro',
           'bulk ', 'block-', 'exo',
           'phase ', 'para', 's-']
babble2 = ['particles', 'emissions', 'magnets',
           'growths', 'cultures', 'calculations',
           'topologies', 'media', 'histories',
           'cavitations', 'conductors', 'war events',
           'excitations', 'oscillations', 'resonances',
           'coefficients', 'peace histories', 'dimensions',
           'matter', 'surfaces', 'lattices',
           'trajectories', 'timelines', 'sources',
           'narratives', 'economies', 'projections',
           'conflicts', 'collisions', 'devices',
           'mappings', 'depositions', 'movements',
           'grids', 'fluids', 'arrays',
           'solvents', 'lubricants', 'solids',
           'peptides', 'oxides', 'chains',
           'potentials', 'aggressions', 'trends',
           'rhizomes', 'cells', 'clusters',
           'actions', 'buffers', 'reactions',
           'probes', 'processes', 'cascades',
           'bosons', 'leptons', 'hadrons',
           'mesons', 'poles', 'spaces',
           'rings', 'films', 'screens',
           'filters', 'remnants', 'quarks',
           'formations', 'structures', 'imprints']

# Loop to make several of these...
for x in range(0, 15):

    # Randomly determining the title type
    # 1: type + babble prefix + babble
    # 2: type prefix + type + babble prefix + babble
    # 3: type prefix + type + babble
    # 4: type + babble1 + babble prefix + babble
    # 5: address +  babble prefix + babble
    titleType = random.randint(1,5)
    
    # Build title depending on random result
    if titleType == 1:
        workTitle = (random.choice(workType)).title() + " of " + random.choice(babblePrefix).title() + " " + (random.choice(babble1)+random.choice(babble2)).title()
    elif titleType == 2:
        workTitle = (random.choice(optionalWorkPrefix) + ' ' + random.choice(workType)).title() + " of " + random.choice(babblePrefix).title() + " " + (random.choice(babble1)+random.choice(babble2)).title()
    elif titleType == 3:
        workTitle = (random.choice(optionalWorkPrefix) + " " + random.choice(workType)).title() + " of " + (random.choice(babble1)+random.choice(babble2)).title()
    elif titleType == 4:
        workTitle = (random.choice(workType)).title() + " of " + (random.choice(babble1) + random.choice(babblePrefix) + " " + random.choice(babble2)).title()
    elif titleType == 5:
        workTitle = (random.choice(addressWork) + " " + random.choice(babblePrefix) + " " + random.choice(babble1) + random.choice(babble2)).title()
        
    # Print title
    print(workTitle)

print("\nDone")
