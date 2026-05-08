# MaximumAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~MaximumAngle`

Gets or sets the maximum angle of this limit angle mate.
Gets or sets the maximum angle of this limit angle mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaximumAngle As System.Double
```

```

Dim instance As IAngleMateFeatureData
Dim value As System.Double
 
instance.MaximumAngle = value
 
value = instance.MaximumAngle
```

```

System.double MaximumAngle {get; set;}
```

```

property System.double MaximumAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Maximum angle in radians

Remarks

This property is valid only if [IAngleMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~IsAdvancedMate.md) is set to true.

Example

See the [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.md)  
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.md)  
[IAngleMateFeatureData::Angle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~Angle.md)
