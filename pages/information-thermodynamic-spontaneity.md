title: Counting With Chemicals
subtitle:  Information Processing and Thermodynamic Sponaneity
date: February 1, 2012
tags: [information-theory, language, communication]

I suspect there have been much more thorough and academic treaments of the subject than the present document, but perhaps through it's disregard for convention it will be useful by illuminating underappreciated, practical aspects of the relationship between information and thermodynamics.

### Imagining Computation Without Energy
The most accessible way that I've found to grasp the role of thermodynamics in computation is to imagine trying to carry out some algorithm which doesn't require the use of energy.  This is kind of tricky at first, because the standard context for computation is the electronic circuit which only some of us understand, and fewer understand intuitively.  However, if we consider system for which we have a better intuition, and can imagine those systems doing some sort of computation, then we can more directly grasp the role of thermodynamics in information processing.  First, consider metabolic network.  While not the standard context for thinking about information processing, it's basically what your body does.

### Metabolic Networks

#### Sequential Computation
Imagine your body is trying to carry out some operation like counting, where order matters.  I have no idea whether the human body every tries to do abstract counting, or if it does, how it goes about it, but let's say that we're trying to count the number of times a chemical concentration crosses some threshold. For fun, let's imagine that the body is trying to learn to predict that you don't have coffees on Wednesday.  It knows you didn't have coffee today, and it needs to keep count of the number of caffeine bursts so that it doesn't give you a headache next Wednesday.  To make things more plausible (maybe not that plausible...), let's imagine you are an immortal being, where you have been drinking coffee 6 out of 7 days a week, always skipping Wednesday, for a few millenia&mdash;some metabolic counting might even arise over this period, through some variety of ontogenic natural selection.

A simple chemical counting algorithm would invovle keeping some state which symbolizes a number, and then changing the state with each new caffeine buurst.  So let's imagine we have 7 species of molecules which can sequentially be turned into one another.  Here is where the thermodynamic spontanaeity comes in! If we didn't have some potential wells at each state, how would it mean anything to be in a particular state?
