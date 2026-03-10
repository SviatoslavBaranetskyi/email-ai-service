from aiokafka.admin import AIOKafkaAdminClient, NewTopic


async def create_topics(bootstrap_servers: str, topics: list[str]):
    admin = AIOKafkaAdminClient(bootstrap_servers=bootstrap_servers)
    await admin.start()
    try:
        existing_topics = await admin.list_topics()
        new_topics = [
            NewTopic(name=topic, num_partitions=1, replication_factor=1)
            for topic in topics if topic not in existing_topics
        ]
        if new_topics:
            await admin.create_topics(new_topics)
            for t in new_topics:
                print(f"Topic {t.name} created!")
    finally:
        await admin.close()