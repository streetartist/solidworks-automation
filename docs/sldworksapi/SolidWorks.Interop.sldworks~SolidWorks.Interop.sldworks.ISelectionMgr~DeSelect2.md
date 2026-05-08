# DeSelect2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2`

Deselects the specified entity.
Deselects the specified entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeSelect2( _
   ByVal AtIndex As System.Object, _
   ByVal Mark As System.Integer _
) As System.Integer
```

```

Dim instance As ISelectionMgr
Dim AtIndex As System.Object
Dim Mark As System.Integer
Dim value As System.Integer
 
value = instance.DeSelect2(AtIndex, Mark)
```

```

System.int DeSelect2( 
   System.object AtIndex,
   System.int Mark
)
```

```

System.int DeSelect2( 
   System.Object^ AtIndex,
   System.int Mark
) 
```

#### Parameters

*AtIndex*
:   Index position within the current list of selected items where index ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md) (see **Remarks**)

*Mark*
:   - -1 = All selections regardless of marks

    0 = only the selections without marks

    Any other value = Value that was used to mark and select an object

#### Return Value

1 if the specified entity is deselected, 0 if not

Remarks

If running SOLIDWORKS x64, then you must declare AtIndex as a Long in VBA.

AtIndex should be either an array of 32-bit integers or a single 32-bit integer. See [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm) for details about data types.

Example

[Deselect Marked Entity (C#)](Deselect_Marked_Entity_Example_CSharp.htm)  
[Deselect Marked Entity (VB.NET)](Deselect_Marked_Entity_Example_VBNET.htm)  
[Deselect Marked Entity (VBA)](Deselect_Marked_Entity_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::GetSelectedObject6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)  
[ISelectionMgr::GetSelectedObjectCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md)  
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md)  
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.md)  
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md)  
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.md)  
[ISelectionMgr::ISelectionMgr::GetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.md)  
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.md)  
[ISelectionMgr::IDeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.md)  
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.md)  
[ISelectionMgr::IGetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.md)  
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.md)  
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.md)
