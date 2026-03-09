/*
 * This file is a subset of the Git API definitions from the VS Code
 * repository.  Copy/paste the relevant pieces you need for your extension.
 *
 * Source (at time of writing):
 * https://github.com/microsoft/vscode/blob/main/extensions/git/src/api/git.d.ts
 */

import * as vscode from 'vscode';

export interface GitExtension {
    readonly enabled: boolean;
    readonly repositories: Repository[];
    getAPI(version: number): API;
}

export interface API {
    readonly repositories: Repository[];
    // other API members omitted for brevity
}

export interface Repository {
    readonly rootUri: vscode.Uri;
    readonly inputBox: InputBox;
    readonly state: RepositoryState;

    add(pathspec: string[]): Thenable<void>;
    commit(message: string, opts?: CommitOptions): Thenable<void>;
    // ...more methods (push, pull, etc.)
}

export interface InputBox {
    value: string;
}

export interface RepositoryState {
    // see full definition in original file if needed
    readonly workingTreeChanges: Change[];
    readonly indexChanges: Change[];
}

export interface Change {
    readonly uri: vscode.Uri;
    // ...
}

export interface CommitOptions {
    readonly all?: boolean;
    readonly amend?: boolean;
}
