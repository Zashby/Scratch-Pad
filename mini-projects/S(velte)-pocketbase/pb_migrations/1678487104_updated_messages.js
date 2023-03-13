migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("i3ojcyuk2apdtiw")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "hx6ssqc7",
    "name": "text",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": 160,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("i3ojcyuk2apdtiw")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "hx6ssqc7",
    "name": "field",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": 160,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
})
