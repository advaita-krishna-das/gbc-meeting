function CommentsSummaryWidget() {

    function setComments(list) {
        roles = list.filter(function (v, i) { return v.role != null } )

        roles = groupBy(roles, "role")
        types = groupBy(list, "type")
        total = list.length
    }

    function view() {
        return {
            roles, types, total, rename
        }
    }

    function rename(val) {
        var r = {
            "plus": "P", "minus": "M", "info": "I"
        }
        return r[val] || val
    }

    var roles
    var types
    var total

    return { setComments, view }
}