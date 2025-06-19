/**
 * @jest-environment jsdom
 */
import '@testing-library/jest-dom';
import { fireEvent, getByText, getByLabelText, screen } from '@testing-library/dom';

// Mock fetch
beforeEach(() => {
  global.fetch = jest.fn();
  document.body.innerHTML = `
    <div id="activities-list"></div>
    <select id="activity"></select>
    <form id="signup-form"></form>
    <div id="message" class="hidden"></div>
  `;
});

afterEach(() => {
  jest.resetAllMocks();
});

test('renders activities and participants', async () => {
  const activities = {
    "Chess Club": {
      description: "desc", schedule: "sched", max_participants: 2, participants: ["a@b.com"]
    }
  };
  fetch.mockResolvedValueOnce({ json: () => Promise.resolve(activities) });
  await import('../src/static/app.js');
  // Wait for DOM update
  await new Promise(r => setTimeout(r, 10));
  expect(document.querySelector('.activity-card')).toBeInTheDocument();
  expect(document.querySelector('.participant-item')).toHaveTextContent('a@b.com');
});

test('signup form submits and shows message', async () => {
  fetch.mockResolvedValueOnce({ json: () => Promise.resolve({
    "Chess Club": { description: "desc", schedule: "sched", max_participants: 2, participants: [] }
  }) });
  await import('../src/static/app.js');
  // Wait for DOM update
  await new Promise(r => setTimeout(r, 10));
  fetch.mockResolvedValueOnce({ ok: true, json: () => Promise.resolve({ message: 'Signed up!' }) });
  document.body.innerHTML += `
    <input id="email" value="test@mergington.edu" />
    <select id="activity"><option value="Chess Club">Chess Club</option></select>
    <form id="signup-form"></form>
    <div id="message" class="hidden"></div>
  `;
  const signupForm = document.getElementById('signup-form');
  fireEvent.submit(signupForm);
  await new Promise(r => setTimeout(r, 10));
  expect(document.getElementById('message')).toHaveTextContent('Signed up!');
});
