import React from 'react';
import { Route } from 'react-router-dom';

import Home from './components/Home';
import Contact from './components/Contact';
import Projects from './components/projects/Projects';
import About from './components/About';

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={Home} />
        <Route path='/about' component={About} />
        <Route path='/projects' component={Projects} />
        <Route path='/contact' component={Contact} />
    </div>
);

export default BaseRouter;