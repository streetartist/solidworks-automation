# GetSelectionPoint2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2`

Gets the selected point in model space coordinates from the currently selected object.
Gets the selected point in model space coordinates from the currently selected object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectionPoint2( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Object
```

```

Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As System.Object
 
value = instance.GetSelectionPoint2(Index, Mark)
```

```

System.object GetSelectionPoint2( 
   System.int Index,
   System.int Mark
)
```

```

System.Object^ GetSelectionPoint2( 
   System.int Index,
   System.int Mark
) 
```

#### Parameters

*Index*
:   Index position with in the current list of selected items, where AtIndex ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md) (see **Remarks**)

*Mark*
:   - -1 = All selections regardless of marks

    0 = only the selections without marks

    Any other value = Value that was used to mark and select an object

#### Return Value

Array of 3 doubles (x,y,z)

Remarks

The index starts at 1, even when using C++. However, if you specify -1 for the Index argument, then the Mark argument is ignored and the dynamically highlighted view is selected if dynamic highlighting is turned on. See also IAssemblyDoc event [DynamicHighlightNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.md), IDrawingDoc event [DynamicHighlightNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DynamicHighlightNotifyEventHandler.md), and IPartDoc event [DynamicHighlightNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DynamicHighlightNotifyEventHandler.md).

The point returned from ISelectionMgr::GetSelectionPoint2 or [ISelectionMgr::IGetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.md) cannot lie on the object that was selected. For example, the user can select an edge when the edge is within the pick radius of their mouse cursor. However, to get a point on a face, edge, or vertex, use that object's GetClosestPointOn method.

To do this, get the [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), or [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) object using the [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) method, and then use that object to call GetClosestPointOn. Pass the X,Y,Z values returned from ISelectionMgr::GetSelectionPoint2 or ISelectionMgr::IGetSelectionPoint2, and the GetClosestPointOn method will return the closest X,Y,Z point that is on the face, edge, or vertex.

If the selected object is sketch geometry, then the coordinates returned are in sketch space. The coordinates are 2D and related to the origin of the sketch that owns the selected geometry.

Example

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)  
[Create Drag Arrow Manipulator (C#)](Create_Drag_Arrow_Manipulator_Example_CSharp.htm)  
[Create Drag Arrow Manipulator (VB.NET)](Create_Drag_Arrow_Manipulator_Example_VBNET.htm)  
[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.md)  
[ISelectionMgr::GetSelectedObjectLoop2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md)  
[ISelectionMgr::GetSelectedObjectMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.md)  
[ISelectionMgr::GetSelectedObjectsComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md)  
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.md)  
[ISelectionMgr::GetSelectedObjectType3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md)  
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.md)  
[ISelectionMgr::IDeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.md)  
[ISelectionMgr::DeSelect2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.md)  
[ISelectionMgr::SetSelectionPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.md)  
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.md)  
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.md)
