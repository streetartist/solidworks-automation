# FromToStartPoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToStartPoint`

Gets or sets the position of the first weld bead with respect to the end of the selected face or edge.
Gets or sets the position of the first weld bead with respect to the end of the selected face or edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FromToStartPoint As System.Double
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double
 
instance.FromToStartPoint = value
 
value = instance.FromToStartPoint
```

```

System.double FromToStartPoint {get; set;}
```

```

property System.double FromToStartPoint {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Position of the first weld bead (see **Remarks**)

Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::FromToLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToLength.md) is true.

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)  
[ICosmeticWeldBeadFeatureData::FromToReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToReverse.md)  
[ICosmeticWeldBeadFeatureData::FromToWeldLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToWeldLength.md)
