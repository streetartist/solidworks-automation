# CanCreateBendLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~CanCreateBendLines`

Gets whether the bend lines parameters affect this lofted bend feature.
Gets whether the bend lines parameters affect this lofted bend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CanCreateBendLines() As System.Boolean
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean
 
value = instance.CanCreateBendLines()
```

```

System.bool CanCreateBendLines()
```

```

System.bool CanCreateBendLines(); 
```

#### Return Value

True if bend lines parameters affect this lofted bend feature, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::BendLineControlOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~BendLineControlOption.md)  
[ILoftedBendsFeatureData::MaximumDeviation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~MaximumDeviation.md)  
[ILoftedBendsFeatureData::NumberOfBendLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~NumberOfBendLines.md)
