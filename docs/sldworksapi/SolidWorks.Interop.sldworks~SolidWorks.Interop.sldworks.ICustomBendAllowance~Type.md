# Type Property (ICustomBendAllowance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type`

Gets or sets the bend allowance type.
Gets or sets the bend allowance type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Type As System.Integer
```

```

Dim instance As ICustomBendAllowance
Dim value As System.Integer
 
instance.Type = value
 
value = instance.Type
```

```

System.int Type {get; set;}
```

```

property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Bend allowance type as defined in [swBendAllowanceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendAllowanceTypes_e.html)

Remarks

After setting [ICustomBendAllowance::BendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendAllowance.md), [ICustomBendAllowance::BendDeduction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendDeduction.md), [ICustomBendAllowance::BendTableFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendTableFile.md), [ICustomBendAllowance::BendCalculationTableFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendCalculationTableFile.md), and [ICustomBendAllowance::KFactor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~KFactor.md) use this property to set the value for the type. If you do not set this property last, the ICustomBendAllowance property set last automatically overrides any previously set custom bend allowance type.

See the ICustomBendAllowance Remarks.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

See the [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) examples.

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) examples.

Example

[Change Bend Radius of Sketch Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)  
[Set Custom Bend Deduction (VBA)](Set_Custom_Bend_Deduction_Example_VB.htm)  
[Set Custom Bend Deduction (VB.NET)](Set_Custom_Bend_Deduction_Example_VBNET.htm)  
[Set Custom Bend Deduction (C#)](Set_Custom_Bend_Deduction_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)  
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.md)
