# GetSelectedObjectsComponent4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4`

Gets the selected component in an assembly or drawing.
Gets the selected component in an assembly or drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedObjectsComponent4( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Object
```

```

Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As System.Object
 
value = instance.GetSelectedObjectsComponent4(Index, Mark)
```

```

System.object GetSelectedObjectsComponent4( 
   System.int Index,
   System.int Mark
)
```

```

System.Object^ GetSelectedObjectsComponent4( 
   System.int Index,
   System.int Mark
) 
```

#### Parameters

*Index*
:   Index position within the current list of selected items, where the index ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md) (see **Remarks**)

*Mark*
:   - -1 = All selections regardless of marks

    0 = Only the selections without marks

    Any other value = Value that was used to mark and select an object

#### Return Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) or [Drawing component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)

Remarks

The index starts at 1, even when using C++. However, if you specify -1 for the Index argument, then the Mark argument is ignored and the dynamically highlighted component is selected if dynamic highlighting is turned on. See also IAssemblyDoc event [DynamicHighlightNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.md).

The difference between this method and the now obsolete [ISelectionMgr::GetSelectedObjectsComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md) is that ISelectionMgr::GetSelectedObjectsComponent4 can return an [IDrawingComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md) and ISelectionMgr::GetSelectedObjectsComponent3 cannot.

Example

[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)  
[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)  
[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)  
[Select Drawing Component (C#)](Select_Drawing_Component_Example_CSharp.htm)  
[Select Drawing Component (VB.NET)](Select_Drawing_Component_Example_VBNET.htm)  
[Select Drawing Component (VBA)](Select_Drawing_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::DeSelect2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.md)  
[ISelectionMgr::GetSelectedObject6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)  
[ISelectionMgr::GetSelectedObjectLoop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md)  
[ISelectionMgr::GetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.md)  
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.md)  
[ISelectionMgr::GetSelectedObjectType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md)  
[ISelectionMgr::GetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.md)  
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.md)  
[ISelectionMgr::IDeSelect2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.md)  
[ISelectionMgr::IGetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.md)  
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.md)  
[IComponent2::Select4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select4.md)  
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.md)  
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.md)
