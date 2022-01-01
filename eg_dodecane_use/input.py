# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'], 
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

# Constraints on generated species
generatedSpeciesConstraints(
    maximumCarbonAtoms = 12,
)

# List of species
species(
    label='n-dodecane',
    structure=SMILES("CCCCCCCCCCCC"),
)

species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]"),
)


simpleReactor(
    temperature=(1600,'K'),
    pressure=(400,'Pa'),
    initialMoleFractions={
        "n-dodecane": 0.02,
        "Ar": 0.98,
    },
    terminationConversion={
        'n-dodecane': 0.90,
    },
    terminationTime=(1e6,'s'),
)


simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000,
    filterReactions=True,
)


options(
    units='si',
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=False,
    saveSimulationProfiles=True,
)
