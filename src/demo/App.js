/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { CopyButton } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <CopyButton
                    id='btn'
                    setProps={this.setProps}
                    {...this.state}
                >Copy</CopyButton>
            </div>
        )
    }
}

export default App;
