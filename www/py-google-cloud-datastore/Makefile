PORTNAME=	google-cloud-datastore
PORTVERSION=	2.8.3
CATEGORIES=	www python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	sunpoet@FreeBSD.org
COMMENT=	Google Cloud Datastore API client library
WWW=		https://github.com/googleapis/python-datastore

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}google-api-core>=2.3.1<3.0.0:www/py-google-api-core@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}google-cloud-core>=1.4.0<3.0:www/py-google-cloud-core@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}proto-plus>=1.22.0<2.0.0:devel/py-proto-plus@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}protobuf>=3.19.5,1<5.0.0,1:devel/py-protobuf@${PY_FLAVOR}

USES=		python:3.7+
USE_PYTHON=	autoplist concurrent distutils

NO_ARCH=	yes

OPTIONS_DEFINE=	LIBCST
LIBCST_DESC=	Fixup scripts

LIBCST_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}libcst>=0.2.5:devel/py-libcst@${PY_FLAVOR}

.include <bsd.port.mk>
