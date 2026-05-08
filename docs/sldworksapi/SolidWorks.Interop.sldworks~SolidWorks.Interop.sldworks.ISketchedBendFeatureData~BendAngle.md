# BendAngle Property (ISketchedBendFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~BendAngle`

Gets or sets the bend angle of this sketched bend.
Gets or sets the bend angle of this sketched bend.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendAngle As System.Double
```

```

Dim instance As ISketchedBendFeatureData
Dim value As System.Double
 
instance.BendAngle = value
 
value = instance.BendAngle
```

```

System.double BendAngle {get; set;}
```

```

property System.double BendAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.261799 <= Bend angle in increments of 0.261799 radians (15 degrees) <= 1.5708

Example

See the [ISketchedBendFeatureData::OverrideValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~OverrideValue.md) examples.

Example

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md)  
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.md)
