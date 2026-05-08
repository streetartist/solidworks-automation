# IGetVisibleComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents`

Gets the visible components in this drawing view.
Gets the visible components in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVisibleComponents( _
   ByVal ViewComponentCount As System.Integer _
) As Component2
```

```

Dim instance As IView
Dim ViewComponentCount As System.Integer
Dim value As Component2
 
value = instance.IGetVisibleComponents(ViewComponentCount)
```

```

Component2 IGetVisibleComponents( 
   System.int ViewComponentCount
)
```

```

Component2^ IGetVisibleComponents( 
   System.int ViewComponentCount
) 
```

#### Parameters

*ViewComponentCount*
:   Number of visible components

#### Return Value

Visible [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in this drawing view

Remarks

Visible components are only those components not completely obscured by other components in the view.

Call [IView::GetVisibleComponentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md) before calling this method to get the value of ViewComponentCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)  
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.md)  
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.md)  
[IView::GetVisibleEntityCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount.md)  
[IView::IGetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.md)
