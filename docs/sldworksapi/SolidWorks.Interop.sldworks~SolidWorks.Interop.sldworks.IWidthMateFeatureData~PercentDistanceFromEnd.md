# PercentDistanceFromEnd Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~PercentDistanceFromEnd`

Gets or sets the percentage of distance from the end of this width mate.
Gets or sets the percentage of distance from the end of this width mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PercentDistanceFromEnd As System.Double
```

```

Dim instance As IWidthMateFeatureData
Dim value As System.Double
 
instance.PercentDistanceFromEnd = value
 
value = instance.PercentDistanceFromEnd
```

```

System.double PercentDistanceFromEnd {get; set;}
```

```

property System.double PercentDistanceFromEnd {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Percentage of distance from the end

Remarks

This property is valid only if [IWidthMateFeatureData::ConstraintType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType.md) is set to [swMateWidthOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateWidthOptions_e.html).swMateWidth\_Percent.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.md)  
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.md)
