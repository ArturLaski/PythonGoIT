def get_grade(key):
  '''
  Przypisujemy dla grade_system wartości F=> 1 FX=>2 itd. zgodnie z tabelką
  '''
  grade_system = {'F':1, 'FX':2, 'E':3, 'D':3, 'C':4, 'B':5, 'A':5}    
  return grade_system.get(key, None) # pobieramy z grade_system po kluczu KEY  wartość i zwracamy

def get_description(key):
  '''
  Podobnie robimy grade_explain jako objaśnienie zgodnie z tabelką
  '''
  grade_explain = {'F':'Unsatisfactorily', 'FX':'Unsatisfactorily', 'E':'Enough', 'D':'Satisfactorily', 'C':'Good', 'B':'Very good', 'A':'Perfectly'}
  return grade_explain.get(key, None) # pobieramy z grade_explain  po kluczu KEY wartość i zwracamy
      
    