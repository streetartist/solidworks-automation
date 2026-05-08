# FromToWeldLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToWeldLength`

Gets or sets the length of the weld.
Gets or sets the length of the weld.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FromToWeldLength As System.Double
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double
 
instance.FromToWeldLength = value
 
value = instance.FromToWeldLength
```

```

System.double FromToWeldLength {get; set;}
```

```

property System.double FromToWeldLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length of this weld (see **Remarks**)

Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::FromToLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToLength.md) is true.

The length of the weld is the distance from [ICosmeticWeldBeadFeatureData::FromToStartPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToStartPoint.md).

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)  
[ICosmeticWeldBeadFeatureData::FromToReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToReverse.md)
