# D1EndCondition Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition`

Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear pattern feature.
Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1EndCondition As System.Integer
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Integer
 
instance.D1EndCondition = value
 
value = instance.D1EndCondition
```

```

System.int D1EndCondition {get; set;}
```

```

property System.int D1EndCondition {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Spacing of pattern instances in Direction 1 as defined in [swPatternEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html)

Remarks

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Example

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)
