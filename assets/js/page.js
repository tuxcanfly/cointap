import React, { Component } from 'react'
import { Link } from 'react-router-dom'

class PageForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            address: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    loadPageFromServer() {
        $.ajax({
            url: 'api/balance/',
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({balance: data.balance});
            }.bind(this)
        })
    }

    componentDidMount() {
        this.loadPageFromServer();
    }

    componentWillUnmount() {
    }

    handleChange(event) {
        this.setState({address: event.target.value});
    }

    handleSubmit(event) {
        event.preventDefault();

        var data = {
            address: this.state.address,
        }
        const context = this;

        // Submit form via jQuery/AJAX
        $.ajax({
            type: 'POST',
            url: this.props.url,
            data: data
        })
        .done(function(data) {
            context.setState({amount: data.amount * 1e-8, tx: data.tx});
            $("#tx").removeClass("hide");
        })
        .fail(function(jqXhr) {
            console.log('failed to register');
        });
    }

    render() {
        var balance = this.balance = this.state.balance * 1e-8;
        var amount = Math.floor(this.state.balance  * 1e-5) * 1e-8;
        return (
            <div>
                <div>
                    <h1>HSK Testnet Faucet</h1>
                    <p>A faucet for <a href="https://handshake.org" target="_blank">Handshake</a>  Testnet Coins</p>

                    <div className="primary callout">
                        <p>Current wallet balance is {balance} HSK.</p>
                        <p>Giving out {amount} HSK per request.</p>
                    </div>

                    <form onSubmit={this.handleSubmit}>
                        <div className="row">
                            <div className="large-12 columns">
                                <fieldset>
                                    <legend>Enter your coin address</legend>
                                    <input id="address" name="address" type="text" value={this.state.address} onChange={this.handleChange} required placeholder="hsk address, e.g. ts1q2u8khznynfwf0jkp65jzfkd3fppqtwf6jmzkqj" />
                                    <button type="submit" className="large button">Send Coins</button>
                                </fieldset>
                            </div>
                        </div>
                    </form>

                    <div id="tx" className="secondary callout hide">
                        <p>Sent {this.state.amount} HSK via {this.state.tx} to {this.state.address}</p>
                    </div>
                </div>
            </div>
        );
    }
}

export { PageForm }
