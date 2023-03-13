migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("i3ojcyuk2apdtiw")

  collection.listRule = ""
  collection.viewRule = ""
  collection.createRule = "user = @request.auth.id"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("i3ojcyuk2apdtiw")

  collection.listRule = null
  collection.viewRule = null
  collection.createRule = null

  return dao.saveCollection(collection)
})
