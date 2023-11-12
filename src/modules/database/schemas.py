COLLECTIONS = {
	"local": {},
	"remote": {},
	"soundcloud": {},
	"spotify": {},
	"youtube": {}
}

DATA_TABLES = {
	"artists": {},
	"events": {},
	# Add some events (e.g. Vietkong) to be included as historical context for tracks, albums and performances
	# Could be extended with manually input (calendar app integration?) personal events
	"events_history": {},
	"labels": {},
	"venues": {}
}

PLATFORM_SCHEMA = {
	"tracks": {
		"id": "integer primary key autoincrement",
	},
	"fragments": {
		"id": "integer primary key autoincrement",
	},
	"albums": {
		"id": "integer primary key autoincrement",
	},
	"performances": {
		"id": "integer primary key autoincrement",
	},
	"playlists": {
		"id": "integer primary key autoincrement",
		"name": "text",
		# when sourcing playlist from platform, it can be "renamed" from "alias" - define (common) "name" to enable sync
		"alias": "text",
		"create_time": "text",
		# e.g. sy and yt allow to save other users playlists
		"owner": "text",
		# ordered list of track ids
		"tracks": "blob",
		"shuffle_force": "numeric",
		"repeat_force": "numeric",
		"fade_force": "numeric"
	}
}