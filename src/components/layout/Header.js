import React, { Component, Fragment } from 'react';
import { Link } from 'react-router-dom';
import logo from '../../assets/img/logo.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons/faSearch'

export default class Header extends Component {
    constructor(props) {
        super(props)
        
        this.state = {
            menu_class: '',
        }
    }

    setToggleMenuClass = () => {
        if (this.state.menu_class === '') {
            this.setState({
                menu_class: 'toggled',
            })
        } else {
            this.setState({
                menu_class: '',
            })
        }
    }

    render() {
        // let top_menu_class = `top-menu ${this.state.menu_class}`;
        return (
            <Fragment>
                <div className="nav-wrapper">
                    <div className="grad-bar"></div>
                    <nav className="navbar">
                        <img src={logo} alt="Tshepo Mohlatlole" />

                        <div className="menu-toggle">
                            <span className="bar"></span>
                            <span className="bar"></span>
                            <span className="bar"></span>
                        </div>
                        <ul className="nav no-search">
                            <li className="nav-item">
                                <Link to="/">Home</Link>
                            </li>
                            <li className="nav-item">
                                <Link to="/about">About</Link>
                            </li>
                            <li className="nav-item">
                                <Link to="/skills">Skills</Link>
                            </li>
                            <li className="nav-item">
                                <Link to="/projects">Projects</Link>
                            </li>
                            <li className="nav-item">
                                <Link to="/contact">Contact</Link>
                            </li>

                            <FontAwesomeIcon icon={faSearch} className="search-icon" />
                            <input className="search-input" type="text" placeholder="Search.."/>
                        </ul>
                    </nav>
                </div>
            </Fragment>
        )
    }
}
