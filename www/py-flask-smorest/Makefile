PORTNAME=	flask-smorest
DISTVERSION=	0.39.0
CATEGORIES=	www devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	meka@tilda.center
COMMENT=	Flask/Marshmallow-based REST API framework
WWW=		https://github.com/marshmallow-code/flask-smorest

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}apispec>=3.0.0:devel/py-apispec@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}Flask>=1.1.0:www/py-flask@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}marshmallow>=2.15.2:devel/py-marshmallow@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}webargs>=6.0.0:www/py-webargs@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}werkzeug>=0.15:www/py-werkzeug@${PY_FLAVOR}

USES=		python:3.6+
USE_PYTHON=	autoplist concurrent distutils pytest

NO_ARCH=	yes

.include <bsd.port.mk>
