PORTNAME=	enlighten
DISTVERSION=	1.11.1
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	yuri@FreeBSD.org
COMMENT=	Console progress bar module for Python
WWW=		https://github.com/Rockhopper-Technologies/enlighten

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}blessed>=1.17.7:devel/py-blessed@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}prefixed>=0.3.2:devel/py-prefixed@${PY_FLAVOR}

USES=		python:3.6+
USE_PYTHON=	distutils autoplist pytest

NO_ARCH=	yes

.include <bsd.port.mk>
