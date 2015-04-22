__author__ = 'atrimble'


def get_topic_string(topic, partition):
    return topic + "(" + partition + ")"


def get_topic(topic_partition):
    if topic_partition.indexOf('(') > -1:
        return topic_partition.split("\\(")[0]
    return topic_partition


def get_partition(topic_partition):
    if topic_partition.indexOf('(') > -1:
        spl = topic_partition.split("\\(")
        if spl.length > 1:
            return spl[1]

    return '.*'
