# Visible Property (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Visible`

Gets or sets the visibility state for this component for this drawing view.
Gets or sets the visibility state for this component for this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Visible As System.Boolean
```

```

Dim instance As IDrawingComponent
Dim value As System.Boolean
 
instance.Visible = value
 
value = instance.Visible
```

```

System.bool Visible {get; set;}
```

```

property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the component is visible, false if hidden

Remarks

Call the [IModelDoc2::Rebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.md) after setting this method.

Example

[Get Components' Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)  
[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)
