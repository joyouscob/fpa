from django import forms
from .models import Lgas, State, PredictionSearch

class SearchForm(forms.ModelForm):
  class Meta:
      model = PredictionSearch
      fields = ('state', 'lga')
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['lga'].queryset = Lgas.objects.none()
    if 'state' in self.data:
        try:
            state_id = int(self.data.get('state'))
            self.fields['lga'].queryset = Lgas.objects.filter(state_id=state_id).order_by('name')
        except (ValueError, TypeError):
            pass # invalid input from the client; ignore and fallback to empty City queryset
    elif self.instance.pk:
        self.fields['lga'].queryset = self.instance.state.lga_set.order_by('name')
