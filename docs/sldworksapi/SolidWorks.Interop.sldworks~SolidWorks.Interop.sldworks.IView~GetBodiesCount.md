# GetBodiesCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBodiesCount`

Gets the number of bodies of a multibody part in the drawing view.
Gets the number of bodies of a multibody part in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodiesCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetBodiesCount()
```

```

System.int GetBodiesCount()
```

```

System.int GetBodiesCount(); 
```

#### Return Value

Number of bodies of a multibody part in the view

Example

[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)  
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)  
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IView::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBodies.md)  
[IView::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetBodies.md)  
[IView::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Bodies.md)
