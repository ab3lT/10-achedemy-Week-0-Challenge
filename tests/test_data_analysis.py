import pytest
from src.data_analysis import calculate_summary_statistics

def test_calculate_summary_statistics():
    data = {'GHI': [100, 200, 300], 'DNI': [50, 100, 150]}
    df = pd.DataFrame(data)
    
    result = calculate_summary_statistics(df)
    
    assert 'mean' in result.columns
    assert result.loc['mean', 'GHI'] == 200
