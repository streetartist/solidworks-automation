# GetSelectionPointInSketchSpace2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2`

Gets the selection point projected on to the active sketch and returned in sketch space.
Gets the selection point projected on to the active sketch and returned in sketch space.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectionPointInSketchSpace2( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Object
```

```

Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As System.Object
 
value = instance.GetSelectionPointInSketchSpace2(Index, Mark)
```

```

System.object GetSelectionPointInSketchSpace2( 
   System.int Index,
   System.int Mark
)
```

```

System.Object^ GetSelectionPointInSketchSpace2( 
   System.int Index,
   System.int Mark
) 
```

#### Parameters

*Index*
:   Index position with in the current list of selected items, where AtIndex ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md) (see **Remarks**)

*Mark*
:   - -1 = All selections regardless of marks
    - 0 = only the selections without marks
    - Any other value that was used to mark and select an object

#### Return Value

Array of 3 doubles (x,y,z)

Remarks

The selection point is projected on to the currently active sketch, resulting in a z value of 0.00.

If a sketch is not currently active, then the return value is the same as that returned by [ISelectionMgr::GetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.md) or [ISelectionMgr::IGetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.md). You can determine if a sketch is active by checking for a Nothing or null return value from [IModelDoc2::GetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetActiveSketch2.md) or [IModelDoc2::IGetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetActiveSketch2.md).

The index starts at 1. However, if you specify -1 for the Index argument, then the Mark argument is ignored and the dynamically highlighted view is selected if dynamic highlighting is turned on. See also IAssemblyDoc event [DynamicHighlightNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.md), IDrawingDoc event [DynamicHighlightNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DynamicHighlightNotifyEventHandler.md), and IPartDoc event [DynamicHighlightNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DynamicHighlightNotifyEventHandler.md).

Example

[Create Line From User Selection (VBA)](Create_Line_From_User_Selection_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.md)  
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.md)  
[ISelectionMgr::GetSelectedObjectCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md)  
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md)  
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.md)  
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md)  
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.md)  
[ISelectionMgr::GetSelectedObjectType3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md)  
[ISelectionMgr::IDeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.md)  
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.md)  
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.md)  
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.md)
