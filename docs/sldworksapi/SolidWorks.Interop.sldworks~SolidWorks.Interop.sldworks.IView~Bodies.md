# Bodies Property (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Bodies`

Gets or sets the bodies of a multibody part to show in the drawing view.
Gets or sets the bodies of a multibody part to show in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Bodies As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
instance.Bodies = value
 
value = instance.Bodies
```

```

System.object Bodies {get; set;}
```

```

property System.Object^ Bodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) of a multibody part

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
[IView::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBodiesCount.md)  
[IView::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBodies.md)  
[IView::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetBodies.md)
