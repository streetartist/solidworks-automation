# TangentPropagation Property (ICosmeticWeldBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~TangentPropagation`

Gets or sets whether to apply the weld bead to all edges that are tangent to the selected faces or edges.
Gets or sets whether to apply the weld bead to all edges that are tangent to the selected faces or edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TangentPropagation As System.Boolean
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean
 
instance.TangentPropagation = value
 
value = instance.TangentPropagation
```

```

System.bool TangentPropagation {get; set;}
```

```

property System.bool TangentPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to apply the weld bead to all edges that are tangent to the selected faces or edges, false to not (see **Remarks**)

Remarks

| If this property is... | Then use... |
| --- | --- |
| True | [ICosmeticWeldBeadFeatureData::FromToLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToLength.md) to enable the from/to length properties |
| False | [ICosmeticWeldBeadFeatureData::Side](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Side.md) to define how to apply the weld bead to the selected faces or edges |

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)
