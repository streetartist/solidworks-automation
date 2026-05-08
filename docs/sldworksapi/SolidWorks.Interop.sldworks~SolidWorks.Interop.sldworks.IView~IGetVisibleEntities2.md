# IGetVisibleEntities2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities2`

Gets the visible entities of the specified type for the specified component in this drawing view.
Gets the visible entities of the specified type for the specified component in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVisibleEntities2( _
   ByVal LpViewComponent As Component2, _
   ByVal EntityType As System.Integer, _
   ByVal ViewEntityCount As System.Integer _
) As Entity
```

```

Dim instance As IView
Dim LpViewComponent As Component2
Dim EntityType As System.Integer
Dim ViewEntityCount As System.Integer
Dim value As Entity
 
value = instance.IGetVisibleEntities2(LpViewComponent, EntityType, ViewEntityCount)
```

```

Entity IGetVisibleEntities2( 
   Component2 LpViewComponent,
   System.int EntityType,
   System.int ViewEntityCount
)
```

```

Entity^ IGetVisibleEntities2( 
   Component2^ LpViewComponent,
   System.int EntityType,
   System.int ViewEntityCount
) 
```

#### Parameters

*LpViewComponent*
:   [Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) from which to get EntityType

*EntityType*
:   Type of entity as defined in [swViewEntityType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewEntityType_e.html)

*ViewEntityCount*
:   Number of visible entities of EntityType in LpViewComponent

#### Return Value

- In-process, unmanaged C++: Pointer to an array of visible entities

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Visible entities are entities that are not completely obscured by other entities in the view.

Call [IView::GetVisibleEntityCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount2.md) before calling this method to get the value of ViewEntityCount.

The difference between this method and the now obsolete IView::IGetVisibleEntities method is that this method supports silhouette edges (EntityType = swViewEntityType\_e.swViewEntityType\_SilhouetteEdge).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetVisibleEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities2.md)  
[IView::GetVisibleComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md)  
[IView::GetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::GetHiddenComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.md)  
[IView::EnumHiddenComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)  
[IView::IGetVisibleComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.md)
