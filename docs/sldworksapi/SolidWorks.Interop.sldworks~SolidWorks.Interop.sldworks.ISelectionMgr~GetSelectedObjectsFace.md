# GetSelectedObjectsFace Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsFace`

Gets the face of the specified selection if the specified selection is a silhouette edge.
Gets the face of the specified selection if the specified selection is a [silhouette edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedObjectsFace( _
   ByVal AtIndex As System.Integer, _
   ByVal Mark As System.Integer _
) As Face2
```

```

Dim instance As ISelectionMgr
Dim AtIndex As System.Integer
Dim Mark As System.Integer
Dim value As Face2
 
value = instance.GetSelectedObjectsFace(AtIndex, Mark)
```

```

Face2 GetSelectedObjectsFace( 
   System.int AtIndex,
   System.int Mark
)
```

```

Face2^ GetSelectedObjectsFace( 
   System.int AtIndex,
   System.int Mark
) 
```

#### Parameters

*AtIndex*
:   Index position within the current list of selected items, where AtIndex ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md)

*Mark*
:   - 1 = All selections regardless of marks

    0 = only the selections without marks

    Any other value = Value that was used to mark and select an object

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
