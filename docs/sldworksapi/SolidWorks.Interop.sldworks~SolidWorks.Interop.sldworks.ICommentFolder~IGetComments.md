# IGetComments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~IGetComments`

Gets all of the comments in this folder.
Gets all of the comments in this folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetComments( _
   ByVal Count As System.Integer _
) As Comment
```

```

Dim instance As ICommentFolder
Dim Count As System.Integer
Dim value As Comment
 
value = instance.IGetComments(Count)
```

```

Comment IGetComments( 
   System.int Count
)
```

```

Comment^ IGetComments( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of comments in the folder

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [IComment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.md) objects

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Example

Before calling this method, call [ICommentFolder::GetCommentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~GetCommentCount.md) before to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommentFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.md)  
[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.md)  
[ICommentFolder::GetComments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~GetComments.md)
