PORTNAME=	python-lsp-black
DISTVERSION=	1.2.1
CATEGORIES=	textproc python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	yuri@FreeBSD.org
COMMENT=	Black plugin for the Python LSP Server
WWW=		https://github.com/python-lsp/python-lsp-black

LICENSE=	MIT

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}python-lsp-server>=1.4.0:textproc/py-python-lsp-server@${PY_FLAVOR}

USES=		python:3.7+
USE_PYTHON=	distutils autoplist pytest

NO_ARCH=	yes

.include <bsd.port.mk>
