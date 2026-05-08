# IDeSelect Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect`

Obsolete. Superseded by ISelectionMgr::IDeSelect2.
Obsolete. Superseded by [ISelectionMgr::IDeSelect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeSelect( _
   ByVal Count As System.Integer, _
   ByRef AtIndex As System.Integer _
) As System.Integer
```

```

Dim instance As ISelectionMgr
Dim Count As System.Integer
Dim AtIndex As System.Integer
Dim value As System.Integer
 
value = instance.IDeSelect(Count, AtIndex)
```

```

System.int IDeSelect( 
   System.int Count,
   ref System.int AtIndex
)
```

```

System.int IDeSelect( 
   System.int Count,
   System.int% AtIndex
) 
```

#### Parameters

*Count*

*AtIndex*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
