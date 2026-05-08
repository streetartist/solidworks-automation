# SetTitle2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetTitle2`

Sets the title of a new document.
Sets the title of a new document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTitle2( _
   ByVal NewTitle As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim NewTitle As System.String
Dim value As System.Boolean
 
value = instance.SetTitle2(NewTitle)
```

```

System.bool SetTitle2( 
   System.string NewTitle
)
```

```

System.bool SetTitle2( 
   System.String^ NewTitle
) 
```

#### Parameters

*NewTitle*
:   Name to give to the document window

#### Return Value

True if successfully renamed, false otherwise

Remarks

This title appears in the active window's title bar.

This method:

- Does not save this model document to disk; instead, it renames the document window.
- Is only valid when for a new document that has not yet been saved.
- Does not change the title of a document that has already been saved and exists on disk. If you want to rename an existing document, use ModelDoc2::SaveAs.

To retrieve the title of a document, use [IModelDoc2::GetTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetTitle.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
