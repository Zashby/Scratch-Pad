migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("i3ojcyuk2apdtiw")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "v73a6is8",
    "name": "user",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "_pb_users_auth_",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": []
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("i3ojcyuk2apdtiw")

  // remove
  collection.schema.removeField("v73a6is8")

  return dao.saveCollection(collection)
})
