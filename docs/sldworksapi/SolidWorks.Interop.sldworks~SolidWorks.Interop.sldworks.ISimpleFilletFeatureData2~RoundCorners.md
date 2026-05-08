# RoundCorners Property (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RoundCorners`

Gets or sets whether to round the corners of this simple fillet feature.
Gets or sets whether to round the corners of this simple fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RoundCorners As System.Boolean
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean
 
instance.RoundCorners = value
 
value = instance.RoundCorners
```

```

System.bool RoundCorners {get; set;}
```

```

property System.bool RoundCorners {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if simple fillet feature has round corners, false if not

Remarks

This property is valid only if [ISimpleFilletFeatureData2::CurvatureContinuous](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.md) is false, and at least two adjacent edges to fillet are selected.

Example

See [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)
