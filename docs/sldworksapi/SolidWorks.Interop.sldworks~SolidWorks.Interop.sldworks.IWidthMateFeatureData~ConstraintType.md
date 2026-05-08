# ConstraintType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType`

Gets or sets the type of constraint for this width mate.
Gets or sets the type of constraint for this width mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConstraintType As System.Integer
```

```

Dim instance As IWidthMateFeatureData
Dim value As System.Integer
 
instance.ConstraintType = value
 
value = instance.ConstraintType
```

```

System.int ConstraintType {get; set;}
```

```

property System.int ConstraintType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Constraint type as defined in [swMateWidthOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateWidthOptions_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.md)  
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.md)  
[IWidthMateFeatureData::DistanceFromEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~DistanceFromEnd.md)  
[IWidthMateFeatureData::FlipDimension Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~FlipDimension.md)  
[IWidthMateFeatureData::PercentDistanceFromEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~PercentDistanceFromEnd.md)
