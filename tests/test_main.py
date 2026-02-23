# Unit Tests

def test_run():
    from src.main import run
    result = run()
    assert result == "Application running successfully"

if __name__ == "__main__":
    test_run()
    print("All tests passed")
