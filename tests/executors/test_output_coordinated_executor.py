from mirakuru.executors import OutputCoordinatedExecutor


def test_it_waits_for_process_output():
    command = 'bash -c "sleep 2 && echo foo && echo bar && sleep 100"'
    executor = OutputCoordinatedExecutor(command, 'foo')
    executor.start()

    assert executor.running()
    assert executor.output().readline() == 'bar\n'
    executor.stop()
