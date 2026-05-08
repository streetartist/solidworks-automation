# FlipDimension Property (IWidthMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~FlipDimension`

Gets or sets whether to move entities to opposite sides of the dimension of this width mate.
Gets or sets whether to move entities to opposite sides of the dimension of this width mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlipDimension As System.Boolean
```

```

Dim instance As IWidthMateFeatureData
Dim value As System.Boolean
 
instance.FlipDimension = value
 
value = instance.FlipDimension
```

```

System.bool FlipDimension {get; set;}
```

```

property System.bool FlipDimension {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the dimension, false to not (see **Remarks**)

Remarks

This property is valid only if [IWidthMateFeatureData::ConstraintType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType.md) is set to [swMateWidthOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateWidthOptions_e.html).swMateWidth\_Dimension or swMateWidth\_Percent.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.md)  
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.md)
