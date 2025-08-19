from src.main import sort

def test_1_standard_package():
    """Test for a package that is neither bulky nor heavy."""
    result = sort(width=10, height=10, length=10, mass=5)
    assert result == "STANDARD"

def test_2_special_heavy_only():
    """Test for a package that is only heavy."""
    result = sort(width=10, height=10, length=10, mass=25)
    assert result == "SPECIAL"

def test_3_special_bulky_by_volume_only():
    """Test for a package that is bulky only because of its volume."""
    # Volume: 100*100*100 = 1,000,000 cm³
    result = sort(width=100, height=100, length=100, mass=15)
    assert result == "SPECIAL"

def test_4_special_bulky_by_dimension_only():
    """Test for a package that is bulky only because of one dimension."""
    # One dimension > 150 cm
    result = sort(width=160, height=50, length=50, mass=15)
    assert result == "SPECIAL"

def test_5_rejected_heavy_and_bulky_by_volume():
    """Test for a package that is heavy AND bulky (by volume)."""
    # Volume > 1M, mass > 20
    result = sort(width=101, height=101, length=101, mass=21)
    assert result == "REJECTED"

def test_6_rejected_heavy_and_bulky_by_dimension():
    """Test for a package that is heavy AND bulky (by dimension)."""
    # One dimension > 150, mass > 20
    result = sort(width=151, height=10, length=10, mass=21)
    assert result == "REJECTED"

def test_7_volume_boundary_standard():
    """Boundary test: package just below the volume limit."""
    # Volume: 99 * 99 * 99 = 970,299 cm³
    result = sort(width=99, height=99, length=99, mass=19.99)
    assert result == "STANDARD"

def test_8_volume_boundary_special():
    """Boundary test: package at the exact volume limit, but not heavy."""
    # Volume: 100 * 100 * 100 = 1,000,000 cm³
    result = sort(width=100, height=100, length=100, mass=19.99)
    assert result == "SPECIAL"

def test_9_dimension_boundary_special():
    """Boundary test: package at the exact dimension limit, but not heavy."""
    result = sort(width=150, height=10, length=10, mass=19.99)
    assert result == "SPECIAL"

def test_10_all_boundaries_rejected():
    """Boundary test: package at the limit of volume, dimension, and mass."""
    # Volume > 1M (150*100*100), dimension > 150, and mass = 20
    result = sort(width=150, height=100, length=100, mass=20)
    assert result == "REJECTED"