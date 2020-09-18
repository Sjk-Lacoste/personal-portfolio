import React, { Component, Fragment } from 'react';
import axios from 'axios'
// import Project from './Project';

class Projects extends Component {
    constructor(props) {
        super(props);
    
        // Assign state itself, and a default value for items
        this.state = {
            projects: []
        };
    }
    
    componentDidMount() {
        axios.get('/api/projects/')
            .then(res => {
                this.setState({
                    projects: res.data
                });
            });
    }

    render() {
        return (
            <Fragment>
                <div className="hero">
                    <div className="overlay"></div>
                    <div className="bg-img"></div>
                    <div className="heading">
                        <h1>Portfolio</h1>
                        <p></p>
                    </div>
                </div>

                <div className="projects">
                    {this.state.projects.map(project => (
                        <div className="card project-item" key={project.slug} style={{ backgroundImage: `url(${project.image})` }}>
                            <div className="card-content project-image">
                                <h2 className="card-title">{project.title}</h2>
                                <p className="card-text">{project.short_description}</p>
                                <button className="btn">Read More..</button>
                            </div>
                        </div>
                    ))}
                </div>
            </Fragment>
        )
    }
}

export default Projects;