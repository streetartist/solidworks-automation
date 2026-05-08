# UseDefaultBendAllowance Property (ISketchedBendFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseDefaultBendAllowance`

Gets or sets whether to use the default bend allowance for this sketched bend.
Gets or sets whether to use the default bend allowance for this sketched bend.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDefaultBendAllowance As System.Boolean
```

```

Dim instance As ISketchedBendFeatureData
Dim value As System.Boolean
 
instance.UseDefaultBendAllowance = value
 
value = instance.UseDefaultBendAllowance
```

```

System.bool UseDefaultBendAllowance {get; set;}
```

```

property System.bool UseDefaultBendAllowance {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True uses the default bend allowance, false does not

Example

See [ISketchedBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md) examples.

Example

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)  
[Set Custom Bend Deduction (VBA)](Set_Custom_Bend_Deduction_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md)  
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.md)  
[ISketchedBendFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetCustomBendAllowance.md)  
[ISketchedBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetCustomBendAllowance.md)
