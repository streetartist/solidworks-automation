# GetSelectedObjectLoop Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop`

Obsolete. Superseded by ISelectionMgr::GetSelectedObjectLoop2.
Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedObjectLoop( _
   ByVal AtIndex As System.Integer _
) As Loop2
```

```

Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim value As Loop2
 
value = instance.GetSelectedObjectLoop(AtIndex)
```

```

Loop2 GetSelectedObjectLoop( 
   System.int AtIndex
)
```

```

Loop2^ GetSelectedObjectLoop( 
   System.int AtIndex
) 
```

#### Parameters

*AtIndex*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
