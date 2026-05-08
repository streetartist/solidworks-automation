# ArcExtensionLineOrOppositeSide Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ArcExtensionLineOrOppositeSide`

Gets or sets whether to attach or extend the radial dimension leader on this radial display dimension.
Gets or sets whether to attach or extend the radial dimension leader on this radial display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ArcExtensionLineOrOppositeSide As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.ArcExtensionLineOrOppositeSide = value
 
value = instance.ArcExtensionLineOrOppositeSide
```

```

System.bool ArcExtensionLineOrOppositeSide {get; set;}
```

```

property System.bool ArcExtensionLineOrOppositeSide {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

| If... | Then... |
| --- | --- |
| True | - Attach the radial dimension leader to the arc extension line.    - or - - If the radial dimension leader encounters arc geometry, then extend the radial dimension leader to the opposite side of the arc. |
| False | Neither attach nor extend the radial dimension leader. |

Remarks

This property is only valid for radial display dimensions.

Example

[Set Radial Dimension Leader (C#)](Edit_Radial_Dimension_Example_CSharp.htm)  
[Set Radial Dimension Leader (VB.NET)](Edit_Radial_Dimension_Example_VBNET.htm)  
[Set Radial Dimension Leader (VBA)](Edit_Radial_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IModelDoc2::AddRadialDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.md)
