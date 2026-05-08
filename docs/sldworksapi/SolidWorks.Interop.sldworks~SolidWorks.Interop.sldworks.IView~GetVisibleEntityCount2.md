# GetVisibleEntityCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount2`

Gets the number of visible entities of the specified type for the specified component in this drawing view.
Gets the number of visible entities of the specified type for the specified component in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleEntityCount2( _
   ByVal LpViewComponent As Component2, _
   ByVal EntityType As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim LpViewComponent As Component2
Dim EntityType As System.Integer
Dim value As System.Integer
 
value = instance.GetVisibleEntityCount2(LpViewComponent, EntityType)
```

```

System.int GetVisibleEntityCount2( 
   Component2 LpViewComponent,
   System.int EntityType
)
```

```

System.int GetVisibleEntityCount2( 
   Component2^ LpViewComponent,
   System.int EntityType
) 
```

#### Parameters

*LpViewComponent*
:   [Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) from which to get the visible EntityType

*EntityType*
:   Type of entity as defined in [swViewEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)

#### Return Value

Number of visible entities of EntityType in LpViewComponent

Remarks

Visible entities are entities that are not completely obscured by other entities in the view.

Call this method to get the size of the array returned by [IView::IGetVisibleEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities2.md).

The difference between this method and the now obsolete IView::GetVisibleEntityCount method is that this method gets the correct number of silhouette edges (EntityType = swViewEntityType\_e.swViewEntityType\_SilhouetteEdge).

Example

[Hide and Show All Edges in Drawing View (C#)](Hide_and_Show_All_Ediges_in_Drawing_View_Example_CSharp.htm)  
[Hide and Show All Edges in Drawing View (VB.NET)](Hide_and_Show_All_Ediges_in_Drawing_View_Example_VBNET.htm)  
[Hide and Show All Edges in Drawing View (VBA)](Hide_and_Show_All_Edges_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetVisibleEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities2.md)  
[IView::GetVisibleComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md)  
[IView::GetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::IGetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.md)  
[IView::GetHiddenComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.md)  
[IView::EnumHiddenComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)
