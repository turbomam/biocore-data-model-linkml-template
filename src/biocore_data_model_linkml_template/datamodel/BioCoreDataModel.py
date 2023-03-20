# Auto generated from BioCoreDataModel.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-20T09:56:04
# Schema: biocore
#
# id: https://datamodel.terra.bio
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOCORE = CurieNamespace('BioCore', 'https://datamodel.terra.bio/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
DEFAULT_ = BIOCORE


# Types

# Class references



class VocabularyEncodingScheme(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://purl.org/dc/dcam/VocabularyEncodingScheme")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VocabularyEncodingScheme"
    class_model_uri: ClassVar[URIRef] = BIOCORE.VocabularyEncodingScheme


class Service(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://purl.org/dc/dcmitype/Service")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Service"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Service


class List(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.List
    class_class_curie: ClassVar[str] = "rdf:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = BIOCORE.List


class Class(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS.Class
    class_class_curie: ClassVar[str] = "rdfs:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Class


class Resource(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS.Resource
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Resource


class Kind(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://www.w3.org/2006/vcard/ns#Kind")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Kind"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Kind


class Document(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF.Document
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Document


class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF.Person
    class_class_curie: ClassVar[str] = "foaf:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Person


@dataclass
class SingleCell(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOCORE["TerraCore#SingleCell"]
    class_class_curie: ClassVar[str] = "BioCore:TerraCore#SingleCell"
    class_name: ClassVar[str] = "SingleCell"
    class_model_uri: ClassVar[URIRef] = BIOCORE.SingleCell

    hasCellCycle: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.hasCellCycle, list):
            self.hasCellCycle = [self.hasCellCycle] if self.hasCellCycle is not None else []
        self.hasCellCycle = [v if isinstance(v, str) else str(v) for v in self.hasCellCycle]

        super().__post_init__(**kwargs)


class Activity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOCORE["TerraCore#Activity"]
    class_class_curie: ClassVar[str] = "BioCore:TerraCore#Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Activity


class Donor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOCORE["TerraCore#Donor"]
    class_class_curie: ClassVar[str] = "BioCore:TerraCore#Donor"
    class_name: ClassVar[str] = "Donor"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Donor


class Sample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOCORE["TerraCore#Sample"]
    class_class_curie: ClassVar[str] = "BioCore:TerraCore#Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = BIOCORE.Sample


# Enumerations


# Slots
class slots:
    pass

slots.closeMatch = Slot(uri=SKOS.closeMatch, name="closeMatch", curie=SKOS.curie('closeMatch'),
                   model_uri=BIOCORE.closeMatch, domain=None, range=Optional[Union[str, List[str]]])

slots.wasGeneratedBy = Slot(uri=BIOCORE.wasGeneratedBy, name="wasGeneratedBy", curie=BIOCORE.curie('wasGeneratedBy'),
                   model_uri=BIOCORE.wasGeneratedBy, domain=None, range=Optional[str])

slots.used = Slot(uri=BIOCORE.used, name="used", curie=BIOCORE.curie('used'),
                   model_uri=BIOCORE.used, domain=None, range=Optional[str])

slots.format = Slot(uri=BIOCORE.format, name="format", curie=BIOCORE.curie('format'),
                   model_uri=BIOCORE.format, domain=None, range=Optional[str])

slots.member = Slot(uri=RDFS.member, name="member", curie=RDFS.curie('member'),
                   model_uri=BIOCORE.member, domain=None, range=Optional[Union[str, List[str]]])

slots.wasUsedBy = Slot(uri=PROV.wasUsedBy, name="wasUsedBy", curie=PROV.curie('wasUsedBy'),
                   model_uri=BIOCORE.wasUsedBy, domain=None, range=Optional[Union[str, List[str]]])

slots.confirmsDisease = Slot(uri=BIOCORE['TerraCore#confirmsDisease'], name="confirmsDisease", curie=BIOCORE.curie('TerraCore#confirmsDisease'),
                   model_uri=BIOCORE.confirmsDisease, domain=None, range=Optional[Union[str, List[str]]])

slots.donated = Slot(uri=BIOCORE['TerraCore#donated'], name="donated", curie=BIOCORE.curie('TerraCore#donated'),
                   model_uri=BIOCORE.donated, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAge = Slot(uri=BIOCORE['TerraCore#hasAge'], name="hasAge", curie=BIOCORE.curie('TerraCore#hasAge'),
                   model_uri=BIOCORE.hasAge, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAgeAtDeath = Slot(uri=BIOCORE['TerraCore#hasAgeAtDeath'], name="hasAgeAtDeath", curie=BIOCORE.curie('TerraCore#hasAgeAtDeath'),
                   model_uri=BIOCORE.hasAgeAtDeath, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAgeAtDiagnosis = Slot(uri=BIOCORE['TerraCore#hasAgeAtDiagnosis'], name="hasAgeAtDiagnosis", curie=BIOCORE.curie('TerraCore#hasAgeAtDiagnosis'),
                   model_uri=BIOCORE.hasAgeAtDiagnosis, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAgeAtOnset = Slot(uri=BIOCORE['TerraCore#hasAgeAtOnset'], name="hasAgeAtOnset", curie=BIOCORE.curie('TerraCore#hasAgeAtOnset'),
                   model_uri=BIOCORE.hasAgeAtOnset, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAprioriCellType = Slot(uri=BIOCORE['TerraCore#hasAprioriCellType'], name="hasAprioriCellType", curie=BIOCORE.curie('TerraCore#hasAprioriCellType'),
                   model_uri=BIOCORE.hasAprioriCellType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAssayActivity = Slot(uri=BIOCORE['TerraCore#hasAssayActivity'], name="hasAssayActivity", curie=BIOCORE.curie('TerraCore#hasAssayActivity'),
                   model_uri=BIOCORE.hasAssayActivity, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAssayType = Slot(uri=BIOCORE['TerraCore#hasAssayType'], name="hasAssayType", curie=BIOCORE.curie('TerraCore#hasAssayType'),
                   model_uri=BIOCORE.hasAssayType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasBioSample = Slot(uri=BIOCORE['TerraCore#hasBioSample'], name="hasBioSample", curie=BIOCORE.curie('TerraCore#hasBioSample'),
                   model_uri=BIOCORE.hasBioSample, domain=None, range=Optional[Union[str, List[str]]])

slots.hasBioSampleType = Slot(uri=BIOCORE['TerraCore#hasBioSampleType'], name="hasBioSampleType", curie=BIOCORE.curie('TerraCore#hasBioSampleType'),
                   model_uri=BIOCORE.hasBioSampleType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasChild = Slot(uri=BIOCORE['TerraCore#hasChild'], name="hasChild", curie=BIOCORE.curie('TerraCore#hasChild'),
                   model_uri=BIOCORE.hasChild, domain=None, range=Optional[Union[str, List[str]]])

slots.hasCountry = Slot(uri=BIOCORE['TerraCore#hasCountry'], name="hasCountry", curie=BIOCORE.curie('TerraCore#hasCountry'),
                   model_uri=BIOCORE.hasCountry, domain=None, range=Optional[Union[str, List[str]]])

slots.hasCrossReference = Slot(uri=BIOCORE['TerraCore#hasCrossReference'], name="hasCrossReference", curie=BIOCORE.curie('TerraCore#hasCrossReference'),
                   model_uri=BIOCORE.hasCrossReference, domain=None, range=Optional[Union[str, List[str]]])

slots.hasCurrentAddress = Slot(uri=BIOCORE['TerraCore#hasCurrentAddress'], name="hasCurrentAddress", curie=BIOCORE.curie('TerraCore#hasCurrentAddress'),
                   model_uri=BIOCORE.hasCurrentAddress, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDataModality = Slot(uri=BIOCORE['TerraCore#hasDataModality'], name="hasDataModality", curie=BIOCORE.curie('TerraCore#hasDataModality'),
                   model_uri=BIOCORE.hasDataModality, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDiagnosis = Slot(uri=BIOCORE['TerraCore#hasDiagnosis'], name="hasDiagnosis", curie=BIOCORE.curie('TerraCore#hasDiagnosis'),
                   model_uri=BIOCORE.hasDiagnosis, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDonor = Slot(uri=BIOCORE['TerraCore#hasDonor'], name="hasDonor", curie=BIOCORE.curie('TerraCore#hasDonor'),
                   model_uri=BIOCORE.hasDonor, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDonorAgeAtCollection = Slot(uri=BIOCORE['TerraCore#hasDonorAgeAtCollection'], name="hasDonorAgeAtCollection", curie=BIOCORE.curie('TerraCore#hasDonorAgeAtCollection'),
                   model_uri=BIOCORE.hasDonorAgeAtCollection, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDonorAgeAtEvent = Slot(uri=BIOCORE['TerraCore#hasDonorAgeAtEvent'], name="hasDonorAgeAtEvent", curie=BIOCORE.curie('TerraCore#hasDonorAgeAtEvent'),
                   model_uri=BIOCORE.hasDonorAgeAtEvent, domain=None, range=Optional[Union[str, List[str]]])

slots.hasFileSize = Slot(uri=BIOCORE['TerraCore#hasFileSize'], name="hasFileSize", curie=BIOCORE.curie('TerraCore#hasFileSize'),
                   model_uri=BIOCORE.hasFileSize, domain=None, range=Optional[Union[str, List[str]]])

slots.hasHalfSibling = Slot(uri=BIOCORE['TerraCore#hasHalfSibling'], name="hasHalfSibling", curie=BIOCORE.curie('TerraCore#hasHalfSibling'),
                   model_uri=BIOCORE.hasHalfSibling, domain=None, range=Optional[Union[str, List[str]]])

slots.hasLibraryPrepActivity = Slot(uri=BIOCORE['TerraCore#hasLibraryPrepActivity'], name="hasLibraryPrepActivity", curie=BIOCORE.curie('TerraCore#hasLibraryPrepActivity'),
                   model_uri=BIOCORE.hasLibraryPrepActivity, domain=None, range=Optional[Union[str, List[str]]])

slots.hasLibraryPreparationType = Slot(uri=BIOCORE['TerraCore#hasLibraryPreparationType'], name="hasLibraryPreparationType", curie=BIOCORE.curie('TerraCore#hasLibraryPreparationType'),
                   model_uri=BIOCORE.hasLibraryPreparationType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasMeasurement = Slot(uri=BIOCORE['TerraCore#hasMeasurement'], name="hasMeasurement", curie=BIOCORE.curie('TerraCore#hasMeasurement'),
                   model_uri=BIOCORE.hasMeasurement, domain=None, range=Optional[Union[str, List[str]]])

slots.hasMolecularSampleType = Slot(uri=BIOCORE['TerraCore#hasMolecularSampleType'], name="hasMolecularSampleType", curie=BIOCORE.curie('TerraCore#hasMolecularSampleType'),
                   model_uri=BIOCORE.hasMolecularSampleType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasParent = Slot(uri=BIOCORE['TerraCore#hasParent'], name="hasParent", curie=BIOCORE.curie('TerraCore#hasParent'),
                   model_uri=BIOCORE.hasParent, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPhenopacket = Slot(uri=BIOCORE['TerraCore#hasPhenopacket'], name="hasPhenopacket", curie=BIOCORE.curie('TerraCore#hasPhenopacket'),
                   model_uri=BIOCORE.hasPhenopacket, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPhenotypicSex = Slot(uri=BIOCORE['TerraCore#hasPhenotypicSex'], name="hasPhenotypicSex", curie=BIOCORE.curie('TerraCore#hasPhenotypicSex'),
                   model_uri=BIOCORE.hasPhenotypicSex, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSampleTreatment = Slot(uri=BIOCORE['TerraCore#hasSampleTreatment'], name="hasSampleTreatment", curie=BIOCORE.curie('TerraCore#hasSampleTreatment'),
                   model_uri=BIOCORE.hasSampleTreatment, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSequenceLocation = Slot(uri=BIOCORE['TerraCore#hasSequenceLocation'], name="hasSequenceLocation", curie=BIOCORE.curie('TerraCore#hasSequenceLocation'),
                   model_uri=BIOCORE.hasSequenceLocation, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSequencingActivity = Slot(uri=BIOCORE['TerraCore#hasSequencingActivity'], name="hasSequencingActivity", curie=BIOCORE.curie('TerraCore#hasSequencingActivity'),
                   model_uri=BIOCORE.hasSequencingActivity, domain=None, range=Optional[Union[str, List[str]]])

slots.hasServiceProvider = Slot(uri=BIOCORE['TerraCore#hasServiceProvider'], name="hasServiceProvider", curie=BIOCORE.curie('TerraCore#hasServiceProvider'),
                   model_uri=BIOCORE.hasServiceProvider, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSexAssignedAtBirth = Slot(uri=BIOCORE['TerraCore#hasSexAssignedAtBirth'], name="hasSexAssignedAtBirth", curie=BIOCORE.curie('TerraCore#hasSexAssignedAtBirth'),
                   model_uri=BIOCORE.hasSexAssignedAtBirth, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSibling = Slot(uri=BIOCORE['TerraCore#hasSibling'], name="hasSibling", curie=BIOCORE.curie('TerraCore#hasSibling'),
                   model_uri=BIOCORE.hasSibling, domain=None, range=Optional[Union[str, List[str]]])

slots.hasTreatment = Slot(uri=BIOCORE['TerraCore#hasTreatment'], name="hasTreatment", curie=BIOCORE.curie('TerraCore#hasTreatment'),
                   model_uri=BIOCORE.hasTreatment, domain=None, range=Optional[Union[str, List[str]]])

slots.hasVariantCall = Slot(uri=BIOCORE['TerraCore#hasVariantCall'], name="hasVariantCall", curie=BIOCORE.curie('TerraCore#hasVariantCall'),
                   model_uri=BIOCORE.hasVariantCall, domain=None, range=Optional[Union[str, List[str]]])

slots.hasWeight = Slot(uri=BIOCORE['TerraCore#hasWeight'], name="hasWeight", curie=BIOCORE.curie('TerraCore#hasWeight'),
                   model_uri=BIOCORE.hasWeight, domain=None, range=Optional[Union[str, List[str]]])

slots.isFundedBy = Slot(uri=BIOCORE['TerraCore#isFundedBy'], name="isFundedBy", curie=BIOCORE.curie('TerraCore#isFundedBy'),
                   model_uri=BIOCORE.isFundedBy, domain=None, range=Optional[Union[str, List[str]]])

slots.isGeneratedByPipeline = Slot(uri=BIOCORE['TerraCore#isGeneratedByPipeline'], name="isGeneratedByPipeline", curie=BIOCORE.curie('TerraCore#isGeneratedByPipeline'),
                   model_uri=BIOCORE.isGeneratedByPipeline, domain=None, range=Optional[Union[str, List[str]]])

slots.isPairedWith = Slot(uri=BIOCORE['TerraCore#isPairedWith'], name="isPairedWith", curie=BIOCORE.curie('TerraCore#isPairedWith'),
                   model_uri=BIOCORE.isPairedWith, domain=None, range=Optional[Union[str, List[str]]])

slots.usesAntibody = Slot(uri=BIOCORE['TerraCore#usesAntibody'], name="usesAntibody", curie=BIOCORE.curie('TerraCore#usesAntibody'),
                   model_uri=BIOCORE.usesAntibody, domain=None, range=Optional[Union[str, List[str]]])

slots.usesLibrary = Slot(uri=BIOCORE['TerraCore#usesLibrary'], name="usesLibrary", curie=BIOCORE.curie('TerraCore#usesLibrary'),
                   model_uri=BIOCORE.usesLibrary, domain=None, range=Optional[Union[str, List[str]]])

slots.usesReferenceAssembly = Slot(uri=BIOCORE['TerraCore#usesReferenceAssembly'], name="usesReferenceAssembly", curie=BIOCORE.curie('TerraCore#usesReferenceAssembly'),
                   model_uri=BIOCORE.usesReferenceAssembly, domain=None, range=Optional[Union[str, List[str]]])

slots.usesSample = Slot(uri=BIOCORE['TerraCore#usesSample'], name="usesSample", curie=BIOCORE.curie('TerraCore#usesSample'),
                   model_uri=BIOCORE.usesSample, domain=None, range=Optional[Union[str, List[str]]])

slots.hasActivityType = Slot(uri=BIOCORE['TerraCore#hasActivityType'], name="hasActivityType", curie=BIOCORE.curie('TerraCore#hasActivityType'),
                   model_uri=BIOCORE.hasActivityType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAgeCategory = Slot(uri=BIOCORE['TerraCore#hasAgeCategory'], name="hasAgeCategory", curie=BIOCORE.curie('TerraCore#hasAgeCategory'),
                   model_uri=BIOCORE.hasAgeCategory, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAgeUnit = Slot(uri=BIOCORE['TerraCore#hasAgeUnit'], name="hasAgeUnit", curie=BIOCORE.curie('TerraCore#hasAgeUnit'),
                   model_uri=BIOCORE.hasAgeUnit, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAlignedFragments = Slot(uri=BIOCORE['TerraCore#hasAlignedFragments'], name="hasAlignedFragments", curie=BIOCORE.curie('TerraCore#hasAlignedFragments'),
                   model_uri=BIOCORE.hasAlignedFragments, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAllele = Slot(uri=BIOCORE['TerraCore#hasAllele'], name="hasAllele", curie=BIOCORE.curie('TerraCore#hasAllele'),
                   model_uri=BIOCORE.hasAllele, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAmount = Slot(uri=BIOCORE['TerraCore#hasAmount'], name="hasAmount", curie=BIOCORE.curie('TerraCore#hasAmount'),
                   model_uri=BIOCORE.hasAmount, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAmountUnit = Slot(uri=BIOCORE['TerraCore#hasAmountUnit'], name="hasAmountUnit", curie=BIOCORE.curie('TerraCore#hasAmountUnit'),
                   model_uri=BIOCORE.hasAmountUnit, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAnatomicalRegion = Slot(uri=BIOCORE['TerraCore#hasAnatomicalRegion'], name="hasAnatomicalRegion", curie=BIOCORE.curie('TerraCore#hasAnatomicalRegion'),
                   model_uri=BIOCORE.hasAnatomicalRegion, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAnatomicalSite = Slot(uri=BIOCORE['TerraCore#hasAnatomicalSite'], name="hasAnatomicalSite", curie=BIOCORE.curie('TerraCore#hasAnatomicalSite'),
                   model_uri=BIOCORE.hasAnatomicalSite, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAverageReadLength = Slot(uri=BIOCORE['TerraCore#hasAverageReadLength'], name="hasAverageReadLength", curie=BIOCORE.curie('TerraCore#hasAverageReadLength'),
                   model_uri=BIOCORE.hasAverageReadLength, domain=None, range=Optional[Union[str, List[str]]])

slots.hasBirthYear = Slot(uri=BIOCORE['TerraCore#hasBirthYear'], name="hasBirthYear", curie=BIOCORE.curie('TerraCore#hasBirthYear'),
                   model_uri=BIOCORE.hasBirthYear, domain=None, range=Optional[Union[str, List[str]]])

slots.hasCellCycle = Slot(uri=BIOCORE['TerraCore#hasCellCycle'], name="hasCellCycle", curie=BIOCORE.curie('TerraCore#hasCellCycle'),
                   model_uri=BIOCORE.hasCellCycle, domain=None, range=Optional[Union[str, List[str]]])

slots.hasCellState = Slot(uri=BIOCORE['TerraCore#hasCellState'], name="hasCellState", curie=BIOCORE.curie('TerraCore#hasCellState'),
                   model_uri=BIOCORE.hasCellState, domain=None, range=Optional[Union[str, List[str]]])

slots.hasChecksum = Slot(uri=BIOCORE['TerraCore#hasChecksum'], name="hasChecksum", curie=BIOCORE.curie('TerraCore#hasChecksum'),
                   model_uri=BIOCORE.hasChecksum, domain=None, range=Optional[Union[str, List[str]]])

slots.hasChromosome = Slot(uri=BIOCORE['TerraCore#hasChromosome'], name="hasChromosome", curie=BIOCORE.curie('TerraCore#hasChromosome'),
                   model_uri=BIOCORE.hasChromosome, domain=None, range=Optional[Union[str, List[str]]])

slots.hasClonality = Slot(uri=BIOCORE['TerraCore#hasClonality'], name="hasClonality", curie=BIOCORE.curie('TerraCore#hasClonality'),
                   model_uri=BIOCORE.hasClonality, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDateCollected = Slot(uri=BIOCORE['TerraCore#hasDateCollected'], name="hasDateCollected", curie=BIOCORE.curie('TerraCore#hasDateCollected'),
                   model_uri=BIOCORE.hasDateCollected, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDateOfBirth = Slot(uri=BIOCORE['TerraCore#hasDateOfBirth'], name="hasDateOfBirth", curie=BIOCORE.curie('TerraCore#hasDateOfBirth'),
                   model_uri=BIOCORE.hasDateOfBirth, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDateOfDeath = Slot(uri=BIOCORE['TerraCore#hasDateOfDeath'], name="hasDateOfDeath", curie=BIOCORE.curie('TerraCore#hasDateOfDeath'),
                   model_uri=BIOCORE.hasDateOfDeath, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDevelopmentalStage = Slot(uri=BIOCORE['TerraCore#hasDevelopmentalStage'], name="hasDevelopmentalStage", curie=BIOCORE.curie('TerraCore#hasDevelopmentalStage'),
                   model_uri=BIOCORE.hasDevelopmentalStage, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDisease = Slot(uri=BIOCORE['TerraCore#hasDisease'], name="hasDisease", curie=BIOCORE.curie('TerraCore#hasDisease'),
                   model_uri=BIOCORE.hasDisease, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDiseaseStageType = Slot(uri=BIOCORE['TerraCore#hasDiseaseStageType'], name="hasDiseaseStageType", curie=BIOCORE.curie('TerraCore#hasDiseaseStageType'),
                   model_uri=BIOCORE.hasDiseaseStageType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDiseaseStageValue = Slot(uri=BIOCORE['TerraCore#hasDiseaseStageValue'], name="hasDiseaseStageValue", curie=BIOCORE.curie('TerraCore#hasDiseaseStageValue'),
                   model_uri=BIOCORE.hasDiseaseStageValue, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDonorTreatmentType = Slot(uri=BIOCORE['TerraCore#hasDonorTreatmentType'], name="hasDonorTreatmentType", curie=BIOCORE.curie('TerraCore#hasDonorTreatmentType'),
                   model_uri=BIOCORE.hasDonorTreatmentType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDose = Slot(uri=BIOCORE['TerraCore#hasDose'], name="hasDose", curie=BIOCORE.curie('TerraCore#hasDose'),
                   model_uri=BIOCORE.hasDose, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDuplicateFragments = Slot(uri=BIOCORE['TerraCore#hasDuplicateFragments'], name="hasDuplicateFragments", curie=BIOCORE.curie('TerraCore#hasDuplicateFragments'),
                   model_uri=BIOCORE.hasDuplicateFragments, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDuration = Slot(uri=BIOCORE['TerraCore#hasDuration'], name="hasDuration", curie=BIOCORE.curie('TerraCore#hasDuration'),
                   model_uri=BIOCORE.hasDuration, domain=None, range=Optional[Union[str, List[str]]])

slots.hasDurationUnit = Slot(uri=BIOCORE['TerraCore#hasDurationUnit'], name="hasDurationUnit", curie=BIOCORE.curie('TerraCore#hasDurationUnit'),
                   model_uri=BIOCORE.hasDurationUnit, domain=None, range=Optional[Union[str, List[str]]])

slots.hasEstimatedLibrarySize = Slot(uri=BIOCORE['TerraCore#hasEstimatedLibrarySize'], name="hasEstimatedLibrarySize", curie=BIOCORE.curie('TerraCore#hasEstimatedLibrarySize'),
                   model_uri=BIOCORE.hasEstimatedLibrarySize, domain=None, range=Optional[Union[str, List[str]]])

slots.hasFamilyIdentifier = Slot(uri=BIOCORE['TerraCore#hasFamilyIdentifier'], name="hasFamilyIdentifier", curie=BIOCORE.curie('TerraCore#hasFamilyIdentifier'),
                   model_uri=BIOCORE.hasFamilyIdentifier, domain=None, range=Optional[Union[str, List[str]]])

slots.hasFileFormat = Slot(uri=BIOCORE['TerraCore#hasFileFormat'], name="hasFileFormat", curie=BIOCORE.curie('TerraCore#hasFileFormat'),
                   model_uri=BIOCORE.hasFileFormat, domain=None, range=Optional[Union[str, List[str]]])

slots.hasFragments = Slot(uri=BIOCORE['TerraCore#hasFragments'], name="hasFragments", curie=BIOCORE.curie('TerraCore#hasFragments'),
                   model_uri=BIOCORE.hasFragments, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGRCName = Slot(uri=BIOCORE['TerraCore#hasGRCName'], name="hasGRCName", curie=BIOCORE.curie('TerraCore#hasGRCName'),
                   model_uri=BIOCORE.hasGRCName, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGeneContext = Slot(uri=BIOCORE['TerraCore#hasGeneContext'], name="hasGeneContext", curie=BIOCORE.curie('TerraCore#hasGeneContext'),
                   model_uri=BIOCORE.hasGeneContext, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGeneExpressionProgram = Slot(uri=BIOCORE['TerraCore#hasGeneExpressionProgram'], name="hasGeneExpressionProgram", curie=BIOCORE.curie('TerraCore#hasGeneExpressionProgram'),
                   model_uri=BIOCORE.hasGeneExpressionProgram, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGeneticAncestry = Slot(uri=BIOCORE['TerraCore#hasGeneticAncestry'], name="hasGeneticAncestry", curie=BIOCORE.curie('TerraCore#hasGeneticAncestry'),
                   model_uri=BIOCORE.hasGeneticAncestry, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGeneticModification = Slot(uri=BIOCORE['TerraCore#hasGeneticModification'], name="hasGeneticModification", curie=BIOCORE.curie('TerraCore#hasGeneticModification'),
                   model_uri=BIOCORE.hasGeneticModification, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGeneticModificationMethod = Slot(uri=BIOCORE['TerraCore#hasGeneticModificationMethod'], name="hasGeneticModificationMethod", curie=BIOCORE.curie('TerraCore#hasGeneticModificationMethod'),
                   model_uri=BIOCORE.hasGeneticModificationMethod, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGeneticModificationReference = Slot(uri=BIOCORE['TerraCore#hasGeneticModificationReference'], name="hasGeneticModificationReference", curie=BIOCORE.curie('TerraCore#hasGeneticModificationReference'),
                   model_uri=BIOCORE.hasGeneticModificationReference, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGeneticModificationType = Slot(uri=BIOCORE['TerraCore#hasGeneticModificationType'], name="hasGeneticModificationType", curie=BIOCORE.curie('TerraCore#hasGeneticModificationType'),
                   model_uri=BIOCORE.hasGeneticModificationType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGenotypicSex = Slot(uri=BIOCORE['TerraCore#hasGenotypicSex'], name="hasGenotypicSex", curie=BIOCORE.curie('TerraCore#hasGenotypicSex'),
                   model_uri=BIOCORE.hasGenotypicSex, domain=None, range=Optional[Union[str, List[str]]])

slots.hasGrade = Slot(uri=BIOCORE['TerraCore#hasGrade'], name="hasGrade", curie=BIOCORE.curie('TerraCore#hasGrade'),
                   model_uri=BIOCORE.hasGrade, domain=None, range=Optional[Union[str, List[str]]])

slots.hasHostOrganism = Slot(uri=BIOCORE['TerraCore#hasHostOrganism'], name="hasHostOrganism", curie=BIOCORE.curie('TerraCore#hasHostOrganism'),
                   model_uri=BIOCORE.hasHostOrganism, domain=None, range=Optional[Union[str, List[str]]])

slots.hasImmunogen = Slot(uri=BIOCORE['TerraCore#hasImmunogen'], name="hasImmunogen", curie=BIOCORE.curie('TerraCore#hasImmunogen'),
                   model_uri=BIOCORE.hasImmunogen, domain=None, range=Optional[Union[str, List[str]]])

slots.hasLibraryLayout = Slot(uri=BIOCORE['TerraCore#hasLibraryLayout'], name="hasLibraryLayout", curie=BIOCORE.curie('TerraCore#hasLibraryLayout'),
                   model_uri=BIOCORE.hasLibraryLayout, domain=None, range=Optional[Union[str, List[str]]])

slots.hasLot = Slot(uri=BIOCORE['TerraCore#hasLot'], name="hasLot", curie=BIOCORE.curie('TerraCore#hasLot'),
                   model_uri=BIOCORE.hasLot, domain=None, range=Optional[Union[str, List[str]]])

slots.hasLowerBound = Slot(uri=BIOCORE['TerraCore#hasLowerBound'], name="hasLowerBound", curie=BIOCORE.curie('TerraCore#hasLowerBound'),
                   model_uri=BIOCORE.hasLowerBound, domain=None, range=Optional[Union[str, List[str]]])

slots.hasMannerOfDeath = Slot(uri=BIOCORE['TerraCore#hasMannerOfDeath'], name="hasMannerOfDeath", curie=BIOCORE.curie('TerraCore#hasMannerOfDeath'),
                   model_uri=BIOCORE.hasMannerOfDeath, domain=None, range=Optional[Union[str, List[str]]])

slots.hasMeasurementType = Slot(uri=BIOCORE['TerraCore#hasMeasurementType'], name="hasMeasurementType", curie=BIOCORE.curie('TerraCore#hasMeasurementType'),
                   model_uri=BIOCORE.hasMeasurementType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasMedication = Slot(uri=BIOCORE['TerraCore#hasMedication'], name="hasMedication", curie=BIOCORE.curie('TerraCore#hasMedication'),
                   model_uri=BIOCORE.hasMedication, domain=None, range=Optional[Union[str, List[str]]])

slots.hasMorphology = Slot(uri=BIOCORE['TerraCore#hasMorphology'], name="hasMorphology", curie=BIOCORE.curie('TerraCore#hasMorphology'),
                   model_uri=BIOCORE.hasMorphology, domain=None, range=Optional[Union[str, List[str]]])

slots.hasNonDuplicatedFragments = Slot(uri=BIOCORE['TerraCore#hasNonDuplicatedFragments'], name="hasNonDuplicatedFragments", curie=BIOCORE.curie('TerraCore#hasNonDuplicatedFragments'),
                   model_uri=BIOCORE.hasNonDuplicatedFragments, domain=None, range=Optional[Union[str, List[str]]])

slots.hasOrganismType = Slot(uri=BIOCORE['TerraCore#hasOrganismType'], name="hasOrganismType", curie=BIOCORE.curie('TerraCore#hasOrganismType'),
                   model_uri=BIOCORE.hasOrganismType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPairedEndIdentifier = Slot(uri=BIOCORE['TerraCore#hasPairedEndIdentifier'], name="hasPairedEndIdentifier", curie=BIOCORE.curie('TerraCore#hasPairedEndIdentifier'),
                   model_uri=BIOCORE.hasPairedEndIdentifier, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPartNumber = Slot(uri=BIOCORE['TerraCore#hasPartNumber'], name="hasPartNumber", curie=BIOCORE.curie('TerraCore#hasPartNumber'),
                   model_uri=BIOCORE.hasPartNumber, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPercentAlignedReads = Slot(uri=BIOCORE['TerraCore#hasPercentAlignedReads'], name="hasPercentAlignedReads", curie=BIOCORE.curie('TerraCore#hasPercentAlignedReads'),
                   model_uri=BIOCORE.hasPercentAlignedReads, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPercentDuplicateFragments = Slot(uri=BIOCORE['TerraCore#hasPercentDuplicateFragments'], name="hasPercentDuplicateFragments", curie=BIOCORE.curie('TerraCore#hasPercentDuplicateFragments'),
                   model_uri=BIOCORE.hasPercentDuplicateFragments, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPhenotype = Slot(uri=BIOCORE['TerraCore#hasPhenotype'], name="hasPhenotype", curie=BIOCORE.curie('TerraCore#hasPhenotype'),
                   model_uri=BIOCORE.hasPhenotype, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPlatform = Slot(uri=BIOCORE['TerraCore#hasPlatform'], name="hasPlatform", curie=BIOCORE.curie('TerraCore#hasPlatform'),
                   model_uri=BIOCORE.hasPlatform, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPlatformIdentifier = Slot(uri=BIOCORE['TerraCore#hasPlatformIdentifier'], name="hasPlatformIdentifier", curie=BIOCORE.curie('TerraCore#hasPlatformIdentifier'),
                   model_uri=BIOCORE.hasPlatformIdentifier, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPreservationState = Slot(uri=BIOCORE['TerraCore#hasPreservationState'], name="hasPreservationState", curie=BIOCORE.curie('TerraCore#hasPreservationState'),
                   model_uri=BIOCORE.hasPreservationState, domain=None, range=Optional[Union[str, List[str]]])

slots.hasProtocol = Slot(uri=BIOCORE['TerraCore#hasProtocol'], name="hasProtocol", curie=BIOCORE.curie('TerraCore#hasProtocol'),
                   model_uri=BIOCORE.hasProtocol, domain=None, range=Optional[Union[str, List[str]]])

slots.hasRace = Slot(uri=BIOCORE['TerraCore#hasRace'], name="hasRace", curie=BIOCORE.curie('TerraCore#hasRace'),
                   model_uri=BIOCORE.hasRace, domain=None, range=Optional[Union[str, List[str]]])

slots.hasReadCount = Slot(uri=BIOCORE['TerraCore#hasReadCount'], name="hasReadCount", curie=BIOCORE.curie('TerraCore#hasReadCount'),
                   model_uri=BIOCORE.hasReadCount, domain=None, range=Optional[Union[str, List[str]]])

slots.hasReadLength = Slot(uri=BIOCORE['TerraCore#hasReadLength'], name="hasReadLength", curie=BIOCORE.curie('TerraCore#hasReadLength'),
                   model_uri=BIOCORE.hasReadLength, domain=None, range=Optional[Union[str, List[str]]])

slots.hasReferenceAllele = Slot(uri=BIOCORE['TerraCore#hasReferenceAllele'], name="hasReferenceAllele", curie=BIOCORE.curie('TerraCore#hasReferenceAllele'),
                   model_uri=BIOCORE.hasReferenceAllele, domain=None, range=Optional[Union[str, List[str]]])

slots.hasReportedEthnicity = Slot(uri=BIOCORE['TerraCore#hasReportedEthnicity'], name="hasReportedEthnicity", curie=BIOCORE.curie('TerraCore#hasReportedEthnicity'),
                   model_uri=BIOCORE.hasReportedEthnicity, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSampleTreatmentMethod = Slot(uri=BIOCORE['TerraCore#hasSampleTreatmentMethod'], name="hasSampleTreatmentMethod", curie=BIOCORE.curie('TerraCore#hasSampleTreatmentMethod'),
                   model_uri=BIOCORE.hasSampleTreatmentMethod, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSampleTreatmentType = Slot(uri=BIOCORE['TerraCore#hasSampleTreatmentType'], name="hasSampleTreatmentType", curie=BIOCORE.curie('TerraCore#hasSampleTreatmentType'),
                   model_uri=BIOCORE.hasSampleTreatmentType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSampleType = Slot(uri=BIOCORE['TerraCore#hasSampleType'], name="hasSampleType", curie=BIOCORE.curie('TerraCore#hasSampleType'),
                   model_uri=BIOCORE.hasSampleType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSequenceExpression = Slot(uri=BIOCORE['TerraCore#hasSequenceExpression'], name="hasSequenceExpression", curie=BIOCORE.curie('TerraCore#hasSequenceExpression'),
                   model_uri=BIOCORE.hasSequenceExpression, domain=None, range=Optional[Union[str, List[str]]])

slots.hasSource = Slot(uri=BIOCORE['TerraCore#hasSource'], name="hasSource", curie=BIOCORE.curie('TerraCore#hasSource'),
                   model_uri=BIOCORE.hasSource, domain=None, range=Optional[Union[str, List[str]]])

slots.hasStartPosition = Slot(uri=BIOCORE['TerraCore#hasStartPosition'], name="hasStartPosition", curie=BIOCORE.curie('TerraCore#hasStartPosition'),
                   model_uri=BIOCORE.hasStartPosition, domain=None, range=Optional[Union[str, List[str]]])

slots.hasStopPosition = Slot(uri=BIOCORE['TerraCore#hasStopPosition'], name="hasStopPosition", curie=BIOCORE.curie('TerraCore#hasStopPosition'),
                   model_uri=BIOCORE.hasStopPosition, domain=None, range=Optional[Union[str, List[str]]])

slots.hasStrain = Slot(uri=BIOCORE['TerraCore#hasStrain'], name="hasStrain", curie=BIOCORE.curie('TerraCore#hasStrain'),
                   model_uri=BIOCORE.hasStrain, domain=None, range=Optional[Union[str, List[str]]])

slots.hasStructuralVariationType = Slot(uri=BIOCORE['TerraCore#hasStructuralVariationType'], name="hasStructuralVariationType", curie=BIOCORE.curie('TerraCore#hasStructuralVariationType'),
                   model_uri=BIOCORE.hasStructuralVariationType, domain=None, range=Optional[Union[str, List[str]]])

slots.hasTarget = Slot(uri=BIOCORE['TerraCore#hasTarget'], name="hasTarget", curie=BIOCORE.curie('TerraCore#hasTarget'),
                   model_uri=BIOCORE.hasTarget, domain=None, range=Optional[Union[str, List[str]]])

slots.hasTemperatureUnit = Slot(uri=BIOCORE['TerraCore#hasTemperatureUnit'], name="hasTemperatureUnit", curie=BIOCORE.curie('TerraCore#hasTemperatureUnit'),
                   model_uri=BIOCORE.hasTemperatureUnit, domain=None, range=Optional[Union[str, List[str]]])

slots.hasTermName = Slot(uri=BIOCORE['TerraCore#hasTermName'], name="hasTermName", curie=BIOCORE.curie('TerraCore#hasTermName'),
                   model_uri=BIOCORE.hasTermName, domain=None, range=Optional[Union[str, List[str]]])

slots.hasTreatmentOutcome = Slot(uri=BIOCORE['TerraCore#hasTreatmentOutcome'], name="hasTreatmentOutcome", curie=BIOCORE.curie('TerraCore#hasTreatmentOutcome'),
                   model_uri=BIOCORE.hasTreatmentOutcome, domain=None, range=Optional[Union[str, List[str]]])

slots.hasTumorMorphology = Slot(uri=BIOCORE['TerraCore#hasTumorMorphology'], name="hasTumorMorphology", curie=BIOCORE.curie('TerraCore#hasTumorMorphology'),
                   model_uri=BIOCORE.hasTumorMorphology, domain=None, range=Optional[Union[str, List[str]]])

slots.hasURI = Slot(uri=BIOCORE['TerraCore#hasURI'], name="hasURI", curie=BIOCORE.curie('TerraCore#hasURI'),
                   model_uri=BIOCORE.hasURI, domain=None, range=Optional[Union[str, List[str]]])

slots.hasUnit = Slot(uri=BIOCORE['TerraCore#hasUnit'], name="hasUnit", curie=BIOCORE.curie('TerraCore#hasUnit'),
                   model_uri=BIOCORE.hasUnit, domain=None, range=Optional[Union[str, List[str]]])

slots.hasUpperBound = Slot(uri=BIOCORE['TerraCore#hasUpperBound'], name="hasUpperBound", curie=BIOCORE.curie('TerraCore#hasUpperBound'),
                   model_uri=BIOCORE.hasUpperBound, domain=None, range=Optional[Union[str, List[str]]])

slots.hasWeightUnit = Slot(uri=BIOCORE['TerraCore#hasWeightUnit'], name="hasWeightUnit", curie=BIOCORE.curie('TerraCore#hasWeightUnit'),
                   model_uri=BIOCORE.hasWeightUnit, domain=None, range=Optional[Union[str, List[str]]])

slots.isCauseOfDeath = Slot(uri=BIOCORE['TerraCore#isCauseOfDeath'], name="isCauseOfDeath", curie=BIOCORE.curie('TerraCore#isCauseOfDeath'),
                   model_uri=BIOCORE.isCauseOfDeath, domain=None, range=Optional[Union[str, List[str]]])

slots.isContributorToDeath = Slot(uri=BIOCORE['TerraCore#isContributorToDeath'], name="isContributorToDeath", curie=BIOCORE.curie('TerraCore#isContributorToDeath'),
                   model_uri=BIOCORE.isContributorToDeath, domain=None, range=Optional[Union[str, List[str]]])

slots.isWholeCell = Slot(uri=BIOCORE['TerraCore#isWholeCell'], name="isWholeCell", curie=BIOCORE.curie('TerraCore#isWholeCell'),
                   model_uri=BIOCORE.isWholeCell, domain=None, range=Optional[Union[str, List[str]]])

slots.usesSoftware = Slot(uri=BIOCORE['TerraCore#usesSoftware'], name="usesSoftware", curie=BIOCORE.curie('TerraCore#usesSoftware'),
                   model_uri=BIOCORE.usesSoftware, domain=None, range=Optional[Union[str, List[str]]])

slots.domainIncludes = Slot(uri="str(uriorcurie)", name="domainIncludes", curie=None,
                   model_uri=BIOCORE.domainIncludes, domain=None, range=Optional[Union[str, List[str]]])

slots.rangeIncludes = Slot(uri=SCHEMA.rangeIncludes, name="rangeIncludes", curie=SCHEMA.curie('rangeIncludes'),
                   model_uri=BIOCORE.rangeIncludes, domain=None, range=Optional[Union[str, List[str]]])

slots.abstract = Slot(uri=DCT.abstract, name="abstract", curie=DCT.curie('abstract'),
                   model_uri=BIOCORE.abstract, domain=None, range=Optional[Union[str, List[str]]])

slots.accessRights = Slot(uri=DCT.accessRights, name="accessRights", curie=DCT.curie('accessRights'),
                   model_uri=BIOCORE.accessRights, domain=None, range=Optional[Union[str, List[str]]])

slots.accrualMethod = Slot(uri=DCT.accrualMethod, name="accrualMethod", curie=DCT.curie('accrualMethod'),
                   model_uri=BIOCORE.accrualMethod, domain=None, range=Optional[Union[str, List[str]]])

slots.accrualPeriodicity = Slot(uri=DCT.accrualPeriodicity, name="accrualPeriodicity", curie=DCT.curie('accrualPeriodicity'),
                   model_uri=BIOCORE.accrualPeriodicity, domain=None, range=Optional[Union[str, List[str]]])

slots.accrualPolicy = Slot(uri=DCT.accrualPolicy, name="accrualPolicy", curie=DCT.curie('accrualPolicy'),
                   model_uri=BIOCORE.accrualPolicy, domain=None, range=Optional[Union[str, List[str]]])

slots.audience = Slot(uri=DCT.audience, name="audience", curie=DCT.curie('audience'),
                   model_uri=BIOCORE.audience, domain=None, range=Optional[Union[str, List[str]]])

slots.conformsTo = Slot(uri=DCT.conformsTo, name="conformsTo", curie=DCT.curie('conformsTo'),
                   model_uri=BIOCORE.conformsTo, domain=None, range=Optional[Union[str, List[str]]])

slots.contributor = Slot(uri=DCT.contributor, name="contributor", curie=DCT.curie('contributor'),
                   model_uri=BIOCORE.contributor, domain=None, range=Optional[Union[str, List[str]]])

slots.coverage = Slot(uri=DCT.coverage, name="coverage", curie=DCT.curie('coverage'),
                   model_uri=BIOCORE.coverage, domain=None, range=Optional[Union[str, List[str]]])

slots.creator = Slot(uri=DCT.creator, name="creator", curie=DCT.curie('creator'),
                   model_uri=BIOCORE.creator, domain=None, range=Optional[Union[str, List[str]]])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=BIOCORE.description, domain=None, range=Optional[Union[str, List[str]]])

slots.educationLevel = Slot(uri=DCT.educationLevel, name="educationLevel", curie=DCT.curie('educationLevel'),
                   model_uri=BIOCORE.educationLevel, domain=None, range=Optional[Union[str, List[str]]])

slots.extent = Slot(uri=DCT.extent, name="extent", curie=DCT.curie('extent'),
                   model_uri=BIOCORE.extent, domain=None, range=Optional[Union[str, List[str]]])

slots.hasFormat = Slot(uri=DCT.hasFormat, name="hasFormat", curie=DCT.curie('hasFormat'),
                   model_uri=BIOCORE.hasFormat, domain=None, range=Optional[Union[str, List[str]]])

slots.hasVersion = Slot(uri=BIOCORE['TerraCore#hasVersion'], name="hasVersion", curie=BIOCORE.curie('TerraCore#hasVersion'),
                   model_uri=BIOCORE.hasVersion, domain=None, range=Optional[Union[str, List[str]]])

slots.isFormatOf = Slot(uri=DCT.isFormatOf, name="isFormatOf", curie=DCT.curie('isFormatOf'),
                   model_uri=BIOCORE.isFormatOf, domain=None, range=Optional[Union[str, List[str]]])

slots.isPartOf = Slot(uri=DCT.isPartOf, name="isPartOf", curie=DCT.curie('isPartOf'),
                   model_uri=BIOCORE.isPartOf, domain=None, range=Optional[Union[str, List[str]]])

slots.isReferencedBy = Slot(uri=DCT.isReferencedBy, name="isReferencedBy", curie=DCT.curie('isReferencedBy'),
                   model_uri=BIOCORE.isReferencedBy, domain=None, range=Optional[Union[str, List[str]]])

slots.isReplacedBy = Slot(uri=DCT.isReplacedBy, name="isReplacedBy", curie=DCT.curie('isReplacedBy'),
                   model_uri=BIOCORE.isReplacedBy, domain=None, range=Optional[Union[str, List[str]]])

slots.isRequiredBy = Slot(uri=DCT.isRequiredBy, name="isRequiredBy", curie=DCT.curie('isRequiredBy'),
                   model_uri=BIOCORE.isRequiredBy, domain=None, range=Optional[Union[str, List[str]]])

slots.isVersionOf = Slot(uri=DCT.isVersionOf, name="isVersionOf", curie=DCT.curie('isVersionOf'),
                   model_uri=BIOCORE.isVersionOf, domain=None, range=Optional[Union[str, List[str]]])

slots.language = Slot(uri=DCT.language, name="language", curie=DCT.curie('language'),
                   model_uri=BIOCORE.language, domain=None, range=Optional[Union[str, List[str]]])

slots.mediator = Slot(uri=DCT.mediator, name="mediator", curie=DCT.curie('mediator'),
                   model_uri=BIOCORE.mediator, domain=None, range=Optional[Union[str, List[str]]])

slots.medium = Slot(uri=DCT.medium, name="medium", curie=DCT.curie('medium'),
                   model_uri=BIOCORE.medium, domain=None, range=Optional[Union[str, List[str]]])

slots.publisher = Slot(uri=DCT.publisher, name="publisher", curie=DCT.curie('publisher'),
                   model_uri=BIOCORE.publisher, domain=None, range=Optional[Union[str, List[str]]])

slots.references = Slot(uri=DCT.references, name="references", curie=DCT.curie('references'),
                   model_uri=BIOCORE.references, domain=None, range=Optional[Union[str, List[str]]])

slots.relation = Slot(uri=DCT.relation, name="relation", curie=DCT.curie('relation'),
                   model_uri=BIOCORE.relation, domain=None, range=Optional[Union[str, List[str]]])

slots.replaces = Slot(uri=DCT.replaces, name="replaces", curie=DCT.curie('replaces'),
                   model_uri=BIOCORE.replaces, domain=None, range=Optional[Union[str, List[str]]])

slots.requires = Slot(uri=DCT.requires, name="requires", curie=DCT.curie('requires'),
                   model_uri=BIOCORE.requires, domain=None, range=Optional[Union[str, List[str]]])

slots.rights = Slot(uri=DCT.rights, name="rights", curie=DCT.curie('rights'),
                   model_uri=BIOCORE.rights, domain=None, range=Optional[Union[str, List[str]]])

slots.source = Slot(uri=DCT.source, name="source", curie=DCT.curie('source'),
                   model_uri=BIOCORE.source, domain=None, range=Optional[Union[str, List[str]]])

slots.spatial = Slot(uri=DCT.spatial, name="spatial", curie=DCT.curie('spatial'),
                   model_uri=BIOCORE.spatial, domain=None, range=Optional[Union[str, List[str]]])

slots.tableOfContents = Slot(uri=DCT.tableOfContents, name="tableOfContents", curie=DCT.curie('tableOfContents'),
                   model_uri=BIOCORE.tableOfContents, domain=None, range=Optional[Union[str, List[str]]])

slots.temporal = Slot(uri=DCT.temporal, name="temporal", curie=DCT.curie('temporal'),
                   model_uri=BIOCORE.temporal, domain=None, range=Optional[Union[str, List[str]]])

slots.type = Slot(uri=DCT.type, name="type", curie=DCT.curie('type'),
                   model_uri=BIOCORE.type, domain=None, range=Optional[Union[str, List[str]]])

slots.affiliation = Slot(uri=SCHEMA.affiliation, name="affiliation", curie=SCHEMA.curie('affiliation'),
                   model_uri=BIOCORE.affiliation, domain=None, range=Optional[Union[str, List[str]]])

slots.definition_rdfs = Slot(uri=RDFS.definition, name="definition_rdfs", curie=RDFS.curie('definition'),
                   model_uri=BIOCORE.definition_rdfs, domain=None, range=Optional[Union[str, List[str]]])

slots.maker = Slot(uri=FOAF.maker, name="maker", curie=FOAF.curie('maker'),
                   model_uri=BIOCORE.maker, domain=None, range=Optional[Union[str, List[str]]])

slots.name = Slot(uri=FOAF.name, name="name", curie=FOAF.curie('name'),
                   model_uri=BIOCORE.name, domain=None, range=Optional[Union[str, List[str]]])

slots.workInfoHomepage = Slot(uri=FOAF.workInfoHomepage, name="workInfoHomepage", curie=FOAF.curie('workInfoHomepage'),
                   model_uri=BIOCORE.workInfoHomepage, domain=None, range=Optional[Union[str, List[str]]])

slots.hasAlpha2Code = Slot(uri=BIOCORE['TerraCore#hasAlpha2Code'], name="hasAlpha2Code", curie=BIOCORE.curie('TerraCore#hasAlpha2Code'),
                   model_uri=BIOCORE.hasAlpha2Code, domain=None, range=Optional[Union[str, List[str]]])

slots.hasColumnLabel = Slot(uri=BIOCORE['TerraCore#hasColumnLabel'], name="hasColumnLabel", curie=BIOCORE.curie('TerraCore#hasColumnLabel'),
                   model_uri=BIOCORE.hasColumnLabel, domain=None, range=Optional[Union[str, List[str]]])

slots.hasLifeStage = Slot(uri=BIOCORE['TerraCore#hasLifeStage'], name="hasLifeStage", curie=BIOCORE.curie('TerraCore#hasLifeStage'),
                   model_uri=BIOCORE.hasLifeStage, domain=None, range=Optional[Union[str, List[str]]])

slots.hasMailingAddress = Slot(uri=BIOCORE['TerraCore#hasMailingAddress'], name="hasMailingAddress", curie=BIOCORE.curie('TerraCore#hasMailingAddress'),
                   model_uri=BIOCORE.hasMailingAddress, domain=None, range=Optional[Union[str, List[str]]])

slots.hasMissingValueReason = Slot(uri=BIOCORE['TerraCore#hasMissingValueReason'], name="hasMissingValueReason", curie=BIOCORE.curie('TerraCore#hasMissingValueReason'),
                   model_uri=BIOCORE.hasMissingValueReason, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPairedNormal = Slot(uri=BIOCORE['TerraCore#hasPairedNormal'], name="hasPairedNormal", curie=BIOCORE.curie('TerraCore#hasPairedNormal'),
                   model_uri=BIOCORE.hasPairedNormal, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPairedTumor = Slot(uri=BIOCORE['TerraCore#hasPairedTumor'], name="hasPairedTumor", curie=BIOCORE.curie('TerraCore#hasPairedTumor'),
                   model_uri=BIOCORE.hasPairedTumor, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPhenotypeDescription = Slot(uri=BIOCORE['TerraCore#hasPhenotypeDescription'], name="hasPhenotypeDescription", curie=BIOCORE.curie('TerraCore#hasPhenotypeDescription'),
                   model_uri=BIOCORE.hasPhenotypeDescription, domain=None, range=Optional[Union[str, List[str]]])

slots.hasPostalCode = Slot(uri=BIOCORE['TerraCore#hasPostalCode'], name="hasPostalCode", curie=BIOCORE.curie('TerraCore#hasPostalCode'),
                   model_uri=BIOCORE.hasPostalCode, domain=None, range=Optional[Union[str, List[str]]])

slots.hasStage = Slot(uri=BIOCORE['TerraCore#hasStage'], name="hasStage", curie=BIOCORE.curie('TerraCore#hasStage'),
                   model_uri=BIOCORE.hasStage, domain=None, range=Optional[Union[str, List[str]]])

slots.hasTemperature = Slot(uri=BIOCORE['TerraCore#hasTemperature'], name="hasTemperature", curie=BIOCORE.curie('TerraCore#hasTemperature'),
                   model_uri=BIOCORE.hasTemperature, domain=None, range=Optional[Union[str, List[str]]])

slots.definition_prov = Slot(uri=PROV.definition, name="definition_prov", curie=PROV.curie('definition'),
                   model_uri=BIOCORE.definition_prov, domain=None, range=Optional[Union[str, List[str]]])

slots.prefLabel = Slot(uri=SKOS.prefLabel, name="prefLabel", curie=SKOS.curie('prefLabel'),
                   model_uri=BIOCORE.prefLabel, domain=None, range=Optional[Union[str, List[str]]])