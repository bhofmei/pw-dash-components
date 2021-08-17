import React, {Component} from 'react';
import PropTypes from 'prop-types';
import copy from 'copy-to-clipboard';
import {omit} from 'ramda';

/**
 * CopyButton is an button that when clicked copies text to the clipboard.
 *  It has an input value which is the content to be copied.
 * Additional properties of typical Dash components
 */
export default class CopyButton extends Component {
    CopyText(){
        const toCopy = this.props.value;
        copy(toCopy);
    }
    render() {
        const {setProps, value} = this.props;

        return (
            <button
               onChange={e => {
                    setProps({value: e.target.value});
                }}
                onClick={() => {
                    setProps({
                        n_clicks: this.props.n_clicks + 1,
                        n_clicks_timestamp: Date.now(),
                    });
                    this.CopyText()
                }}
            {...omit(['setProps', 'value'], this.props)}
            />

        );
    }
}

CopyButton.defaultProps = {
    n_clicks: 0,
    n_clicks_timestamp: -1
};

CopyButton.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string.isRequired,

    /**
     * Indicates wheather the user can interact with the element
     */
    disabled: PropTypes.oneOfType([PropTypes.string, PropTypes.bool]),

    /**
     * Array that holds components to render
     */
    children: PropTypes.oneOfType([
        PropTypes.arrayOf(PropTypes.node),
        PropTypes.node,
    ]),

    /**
     * The value to copy.
     */
    value: PropTypes.string,

    /**
     * Number of times the button has been clicked.
     */
    n_clicks: PropTypes.number,

    /**
     * Last time the button was clicked.
     */
    n_clicks_timestamp: PropTypes.number,

    /**
     * Often used with CSS to style elements with common properties.
     */
    className: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
