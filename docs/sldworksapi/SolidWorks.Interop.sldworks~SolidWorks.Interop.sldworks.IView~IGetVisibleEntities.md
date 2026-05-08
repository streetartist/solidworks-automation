# IGetVisibleEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities`

Obsolete. Superseded by IView::IGetVisibleEntities2.
Obsolete. Superseded by [IView::IGetVisibleEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVisibleEntities( _
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
 
value = instance.IGetVisibleEntities(LpViewComponent, EntityType, ViewEntityCount)
```

```

Entity IGetVisibleEntities( 
   Component2 LpViewComponent,
   System.int EntityType,
   System.int ViewEntityCount
)
```

```

Entity^ IGetVisibleEntities( 
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
:   Number of specified visible entities

#### Return Value

Array of the specified visible entities

Remarks

Visible entities are only those entities not completely obscured by other entities in the view.

Call [IView::GetVisibleEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount.md) before calling this method to get the value of ViewEntityCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.md)  
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md)  
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)  
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.md)  
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.md)
