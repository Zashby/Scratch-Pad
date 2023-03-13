migrate((db) => {
  const collection = new Collection({
    "id": "i3ojcyuk2apdtiw",
    "created": "2023-03-10 22:23:36.884Z",
    "updated": "2023-03-10 22:23:36.884Z",
    "name": "messages",
    "type": "base",
    "system": false,
    "schema": [
      {
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
      }
    ],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("i3ojcyuk2apdtiw");

  return dao.deleteCollection(collection);
})
