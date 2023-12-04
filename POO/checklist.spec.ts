import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import CheckboxList from './CheckboxList';

describe('CheckboxList', () => {
  it('renders checkboxes and handles selection', () => {
    const items = ['Item 1', 'Item 2', 'Item 3'];

    render(<CheckboxList items={items} />);
    
    const checkboxes = screen.getAllByRole('checkbox');
    expect(checkboxes).toHaveLength(items.length);

    fireEvent.click(checkboxes[0]);
    expect(checkboxes[0]).toBeChecked();

    fireEvent.click(checkboxes[1]);
    expect(checkboxes[1]).toBeChecked();

    fireEvent.click(checkboxes[0]);
    expect(checkboxes[0]).not.toBeChecked();
  });
});
