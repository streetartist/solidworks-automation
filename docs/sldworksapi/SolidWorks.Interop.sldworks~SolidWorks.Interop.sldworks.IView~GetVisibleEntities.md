# GetVisibleEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities`

Obsolete. Superseded by IView::GetVisibleEntities2.
Obsolete. Superseded by [IView::GetVisibleEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleEntities( _
   ByVal LpViewComponent As Component2, _
   ByVal EntityType As System.Integer _
) As System.Object
```

```

Dim instance As IView
Dim LpViewComponent As Component2
Dim EntityType As System.Integer
Dim value As System.Object
 
value = instance.GetVisibleEntities(LpViewComponent, EntityType)
```

```

System.object GetVisibleEntities( 
   Component2 LpViewComponent,
   System.int EntityType
)
```

```

System.Object^ GetVisibleEntities( 
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

Array of the specified visible entities

Remarks

Visible entities are only those entities not completely obscured by other entities in the view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetVisibleEntityCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount.md)  
[IView::IGetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.md)  
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.md)  
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md)  
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.md)  
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)
