import React from 'react'
import { Route, HashRouter, BrowserRouter, Switch, Redirect } from 'react-router-dom'
import { MainContainer, HomeContainer, FeedContainer } from 'containers'

export default function getRoutes(checkAuth) {
  return (
    <BrowserRouter>
      <Switch>
        <MainContainer>
        <Route exact path='/' render={() => {
          return checkAuth() ? <HomeContainer /> : <HomeContainer /> }} />
        <Route path='/feed' render={() => { return <FeedContainer /> }} />
        </MainContainer>
      </Switch>
    </BrowserRouter>
  )
}
