# BendLineControlOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~BendLineControlOption`

Gets or sets the lofted bend line control options.
Gets or sets the lofted bend line control options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendLineControlOption As System.Integer
```

```

Dim instance As ILoftedBendsFeatureData
Dim value As System.Integer
 
instance.BendLineControlOption = value
 
value = instance.BendLineControlOption
```

```

System.int BendLineControlOption {get; set;}
```

```

property System.int BendLineControlOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Lofted bend line control options as defined in [swBendLineControlOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendLineControlOption_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.md)  
[ILoftedBendsFeatureData::CanCreateBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~CanCreateBendLines.md)  
[ILoftedBendsFeatureData::MaximumDeviation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~MaximumDeviation.md)  
[ILoftedBendsFeatureData::NumberOfBendLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~NumberOfBendLines.md)
