# This describes objects that we'll store in the database.
# This file was originally generated by the cvToSql program.
# Looks like that program needs to convert to docString comments....

from django.db import models

# Cell line or tissue used as the source of experimental material.
class CellType(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.TextField("description")
	# A description up to a paragraph long of plain text.
    organism = models.CharField("organism", max_length=255)
	# Common name of donor organism.
    tissue = models.CharField("tissue", max_length=255, blank=True)
	# Tissue source of sample.
    vendorName = models.CharField("vendor name", max_length=255)
	# Name of vendor selling reagent.
    vendorId = models.CharField("vendor id", max_length=255, blank=True)
	# Catalog number of other way of identifying reagent.
    orderUrl = models.TextField("order url", blank=True)
	# Web page to order regent.
    karyotype = models.TextField("karyotype", blank=True)
	# Status of chromosomes in cell - usually either normal or cancer.
    lineage = models.CharField("lineage", max_length=255, blank=True)
	# High level developmental lineage of cell.
    termId = models.CharField("term id", max_length=255, blank=True)
	# ID of term in external controlled vocabulary. See also termUrl.
    termUrl = models.CharField("term url", max_length=255, blank=True)
	# External URL describing controlled vocabulary.
    color = models.CharField("color", max_length=255, blank=True)
	# Red,green,blue components of color to visualize, each 0-255.
    sex = models.CharField("sex", max_length=255)
	# M for male, F for female, B for both, U for unknown.
    tier = models.PositiveIntegerField("tier", blank=True)
	# ENCODE cell line tier. 1-3 with 1 being most commonly used, 3 least.
    protocol = models.CharField("protocol", max_length=255, blank=True)
	# Scientific protocol used for growing cells
    category = models.CharField("category", max_length=255, blank=True)
	# Category of cell source - Tissue, primaryCells, etc.
    lab = models.CharField("lab", max_length=255, blank=True)
	# Scientific lab producing data.
    childOf = models.CharField("child of", max_length=255, blank=True)
	# Name of cell line or tissue this cell is descended from.
    lots = models.PositiveIntegerField("lots", blank=True)
	# The specific lots of reagent used.
    label = models.CharField("label", max_length=255, blank=True)
	# A relatively short label, no more than a few words
    age = models.CharField("age", max_length=255, blank=True)
	# Age of donor organism.
    strain = models.CharField("strain", max_length=255, blank=True)
	# Strain of organism.

    class Meta:
        db_table = 'cvDb_cellType'

    def __unicode__(self):
        return self.term

# Describes where an antibody is thought to bind
class AbTarget(models.Model):
    term = models.CharField("term", primary_key=True, max_length=255)
        # A relatively short label, no more than a few words 
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
        # If non-empty, the reason why this entry is obsolete.
    description = models.TextField("description")
        # Short description of antibody target
    externalId = models.CharField("external id", max_length=255)
        # Identifier for target, prefixed with source of ID, usually GeneCards
    url = models.CharField("target url", max_length=255, blank=True)
        # Web page associated with antibody target. 
        
    class Meta:
        db_table = 'cvDb_abTarget'

    def __unicode__(self):
        return self.term

# Describes an antibody
class Antibody(models.Model):
    term = models.CharField("term", max_length=255)
        # A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
        # A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
        # If non-empty, the reason why this entry is obsolete.
    description = models.TextField("description")
        # Short description of antibody itself.
    target = models.ForeignKey(AbTarget, db_column='target', max_length=255)
        # Molecular target of antibody.
    vendorName = models.CharField("vendor name", max_length=255)
        # Name of vendor selling reagent.
    vendorId = models.CharField("vendor id", max_length=255)
        # Catalog number of other way of identifying reagent.
    orderUrl = models.CharField("order url", max_length=255, blank=True)
        # Web page to order regent.
    lab = models.CharField("lab", max_length=255)
        # Scientific lab producing data.
    validation = models.CharField("validation", max_length=255)
        # How antibody was validated to be specific for target.
    label = models.CharField("label", max_length=255, blank=True)
        # A relatively short label, no more than a few words
    lots = models.CharField("lots", max_length=255, blank=True)
        # The specific lots of reagent used.

    class Meta:
        db_table = 'cvDb_ab'
        verbose_name_plural = "antibodies"

    def __unicode__(self):
        return self.term


# Algorithm used in high-throughput sequencing experiments to map sequenced tags to a particular location in the reference genome.
class MapAlgorithm(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_mapAlgorithm'

    def __unicode__(self):
        return self.term


# Specific information about cDNA sequence reads including length, directionality and single versus paired read.
class ReadType(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.

    class Meta:
        db_table = 'cvDb_readType'

    def __unicode__(self):
        return self.term


# The length of the insertion for paired reads for RNA-seq experiments.
class InsertLength(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_insertLength'

    def __unicode__(self):
        return self.term


# length of GIS DNA PET fragments, which has different values than fragLength
class FragSize(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_fragSize'

    def __unicode__(self):
        return self.term


# The cellular compartment from which RNA is extracted. Primarily used by the Transcriptome Project.
class Localization(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    termId = models.CharField("term id", max_length=255)
	# ID of term in external controlled vocabulary. See also termUrl.
    termUrl = models.CharField("term url", max_length=255)
	# External URL describing controlled vocabulary.
    label = models.CharField("label", max_length=255, blank=True)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_localization'

    def __unicode__(self):
        return self.term


# Fraction of total cellular RNA selected for by an experiment. This includes size fractionation (long versus short) and feature frationation (PolyA-, PolyA+, rRNA-).
class RnaExtract(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255, blank=True)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_rnaExtract'

    def __unicode__(self):
        return self.term


# NoTypeDescription
class Promoter(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.

    class Meta:
        db_table = 'cvDb_promoter'

    def __unicode__(self):
        return self.term


# The type of control (or 'input') used in ChIP-seq experiments to remove background noise before peak calling.
class Control(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_control'

    def __unicode__(self):
        return self.term


# Treatment used as an experimental variable in a series of experiments.
class Treatment(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.TextField("description")
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255, blank=True)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_treatment'

    def __unicode__(self):
        return self.term


# Lab specific protocol that may cover a number of steps in an experiment.  Most typically this identifies methods for building a DNA or RNA library.
class Protocol(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_protocol'

    def __unicode__(self):
        return self.term


# The phase in a cell cycle that corresponds to a defined DNA content range determined by flow 
# cytometry measurements that includes G1 (gap phase 1), S phase (the DNA synthesis phase), and 
# G2/M (the gap 2 and mitosis phases; here abbreviated G2). Different portions of S phase are 
# obtained by dividing the cell cycle into seven DNA content windows based on the relative peak 
# positions corresponding to the G1 and G2 cell cycle fractions. The G1 peak position is routinely 
# set at "60" relative UV fluorescence, thus producing G2 peak values in the 116-120 range
class Phase(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_phase'

    def __unicode__(self):
        return self.term


# Genomic region(s) targeted by an experiment that is not whole-genome
class Region(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_region'

    def __unicode__(self):
        return self.term


# The restriction enzyme used in an experiment, typically for DNA library preparation for a high-throughput sequencing experiment.
class RestrictionEnzyme(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_restrictionEnzyme'

    def __unicode__(self):
        return self.term


# Different track formats often allow different views of the data of a single experiment.  
# These views sometimes represent different stages of processing, such as experimental 'signal' 
# resulting directly from high-throughput sequencing and called 'peaks' which result from further 
# analysis.
class View(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.TextField("description")
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_view'

    def __unicode__(self):
        return self.term


# The types of experiments such as ChIP-seq, DNAse-seq and RNA-seq.
class DataType(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words
    dataGroup = models.CharField("data group", max_length=255)
	# High level grouping of experimental assay type.

    class Meta:
        db_table = 'cvDb_dataType'

    def __unicode__(self):
        return self.term


# NoTypeDescription
class Version(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.

    class Meta:
        db_table = 'cvDb_version'

    def __unicode__(self):
        return self.term


# The strain of the doner organism used in an experiment.
class Strain(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255, blank=True)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_strain'

    def __unicode__(self):
        return self.term


# The age of the organism used to produce tissue or cell line.
class Age(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    stage = models.CharField("stage", max_length=255)
	# High level place within life cycle of donor organism.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_age'

    def __unicode__(self):
        return self.term


# This indicates the status of a file in the attic or not.  It is an internal piece of metaData.
class Attic(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_attic'

    def __unicode__(self):
        return self.term


# Cell type category, such as T for tissue, L for cell line, P for primary cells
class Category(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_category'
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.term


# The sex of a cell line or tissue sample affects the genome target of an experiment.
class Sex(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.

    class Meta:
        db_table = 'cvDb_sex'
        verbose_name_plural = "sexes"

    def __unicode__(self):
        return self.term


# The status of the file or table object (revoked, replaced, etc)
class ObjStatus(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.

    class Meta:
        db_table = 'cvDb_objStatus'
        verbose_name_plural = "objStatuses"

    def __unicode__(self):
        return self.term


# The type of organism for an experiment.
class Organism(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.

    class Meta:
        db_table = 'cvDb_organism'

    def __unicode__(self):
        return self.term


# Source of tissue from either an indiviual organism or pooled set of organisms
class TissueSourceType(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.

    class Meta:
        db_table = 'cvDb_tissueSourceType'

    def __unicode__(self):
        return self.term


# Sequencing platform used in high-throughput sequencing experiment.
class SeqPlatform(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    geoPlatformName = models.CharField("geo platform name", max_length=255)
	# Short description of sequencing platform. Matches term used by GEO.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_seqPlatform'

    def __unicode__(self):
        return self.term


# Platform used in experiment.
class Platform(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    geoPlatformName = models.CharField("geo platform name", max_length=255)
	# Short description of sequencing platform. Matches term used by GEO.

    class Meta:
        db_table = 'cvDb_platform'

    def __unicode__(self):
        return self.term


# The name of the lab producing the data.  Often many labs are working together under one 
# grant or one project.
class Lab(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words
    labInst = models.CharField("lab inst", max_length=255)
	# The institution where the lab is located.
    labPi = models.CharField("lab pi", max_length=255)
	# Last name or other short identifier for lab's primary investigator
    labPiFull = models.CharField("lab pi full", max_length=255)
	# Full name of lab's primary investigator.
    grantPi = models.CharField("grant pi", max_length=255)
	# Last name of primary investigator on grant paying for data.
    organism = models.CharField("organism", max_length=255)
	# Common name of donor organism.

    class Meta:
        db_table = 'cvDb_lab'

    def __unicode__(self):
        return self.term


# Principle investigator holding the grant by which a set of experiments are financed. 
# Several labs led by other PI's may be under one grant.
class Grantee(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.CharField("description", max_length=255)
	# A description up to a paragraph long of plain text.
    grantInst = models.CharField("grant inst", max_length=255)
	# Name of instution awarded grant paying for data.
    projectName = models.CharField("project name", max_length=255)
	# Short name describing grant.
    label = models.CharField("label", max_length=255, blank=True)
	# A relatively short label, no more than a few words

    class Meta:
        db_table = 'cvDb_grantee'

    def __unicode__(self):
        return self.term


# Types of terms used frequently in controlled vocabulary or metadata should be defined here.
class TypeOfTerm(models.Model):
    term = models.CharField("term", max_length=255)
	# A relatively short label, no more than a few words
    tag = models.CharField("tag", max_length=255)
	# A short human and machine readable symbol with just alphanumeric characters.
    deprecated = models.CharField("deprecated", max_length=255, blank=True)
	# If non-empty, the reason why this entry is obsolete.
    description = models.TextField("description")
	# A description up to a paragraph long of plain text.
    label = models.CharField("label", max_length=255)
	# A relatively short label, no more than a few words
    searchable = models.CharField("searchable", max_length=255)
	# Describes how to search for term in Genome Browser. 'No' for unsearchable.
    cvDefined = models.CharField("cv defined", max_length=255)
	# Is there a controlled vocabulary for this term. Is 'yes' or 'no.'
    validate = models.CharField("validate", max_length=255)
	# Describes how to validate field typeOfTerm refers to. Use 'none' for no validation.
    hidden = models.CharField("hidden", max_length=255, blank=True)
	# Hide field in user interface? Can be 'yes' or 'no' or a release list
    priority = models.PositiveIntegerField("priority")
	# Order to display or search terms, lower is earlier.
    requiredVars = models.CharField("required vars", max_length=255, blank=True)
	# Required fields for a term of this type.
    optionalVars = models.CharField("optional vars", max_length=255, blank=True)
	# Optional fields for a term of this type.

    class Meta:
        db_table = 'cvDb_typeOfTerm'

    def __unicode__(self):
        return self.term


class Series(models.Model):
    """
    Represents a series of experiments of the same type done for
    the same project.
    """
    term = models.CharField(max_length=50, unique=True, db_index=True)
    dataType = models.CharField(max_length=40)
    grantee = models.CharField(max_length=255)

    class Meta:
        db_table = 'cvDb_series'
        verbose_name_plural = 'Serieses'

    def __unicode__(self):
        return self.term


class Experiment(models.Model):
    """
    A defined set of conditions for an experiment.  There may be
    multiple replicates of an experiment, but they are all done
    under the same conditions.  Often many experiments are done in
    a 'Series' under sets of conditions that vary in defined ways
    Some experiments may be designated controls for the series.
     """
    updateTime = models.CharField(max_length=40)
    series = models.ForeignKey(Series, db_column='series', to_field='term')
    accession = models.CharField(unique=True, max_length=16)
    organism = models.ForeignKey(Organism, db_column='organism')
    lab = models.ForeignKey(Lab, db_column='lab')
    dataType = models.ForeignKey(DataType, db_column='dataType')
    cellType = models.ForeignKey(CellType, db_column='cellType', blank=True, null=True)
    antibody = models.ForeignKey(Antibody, db_column='ab', blank=True, null=True)
    age = models.ForeignKey(Age, db_column='age', blank=True, null=True)
    attic = models.ForeignKey(Attic, db_column='attic', blank=True, null=True)
    category = models.ForeignKey(Category, db_column='category', blank=True, null=True)
    control = models.ForeignKey(Control, db_column='control', blank=True, null=True)
    fragSize = models.ForeignKey(FragSize, db_column='fragSize', blank=True, null=True)
    grantee = models.ForeignKey(Grantee, db_column='grantee', blank=True, null=True)
    insertLength = models.ForeignKey(InsertLength, db_column='insertLength', blank=True, null=True)
    localization = models.ForeignKey(Localization, db_column='localization', blank=True, null=True)
    mapAlgorithm = models.ForeignKey(MapAlgorithm, db_column='mapAlgorithm', blank=True, null=True)
    objStatus = models.ForeignKey(ObjStatus, db_column='objStatus', blank=True, null=True)
    phase = models.ForeignKey(Phase, db_column='phase', blank=True, null=True)
    platform = models.ForeignKey(Platform, db_column='platform', blank=True, null=True)
    promoter = models.ForeignKey(Promoter, db_column='promoter', blank=True, null=True)
    protocol = models.ForeignKey(Protocol, db_column='protocol', blank=True, null=True)
    readType = models.ForeignKey(ReadType, db_column='readType', blank=True, null=True)
    region = models.ForeignKey(Region, db_column='region', blank=True, null=True)
    restrictionEnzyme = models.ForeignKey(RestrictionEnzyme, db_column='restrictionEnzyme', blank=True, null=True)
    rnaExtract = models.ForeignKey(RnaExtract, db_column='rnaExtract', blank=True, null=True)
    seqPlatform = models.ForeignKey(SeqPlatform, db_column='seqPlatform', blank=True, null=True)
    sex = models.ForeignKey(Sex, db_column='sex', blank=True, null=True)
    strain = models.ForeignKey(Strain, db_column='strain', blank=True, null=True)
    tissueSourceType = models.ForeignKey(TissueSourceType, db_column='tissueSourceType', blank=True, null=True)
    treatment = models.ForeignKey(Treatment, db_column='treatment', blank=True, null=True)
    version = models.ForeignKey(Version, db_column='version', blank=True, null=True)

    class Meta:
        db_table = 'cvDb_experiment'

    def __unicode__(self):
        return self.accession + ' ' + `self.cellType`

class Result(models.Model):
    """
    A result of an experiment - generally either a data file or a
    database table. Intermediate as well as final results may be found
    here.  Some results may be replicated a number of times
    """
    experiment = models.ForeignKey(Experiment, db_column='experiment')
    replicate = models.CharField(max_length=20, blank=True)
    view = models.CharField(max_length=20)
    objType = models.CharField(max_length=20)
    fileName = models.CharField(max_length=255)
    md5sum = models.CharField(max_length=255)
    tableName = models.CharField(max_length=100, blank=True)
    dateSubmitted = models.CharField(max_length=40)
    dateResubmitted = models.CharField(max_length=40, blank=True)
    dateUnrestricted = models.CharField(max_length=40)

    class Meta:
        db_table = 'cvDb_result'

    def __unicode__(self):
        return self.fileName

