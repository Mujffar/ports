PORTNAME=	aioapns
PORTVERSION=	2.2
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	bofh@FreeBSD.org

COMMENT=	Efficient APNs Client Library for Python
WWW=		https://github.com/Fatal1ty/aioapns

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}h2>=4.0.0:www/py-h2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}openssl>=17.5.0:security/py-openssl@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pyjwt>=2.0.0:www/py-pyjwt@${PY_FLAVOR}

USES=		python:3.6+
USE_PYTHON=	autoplist distutils

NO_ARCH=	yes

.include <bsd.port.mk>
