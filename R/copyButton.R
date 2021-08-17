# AUTO GENERATED FILE - DO NOT EDIT

copyButton <- function(children=NULL, id=NULL, disabled=NULL, value=NULL, n_clicks=NULL, n_clicks_timestamp=NULL, className=NULL) {
    
    props <- list(children=children, id=id, disabled=disabled, value=value, n_clicks=n_clicks, n_clicks_timestamp=n_clicks_timestamp, className=className)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CopyButton',
        namespace = 'dash_pairwise',
        propNames = c('children', 'id', 'disabled', 'value', 'n_clicks', 'n_clicks_timestamp', 'className'),
        package = 'dashPairwise'
        )

    structure(component, class = c('dash_component', 'list'))
}
