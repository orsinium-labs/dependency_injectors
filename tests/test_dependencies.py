import dependencies


def test_dependencies_base():
    """base usage
    """
    class Dep:
        pass

    class Target:
        def __init__(self, dep: Dep):
            self.dep = dep

        def __call__(self) -> bool:
            assert isinstance(self.dep, Dep)

    class Container(dependencies.Injector):
        dep = Dep
        target = Target

    Container.target()


def test_dependencies_annotation_detection():
    """detect dependency by type annotation
    """
    class Dep:
        pass

    class Target:
        def __init__(self, name: Dep):
            self.name = name

        def __call__(self) -> bool:
            assert isinstance(self.name, Dep)

    class Container(dependencies.Injector):
        dep = Dep
        target = Target

    Container.target()


class DepGlobal:
    pass


def test_dependencies_lazy_annotation_detection():
    """detect dependency by lazy type annotation.

    All annotations will be lazy in Python 4.0.
    """
    class Target:
        def __init__(self, name: 'DepGlobal'):
            self.name = name

        def __call__(self) -> bool:
            assert isinstance(self.name, DepGlobal)

    class Container(dependencies.Injector):
        dep = DepGlobal
        target = Target

    Container.target()


def test_dependencies_name_detection():
    """detect dependency by argument name
    """
    class Dep:
        pass

    class Target:
        def __init__(self, dep):
            self.dep = dep

        def __call__(self) -> bool:
            assert isinstance(self.dep, Dep)

    class Container(dependencies.Injector):
        dep = Dep
        target = Target

    Container.target()


def test_dependencies_function_injection():
    """inject dependency in function call
    """
    class Dep:
        pass

    def target(dep: Dep) -> bool:
        assert isinstance(dep, Dep)

    class Container(dependencies.Injector):
        dep = Dep
        target_ = target

    Container.target_()


def test_dependencies_partial_injection():
    """inject only some part of arguments
    """
    class Dep:
        pass

    class Target:
        def __init__(self, dep: Dep, name: str):
            self.dep = dep
            self.name = name

        def __call__(self) -> bool:
            assert isinstance(self.dep, Dep)
            assert self.name == 'lol'

    class Container(dependencies.Injector):
        dep = Dep
        target = Target

    Container.let(name='lol').target()


def test_dependencies_overload_deps():
    """pass your own deps instead of default
    """
    class Dep:
        pass

    class Target:
        def __init__(self, dep: Dep):
            self.dep = dep

        def __call__(self) -> bool:
            assert self.dep == 'lol'

    class Container(dependencies.Injector):
        dep = Dep
        target = Target

    Container.let(dep='lol').target()


def test_dependencies_chained_deps():
    """inject deps into deps
    """
    class Root:
        pass

    class Dep:
        def __init__(self, root: Root):
            self.root = root

    class Target:
        def __init__(self, dep: Dep):
            self.dep = dep

        def __call__(self) -> bool:
            assert isinstance(self.dep, Dep)
            assert isinstance(self.dep.root, Root)

    class Container(dependencies.Injector):
        dep = Dep
        root = Root
        target = Target

    Container.target()
