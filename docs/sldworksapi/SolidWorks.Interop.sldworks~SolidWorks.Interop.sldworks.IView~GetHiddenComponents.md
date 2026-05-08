# GetHiddenComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents`

Gets the hidden components in this drawing view.
Gets the hidden components in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHiddenComponents() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetHiddenComponents()
```

```

System.object GetHiddenComponents()
```

```

System.Object^ GetHiddenComponents(); 
```

#### Return Value

Array of hidden components

Example

[Get Components Hidden in Drawing View (VBA)](Get_Components_Hidden_In_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.md)  
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.md)  
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.md)  
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.md)
