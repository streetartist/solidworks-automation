# GetVisibleEntityCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount`

Obsolete. Superseded by IView::GetVisibleEntityCount2.
Obsolete. Superseded by [IView::GetVisibleEntityCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleEntityCount( _
   ByVal LpViewComponent As Component2, _
   ByVal EntityType As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim LpViewComponent As Component2
Dim EntityType As System.Integer
Dim value As System.Integer
 
value = instance.GetVisibleEntityCount(LpViewComponent, EntityType)
```

```

System.int GetVisibleEntityCount( 
   Component2 LpViewComponent,
   System.int EntityType
)
```

```

System.int GetVisibleEntityCount( 
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

Number of specified entities in LpViewComponent

Remarks

Visible entities are only those entities not completely obscured by other entities in the view.

Call this method before calling [IView::IGetVisibleEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.md)  
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md)  
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.md)  
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.md)  
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)
