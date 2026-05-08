# GetSelectedCoordSysElement Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedCoordSysElement`

Gets the selected coordinate system element.
Gets the selected coordinate system element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedCoordSysElement( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Object
```

```

Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As System.Object
 
value = instance.GetSelectedCoordSysElement(Index, Mark)
```

```

System.object GetSelectedCoordSysElement( 
   System.int Index,
   System.int Mark
)
```

```

System.Object^ GetSelectedCoordSysElement( 
   System.int Index,
   System.int Mark
) 
```

#### Parameters

*Index*
:   Index position within the current list of selected items, where Index ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md) (see **Remarks**)

*Mark*
:   - -1 = All selections regardless of marks

    - 0 = only the selections without marks

    Any other value = Value that was used to mark and select an object

#### Return Value

[ICoordinateSystemElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement.md)

Remarks

After calling this method, call [ISelectionMgr::IsCoordSysElementSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsCoordSysElementSelected.md).

Example

See the [ICoordinateSystemElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
