# MaximumDeviation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~MaximumDeviation`

Gets or sets the maximum deviation for the bend lines in a lofted bend feature.
Gets or sets the maximum deviation for the bend lines in a lofted bend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaximumDeviation As System.Double
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Double
 
instance.MaximumDeviation = value
 
value = instance.MaximumDeviation
```

```

System.double MaximumDeviation {get; set;}
```

```

property System.double MaximumDeviation {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Maximum deviation for the bend lines in a lofted bend feature

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::CanCreateBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~CanCreateBendLines.md)  
[ILoftedBendsFeatureData::BendLineControlOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~BendLineControlOption.md)  
[ILoftedBendsFeatureData::NumberOfBendLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~NumberOfBendLines.md)
