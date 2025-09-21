import { v4 as uuidv4 } from 'uuid';

const USER_COOKIE_NAME = 'user_guid';

export async function getUserId(): Promise<string> {
    const existingGuid = getCookie(USER_COOKIE_NAME);
    if (existingGuid) {
        return existingGuid;
    }
    const newGuid = uuidv4();
    setCookie(USER_COOKIE_NAME, newGuid, 365);

    await registerUser(newGuid)  // Add await here

    return newGuid;
}

function getCookie(name: string): string | null {
    const value = `; ${document.cookie}`
    const parts = value.split(`; ${name}=`)
    if (parts.length === 2) return parts.pop()!.split(';').shift()!
    return null
}

function setCookie(name: string, value: string, days: number) {
    const expires = new Date()
    expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000)
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`
}

async function registerUser(guid: string) {
    try {
        console.log('Attempting to register user:', guid);
        const response = await fetch('/api/users/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ guid }),
        });

        console.log('Response status:', response.status);

        if (!response.ok) {
            const errorData = await response.json();
            console.error('API Error:', errorData);
            return;
        }

        const data = await response.json();
        console.log('User registered successfully:', data);

    } catch (error) {
        console.error('Network error registering user:', error);
    }
}

export async function updateUserConfig(config: any) {
    const userId = getUserId();
    try {
        await fetch(`/api/users/${userId}/config/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ config }),
        });
    } catch (error) {
        console.error('Error updating user config:', error);
    }
}
