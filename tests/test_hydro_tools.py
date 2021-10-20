import hydrofunctions


def test_hydrofunctions():
    modules = dir()
    print(modules)
    assert "hydrofunctions" in modules

if __name__ == "__main__":
    print(dir())
