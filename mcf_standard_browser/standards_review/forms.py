__author__ = 'palmer'
from django import forms
from .models import Standard, Adduct, FragmentationSpectrum, Molecule
import os
import logging


class MCFMoleculeForm(forms.ModelForm):
    class Meta:
        model = Molecule
        fields = ('name', 'sum_formula', 'lipidmaps_id', 'pubchem_id', 'cas_id', 'chebi_id', 'hmdb_id', 'inchi_code', 'solubility')

class MCFStandardForm(forms.ModelForm):
    class Meta:
        model = Standard
        fields = ('MCFID','molecule','vendor','vendor_cat','lot_num' ,'location' ,'purchase_date')


class MCFStandardBatchForm(forms.Form):
    semicolon_delimited_file = forms.FileField()


class UploadFileForm(forms.Form):
    mzml_file = forms.FileField()
    adducts = forms.ModelMultipleChoiceField(queryset=Adduct.objects.all())
    standards = forms.ModelMultipleChoiceField(queryset=Standard.objects.all().order_by('MCFID'))
    mass_accuracy_ppm = forms.FloatField(min_value=0.000001)
    quad_window_mz = forms.FloatField(min_value=0.000001)


class FragSpecReview(forms.Form):
    def __init__(self,*args,**kwargs):
        fragSpecId = kwargs.pop('extra')
        self.user = kwargs.pop('user', None)

        super(FragSpecReview, self).__init__(*args, **kwargs)
        for i in fragSpecId:

            logging.debug(i)
            fs = FragmentationSpectrum.objects.get(pk=i)
            logging.debug(fs.dataset)
            initial = 2
            if fs.reviewed:
                if fs.standard:
                    initial = 1
                else:
                    initial = 0
            self.fields['yesno_%s' % i] = forms.ChoiceField(choices=((1, 'Accept'), (0, 'Reject'), (2, 'Unrated')), widget=forms.RadioSelect, label=i, initial=initial)

    def get_response(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('yesno_'):
                yield (self.fields[name].label, value)




class ExportLibrary(forms.Form):
    data_format = forms.ChoiceField(choices=((0, 'mgf'), (1, 'csv'),), widget=forms.Select)
    spectra_to_export = forms.ChoiceField(choices=((0, 'Rated Correct'), (1, 'All Rated'), (2, 'ALL MSMS'),), widget=forms.Select)
