import antidote


def test_antidote_base():
    """base usage
    """
    @antidote.register
    class Dep:
        pass

    @antidote.inject
    def target(dep: Dep) -> bool:
        assert isinstance(dep, Dep)

    target()


def test_antidote_annotation_detection():
    """detect dependency by type annotation
    """
    @antidote.register
    class Dep:
        pass

    @antidote.inject
    def target(name: Dep) -> bool:
        assert isinstance(name, Dep)

    target()


def test_antidote_name_detection():
    """detect dependency by argument name
    """
    @antidote.register
    class Dep:
        pass

    @antidote.inject
    def target(dep) -> bool:
        assert isinstance(dep, Dep)

    target()


def test_antidote_lazy_annotation_detection():
    """detect dependency by lazy type annotation.

    All annotations will be lazy in Python 4.0.
    """
    @antidote.register
    class Dep:
        pass

    @antidote.inject
    def target(name: 'Dep') -> bool:
        assert isinstance(name, Dep)

    target()


def test_antidote_init_injection():
    """inject dependency in object's `__init__`
    """
    @antidote.register
    class Dep:
        pass

    # important: we use here `register` instead of `inject`
    @antidote.register
    class Target:
        def __init__(self, dep: Dep):
            self.dep = dep

        def __call__(self):
            assert isinstance(self.dep, Dep)

    Target()()


def test_antidote_partial_injection():
    """inject only some part of arguments
    """
    @antidote.register
    class Dep:
        pass

    @antidote.inject
    def target(dep: Dep, name: str) -> bool:
        assert isinstance(dep, Dep)
        assert name == 'lol'

    target(name='lol')


def test_antidote_overload_deps():
    """pass your own deps instead of default
    """
    @antidote.register
    class Dep:
        pass

    @antidote.inject
    def target(dep: Dep) -> bool:
        assert dep == 'lol'

    target('lol')


def test_antidote_chained_deps():
    """inject deps into deps
    """
    @antidote.register
    class Root:
        pass

    @antidote.register
    class Dep:
        def __init__(self, root: Root):
            self.root = root

    @antidote.inject
    def target(dep: Dep) -> bool:
        assert isinstance(dep, Dep)
        assert isinstance(dep.root, Root)

    target()
