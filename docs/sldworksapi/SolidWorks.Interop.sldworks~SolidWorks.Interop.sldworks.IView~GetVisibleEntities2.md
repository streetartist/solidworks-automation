# GetVisibleEntities2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities2`

Gets the visible entities of the specified type for the specified component in this drawing view.
Gets the visible entities of the specified type for the specified component in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleEntities2( _
   ByVal LpViewComponent As Component2, _
   ByVal EntityType As System.Integer _
) As System.Object
```

```

Dim instance As IView
Dim LpViewComponent As Component2
Dim EntityType As System.Integer
Dim value As System.Object
 
value = instance.GetVisibleEntities2(LpViewComponent, EntityType)
```

```

System.object GetVisibleEntities2( 
   Component2 LpViewComponent,
   System.int EntityType
)
```

```

System.Object^ GetVisibleEntities2( 
   Component2^ LpViewComponent,
   System.int EntityType
) 
```

#### Parameters

*LpViewComponent*
:   [Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) from which to get EntityType

*EntityType*
:   Type of entity as defined in [swViewEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)

#### Return Value

Array of the visible entities of EntityType in LpViewComponent

Remarks

Visible entities are entities that are not completely obscured by other entities in the view.

The difference between this method and the now obsolete IView::GetVisibleEntities method is that this method supports silhouette edges (EntityType = swViewEntityType\_e.swViewEntityType\_SilhouetteEdge).

Example

[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)  
[Get Visible Components and Entities in Drawing View (VB.NET)](Get_Visible_Components_and_Entites_in_a_Drawing_View_Example_VBNET.htm)  
[Get Visible Components and Entities in Drawing View (C#)](Get_Visible_Components_and_Entites_in_a_Drawing_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetVisibleEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities2.md)  
[IView::GetVisibleEntityCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount2.md)  
[IView::GetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::GetVisibleComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md)  
[IView::IGetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.md)  
[IView::GetHiddenComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.md)  
[IView::EnumHiddenComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)  
[IView::GetVisibleDrawingComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleDrawingComponents.md)
