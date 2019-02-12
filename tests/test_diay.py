import diay


def test_diay_base():
    """base usage
    """
    class Dep:
        pass

    def target(dep: Dep) -> bool:
        assert isinstance(dep, Dep)

    injector = diay.Injector()
    injector.call(target)


def test_diay_annotation_detection():
    """detect dependency by type annotation
    """
    class Dep:
        pass

    def target(name: Dep) -> bool:
        assert isinstance(name, Dep)

    injector = diay.Injector()
    injector.call(target)


def test_diay_name_detection():
    """detect dependency by argument name
    """
    class Dep:
        pass

    def target(dep) -> bool:
        assert isinstance(dep, Dep)

    injector = diay.Injector()
    injector.call(target)


class DepGlobal:
    pass


def test_diay_lazy_annotation_detection():
    """detect dependency by lazy type annotation.

    All annotations will be lazy in Python 4.0.
    """

    def target(name: 'DepGlobal') -> bool:
        assert isinstance(name, DepGlobal)

    injector = diay.Injector()
    injector.call(target)


def test_diay_init_injection():
    """inject dependency in object's `__init__`
    """
    class Dep:
        pass

    class Target:
        def __init__(self, dep: Dep):
            self.dep = dep

        def __call__(self) -> bool:
            assert isinstance(self.dep, Dep)

    injector = diay.Injector()
    target = injector.get(Target)
    target()


def test_diay_partial_injection():
    """inject only some part of arguments
    """
    class Dep:
        pass

    def target(dep: Dep, name: str) -> bool:
        assert isinstance(dep, Dep)
        assert name == 'lol'

    injector = diay.Injector()
    injector.call(target, name='lol')


def test_diay_overload_deps():
    """pass your own deps instead of default
    """
    class Dep:
        pass

    def target(dep: Dep) -> bool:
        assert dep == 'lol'

    injector = diay.Injector()
    injector.call(target, dep='lol')


def test_diay_chained_deps():
    """inject deps into deps
    """
    class Root:
        pass

    class Dep:
        def __init__(self, root: Root):
            self.root = root

    def target(dep: Dep) -> bool:
        assert isinstance(dep, Dep)

    injector = diay.Injector()
    injector.call(target)
