PORTNAME=	fido2
PORTVERSION=	1.0.0
PORTREVISION=	1
CATEGORIES=	security python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	python@FreeBSD.org
COMMENT=	Provides library functionality for FIDO 2.0
WWW=		https://github.com/Yubico/python-fido2

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/COPYING

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cryptography>=2.6<40,1:security/py-cryptography@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}six>=0:devel/py-six@${PY_FLAVOR}
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}mock>0:devel/py-mock@${PY_FLAVOR}

USES=		python:3.7+
USE_PYTHON=	autoplist distutils unittest

NO_ARCH=	yes

.include <bsd.port.mk>
