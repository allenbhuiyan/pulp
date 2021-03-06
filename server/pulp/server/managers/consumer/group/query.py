from pulp.server.db.model.consumer import ConsumerGroup

from pulp.server.exceptions import MissingResource


class ConsumerGroupQueryManager(object):

    def get_group(self, consumer_group_id):
        """
        Returns the consumersitory group with the given ID, raising an exception
        if one does not exist.

        @param consumer_group_id: identifies the group
        @type  consumer_group_id: str

        @return: database representation of the consumer group

        @raise MissingResource: if there is no group with the given ID
        """
        group = ConsumerGroup.get_collection().find_one({'id': consumer_group_id})
        if group is None:
            raise MissingResource(consumer_group=consumer_group_id)
        return group

    def find_all(self):
        """
        Returns all consumersitory groups in the database or an empty list if
        none exist.

        @return: list of database representations of all consumersitory groups
        @rtype:  list
        """
        groups = list(ConsumerGroup.get_collection().find())
        return groups

    @staticmethod
    def find_by_criteria(criteria):
        """
        Return a list of consumersitory groups that match the provided criteria.

        @param criteria:    A Criteria object representing a search you want
                            to perform
        @type  criteria:    pulp.server.db.model.criteria.Criteria

        @return:    list of consumer group instances
        @rtype:     list
        """
        return ConsumerGroup.get_collection().query(criteria)
