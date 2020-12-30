#!/usr/bin/env python3

from aws_cdk import core

from manpower.manpower_stack import ManpowerStack


app = core.App()
ManpowerStack(app, "manpower")

app.synth()
