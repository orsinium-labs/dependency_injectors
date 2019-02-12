from dependency_injector import containers, providers


def test_base():
    class Dep:
        pass

    def target(dep: Dep):
        assert isinstance(dep, Dep)

    class Container(containers.DeclarativeContainer):
        dep = providers.Callable(Dep)
        target_ = providers.Callable(target, dep=dep)

    Container.target_()
