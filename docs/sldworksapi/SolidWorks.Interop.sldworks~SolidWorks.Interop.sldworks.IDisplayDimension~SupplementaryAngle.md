# SupplementaryAngle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SupplementaryAngle`

Changes the angle in the selected angular dimension to its supplementary angle.
Changes the angle in the selected angular dimension to its supplementary angle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SupplementaryAngle() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.SupplementaryAngle()
```

```

System.bool SupplementaryAngle()
```

```

System.bool SupplementaryAngle(); 
```

#### Return Value

True if the angle in the selected angular dimension changes to its supplementary angle, false if not

Remarks

| If the angle in the selected angular dimension is... | Then the supplementary angle is its... |
| --- | --- |
| >180 degrees (i.e., exterior) | Interior angle |
| <180 degrees (i.e., interior) | Exterior angle |

Example

[Change Angle to Supplementary Angle (C#)](Change_Angle_to_Supplementary_Angle_Example_CSharp.htm)  
[Change Angle to Supplementary Angle (VB.NET)](Change_Angle_to_Supplementary_Angle_Example_VBNET.htm)  
[Change Angle to Supplementary Angle (VBA)](Change_Angle_to_Supplementary_Angle_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IModelDocExtension::AddDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.md)  
[IModelDoc2::AddDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.md)
