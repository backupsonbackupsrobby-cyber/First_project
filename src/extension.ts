import * as vscode from 'vscode';
import { GitExtension, API as GitAPI, Repository } from './api/git';

export async function activate(context: vscode.ExtensionContext) {
    const gitExtension = vscode.extensions.getExtension<GitExtension>('vscode.git');

    if (!gitExtension) {
        vscode.window.showErrorMessage('Git extension not found');
        return;
    }

    if (!gitExtension.isActive) {
        await gitExtension.activate();
    }

    const git: GitAPI = gitExtension.exports.getAPI(1);

    // Example: list repositories
    git.repositories.forEach(repo => {
        console.log('Repo:', repo.rootUri.fsPath);
    });

    // Example of performing a commit operation
    if (git.repositories.length > 0) {
        const repo: Repository = git.repositories[0];
        try {
            await repo.add([]); // stage all changes
            await repo.commit('Automated commit from extension', { all: true });
            vscode.window.showInformationMessage('Committed changes to ' + repo.rootUri.fsPath);
        } catch (err) {
            console.error('Commit failed', err);
            vscode.window.showErrorMessage('Git commit failed: ' + err);
        }
    }
}

export function deactivate() {}