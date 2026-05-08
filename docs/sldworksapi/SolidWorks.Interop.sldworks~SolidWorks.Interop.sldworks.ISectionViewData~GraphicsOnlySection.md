# GraphicsOnlySection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GraphicsOnlySection`

Gets or sets whether to generate a graphics-only section view.
Gets or sets whether to generate a graphics-only section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GraphicsOnlySection As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.GraphicsOnlySection = value
 
value = instance.GraphicsOnlySection
```

```

System.bool GraphicsOnlySection {get; set;}
```

```

property System.bool GraphicsOnlySection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to generate a graphics-only section view, false to not

Remarks

This property corresponds to the **Graphics-only section** check box on the Section View PropertyManager page.

When a section view is created, the model is rebuilt. If the model is very large and complex, rebuilding the model slows down the creation of the section view. This property indicates whether to rebuild the model when a section view is created. When this property is set to true:

- **Keep cap color** check box is selected and inactivated on the Section View PropertyManager page.
- [ISectionViewData::KeepCapColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~KeepCapColor.md) returns only true; setting to false is ignored.
- Model is not rebuilt, and the section view is quickly generated.

Example

[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)  
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)  
[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)
