# Side Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Side`

Gets or sets how the weld bead is applied to selected faces or edges.
Gets or sets how the weld bead is applied to selected faces or edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Side As System.Integer
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Integer
 
instance.Side = value
 
value = instance.Side
```

```

System.int Side {get; set;}
```

```

property System.int Side {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Weld bead configuration as defined in [swCosmeticWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticWeldBeadSide_e.html)

Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::TangentPropagation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~TangentPropagation.md) is false.

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)
