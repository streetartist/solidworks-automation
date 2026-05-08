# GetCommentCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~GetCommentCount`

Gets the number of comments in this folder.
Gets the number of comments in this folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCommentCount() As System.Integer
```

```

Dim instance As ICommentFolder
Dim value As System.Integer
 
value = instance.GetCommentCount()
```

```

System.int GetCommentCount()
```

```

System.int GetCommentCount(); 
```

#### Return Value

Number of comments in the folder

Remarks

Call this method before calling [ICommentFolder::IGetComments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~IGetComments.md) to determine the size of the array for that method.

Example

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)  
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)  
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommentFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.md)  
[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.md)
