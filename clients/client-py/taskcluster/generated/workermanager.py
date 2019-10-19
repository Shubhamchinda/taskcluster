# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from ..client import BaseClient
from ..client import createApiClient
from ..client import config
from ..client import createTemporaryCredentials
from ..client import createSession
_defaultConfig = config


class WorkerManager(BaseClient):
    """
    This service manages workers, including provisioning for dynamic worker pools.
    """

    classOptions = {
    }
    serviceName = 'worker-manager'
    apiVersion = 'v1'

    def ping(self, *args, **kwargs):
        """
        Ping Server

        Respond without doing anything.
        This endpoint is used to check that the service is up.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["ping"], *args, **kwargs)

    def listProviders(self, *args, **kwargs):
        """
        List Providers

        Retrieve a list of providers that are available for worker pools.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["listProviders"], *args, **kwargs)

    def createWorkerPool(self, *args, **kwargs):
        """
        Create Worker Pool

        Create a new worker pool. If the worker pool already exists, this will throw an error.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["createWorkerPool"], *args, **kwargs)

    def updateWorkerPool(self, *args, **kwargs):
        """
        Update Worker Pool

        Given an existing worker pool definition, this will modify it and return
        the new definition.

        To delete a worker pool, set its `providerId` to `"null-provider"`.
        After any existing workers have exited, a cleanup job will remove the
        worker pool.  During that time, the worker pool can be updated again, such
        as to set its `providerId` to a real provider.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["updateWorkerPool"], *args, **kwargs)

    def deleteWorkerPool(self, *args, **kwargs):
        """
        Delete Worker Pool

        Mark a worker pool for deletion.  This is the same as updating the pool to
        set its providerId to `"null-provider"`, but does not require scope
        `worker-manager:provider:null-provider`.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["deleteWorkerPool"], *args, **kwargs)

    def workerPool(self, *args, **kwargs):
        """
        Get Worker Pool

        Fetch an existing worker pool defition.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["workerPool"], *args, **kwargs)

    def listWorkerPools(self, *args, **kwargs):
        """
        List All Worker Pools

        Get the list of all the existing worker pools.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["listWorkerPools"], *args, **kwargs)

    def reportWorkerError(self, *args, **kwargs):
        """
        Report an error from a worker

        Report an error that occurred on a worker.  This error will be included
        with the other errors in `listWorkerPoolErrors(workerPoolId)`.

        Workers can use this endpoint to report startup or configuration errors
        that might be associated with the worker pool configuration and thus of
        interest to a worker-pool administrator.

        NOTE: errors are publicly visible.  Ensure that none of the content
        contains secrets or other sensitive information.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["reportWorkerError"], *args, **kwargs)

    def listWorkerPoolErrors(self, *args, **kwargs):
        """
        List Worker Pool Errors

        Get the list of worker pool errors.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["listWorkerPoolErrors"], *args, **kwargs)

    def listWorkersForWorkerGroup(self, *args, **kwargs):
        """
        Workers in a specific Worker Group in a Worker Pool

        Get the list of all the existing workers in a given group in a given worker pool.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["listWorkersForWorkerGroup"], *args, **kwargs)

    def worker(self, *args, **kwargs):
        """
        Get a Worker

        Get a single worker.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["worker"], *args, **kwargs)

    def createWorker(self, *args, **kwargs):
        """
        Create a Worker

        Create a new worker.  The precise behavior of this method depends
        on the provider implementing the given worker pool.  Some providers
        do not support creating workers at all, and will return a 400 error.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["createWorker"], *args, **kwargs)

    def removeWorker(self, *args, **kwargs):
        """
        Remove a Worker

        Remove an existing worker.  The precise behavior of this method depends
        on the provider implementing the given worker.  Some providers
        do not support removing workers at all, and will return a 400 error.
        Others may begin removing the worker, but it may remain available via
        the API (perhaps even in state RUNNING) afterward.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["removeWorker"], *args, **kwargs)

    def listWorkersForWorkerPool(self, *args, **kwargs):
        """
        Workers in a Worker Pool

        Get the list of all the existing workers in a given worker pool.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["listWorkersForWorkerPool"], *args, **kwargs)

    def registerWorker(self, *args, **kwargs):
        """
        Register a running worker

        Register a running worker.  Workers call this method on worker start-up.

        This call both marks the worker as running and returns the credentials
        the worker will require to perform its work.  The worker must provide
        some proof of its identity, and that proof varies by provider type.

        This method is ``experimental``
        """

        return self._makeApiCall(self.funcinfo["registerWorker"], *args, **kwargs)

    funcinfo = {
        "createWorker": {
            'args': ['workerPoolId', 'workerGroup', 'workerId'],
            'input': 'v1/create-worker-request.json#',
            'method': 'put',
            'name': 'createWorker',
            'output': 'v1/worker-full.json#',
            'route': '/workers/<workerPoolId>:/<workerGroup>/<workerId>',
            'stability': 'experimental',
        },
        "createWorkerPool": {
            'args': ['workerPoolId'],
            'input': 'v1/create-worker-pool-request.json#',
            'method': 'put',
            'name': 'createWorkerPool',
            'output': 'v1/worker-pool-full.json#',
            'route': '/worker-pool/<workerPoolId>',
            'stability': 'experimental',
        },
        "deleteWorkerPool": {
            'args': ['workerPoolId'],
            'method': 'delete',
            'name': 'deleteWorkerPool',
            'output': 'v1/worker-pool-full.json#',
            'route': '/worker-pool/<workerPoolId>',
            'stability': 'experimental',
        },
        "listProviders": {
            'args': [],
            'method': 'get',
            'name': 'listProviders',
            'output': 'v1/provider-list.json#',
            'query': ['continuationToken', 'limit'],
            'route': '/providers',
            'stability': 'stable',
        },
        "listWorkerPoolErrors": {
            'args': ['workerPoolId'],
            'method': 'get',
            'name': 'listWorkerPoolErrors',
            'output': 'v1/worker-pool-error-list.json#',
            'query': ['continuationToken', 'limit'],
            'route': '/worker-pool-errors/<workerPoolId>',
            'stability': 'experimental',
        },
        "listWorkerPools": {
            'args': [],
            'method': 'get',
            'name': 'listWorkerPools',
            'output': 'v1/worker-pool-list.json#',
            'query': ['continuationToken', 'limit'],
            'route': '/worker-pools',
            'stability': 'experimental',
        },
        "listWorkersForWorkerGroup": {
            'args': ['workerPoolId', 'workerGroup'],
            'method': 'get',
            'name': 'listWorkersForWorkerGroup',
            'output': 'v1/worker-list.json#',
            'query': ['continuationToken', 'limit'],
            'route': '/workers/<workerPoolId>:/<workerGroup>',
            'stability': 'experimental',
        },
        "listWorkersForWorkerPool": {
            'args': ['workerPoolId'],
            'method': 'get',
            'name': 'listWorkersForWorkerPool',
            'output': 'v1/worker-list.json#',
            'query': ['continuationToken', 'limit'],
            'route': '/workers/<workerPoolId>',
            'stability': 'experimental',
        },
        "ping": {
            'args': [],
            'method': 'get',
            'name': 'ping',
            'route': '/ping',
            'stability': 'stable',
        },
        "registerWorker": {
            'args': [],
            'input': 'v1/register-worker-request.json#',
            'method': 'post',
            'name': 'registerWorker',
            'output': 'v1/register-worker-response.json#',
            'route': '/worker/register',
            'stability': 'experimental',
        },
        "removeWorker": {
            'args': ['workerPoolId', 'workerGroup', 'workerId'],
            'method': 'delete',
            'name': 'removeWorker',
            'route': '/workers/<workerPoolId>/<workerGroup>/<workerId>',
            'stability': 'experimental',
        },
        "reportWorkerError": {
            'args': ['workerPoolId'],
            'input': 'v1/report-worker-error-request.json#',
            'method': 'post',
            'name': 'reportWorkerError',
            'output': 'v1/worker-pool-error.json#',
            'route': '/worker-pool-errors/<workerPoolId>',
            'stability': 'experimental',
        },
        "updateWorkerPool": {
            'args': ['workerPoolId'],
            'input': 'v1/update-worker-pool-request.json#',
            'method': 'post',
            'name': 'updateWorkerPool',
            'output': 'v1/worker-pool-full.json#',
            'route': '/worker-pool/<workerPoolId>',
            'stability': 'experimental',
        },
        "worker": {
            'args': ['workerPoolId', 'workerGroup', 'workerId'],
            'method': 'get',
            'name': 'worker',
            'output': 'v1/worker-full.json#',
            'route': '/workers/<workerPoolId>:/<workerGroup>/<workerId>',
            'stability': 'experimental',
        },
        "workerPool": {
            'args': ['workerPoolId'],
            'method': 'get',
            'name': 'workerPool',
            'output': 'v1/worker-pool-full.json#',
            'route': '/worker-pool/<workerPoolId>',
            'stability': 'experimental',
        },
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'WorkerManager']
