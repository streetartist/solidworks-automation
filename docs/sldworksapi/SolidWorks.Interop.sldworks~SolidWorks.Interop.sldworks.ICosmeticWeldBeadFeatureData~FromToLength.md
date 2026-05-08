# FromToLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToLength`

Gets or sets whether to enable the from/to length properties.
Gets or sets whether to enable the from/to length properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FromToLength As System.Boolean
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean
 
instance.FromToLength = value
 
value = instance.FromToLength
```

```

System.bool FromToLength {get; set;}
```

```

property System.bool FromToLength {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable the from/to length properties, false to not (see **Remarks**)

Remarks

This property is valid only if:

- [ICosmeticWeldBeadFeatureData::TangentPropagation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~TangentPropagation.md) is true

     - or -

- [ICosmeticWeldBeadFeatureData::Side](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Side.md) is either [swCosmeticWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticWeldBeadSide_e.html).swCosmeticWeldBeadSide\_Selection or swCosmeticWeldBeadSide\_e.swCosmeticWeldBeadSide\_BothSides.

If this property is true, you can use the following properties:

- [ICosmeticWeldBeadFeatureData::FromToStartPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToStartPoint.md)
- [ICosmeticWeldBeadFeatureData::FromToReverse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToReverse.md)
- [ICosmeticWeldBeadFeatureData::FromToWeldLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToWeldLength.md)

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)
