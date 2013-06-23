from jenkinsapi.exceptions import UnknownQueueItem

class Invocation(object):
    """
    Represents the state and consequences of a single attempt to start a job.
    This class provides a context manager which is intended to watch the state of the job
    before and after the invoke. It will detect whether a process got queued, launched
    or whether nothing at all happened.

    An instance of this object will be returned by job.invoke()
    """

    def __init__(self, job):
        self.job = job
        self.initial_builds = None
        self.initial_queue_item = None


    def __enter__(self):
        """
        Start watching the job
        """
        self.job.poll()
        self.initial_builds = set(self.job.get_build_dict().keys())

        try:
            self.initial_queue_item = self.job.get_queue_item()
        except UnknownQueueItem:
            pass

    def __exit__(self, type, value, traceback):
        """
        Finish watching the job - it will track which new queue items or builds have
        been created as a consequence of invoking the job.
        """
        self.job.poll()
        newly_created_builds = set(self.job.get_build_dict().keys())

        queueItem = self.job.get_queue_item()


    def get_build_number(self):
        """
        If this job is building or complete then provide it's build-number
        """
        return 1

    def block(self, until='completed'):
        """
        Block this item until a condition is met.
        Setting until to 'running' blocks the item until it is running (i.e. it's no longer queued)
        """

    def stop(self):
        """
        Stop this item, whether it is on the queue or blocked.
        """

    def is_queued(self):
        """
        Returns True if this item is on the queue
        """
        return True

    def is_running(self):
        """
        Returns True if this item is executing now
        """
        return True

    def is_queued_or_running(self):
        return self.is_queued() or self.is_running()

    def get_queue_item(self):
        """
        If the item is queued it will return that QueueItem, otherwise it will
        raise an exception.
        """

    def get_build(self):
        """
        If the item is building it will return a Build object, otherwise it will
        raise an exception.
        """
