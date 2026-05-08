# NumberOfBendLines Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~NumberOfBendLines`

Gets or sets the number of bend lines in this lofted bend feature.
Gets or sets the number of bend lines in this lofted bend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NumberOfBendLines As System.Integer
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Integer
 
instance.NumberOfBendLines = value
 
value = instance.NumberOfBendLines
```

```

System.int NumberOfBendLines {get; set;}
```

```

property System.int NumberOfBendLines {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of bend lines in this lofted bend feature

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::CanCreateBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~CanCreateBendLines.md)  
[ILoftedBendsFeatureData::BendLineControlOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~BendLineControlOption.md)  
[ILoftedBendsFeatureData::MaximumDeviation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~MaximumDeviation.md)
