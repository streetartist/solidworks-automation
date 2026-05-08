# SetVisible Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetVisible`

Sets the visibility of this drawing view.
Sets the visibility of this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetVisible( _
   ByVal Visible As System.Boolean, _
   ByVal DependentsToo As System.Boolean _
) 
```

```

Dim instance As IView
Dim Visible As System.Boolean
Dim DependentsToo As System.Boolean
 
instance.SetVisible(Visible, DependentsToo)
```

```

void SetVisible( 
   System.bool Visible,
   System.bool DependentsToo
)
```

```

void SetVisible( 
   System.bool Visible,
   System.bool DependentsToo
) 
```

#### Parameters

*Visible*
:   True to set the view to visible, false to not

*DependentsToo*
:   True to set the dependents of this view to visible, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetVisible Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisible.md)
