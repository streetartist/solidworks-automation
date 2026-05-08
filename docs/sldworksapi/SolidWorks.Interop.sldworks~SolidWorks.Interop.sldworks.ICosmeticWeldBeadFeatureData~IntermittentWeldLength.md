# IntermittentWeldLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeldLength`

Gets or sets the length of the weld for intermittent weld beads.
Gets or sets the length of the weld for intermittent weld beads.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IntermittentWeldLength As System.Double
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double
 
instance.IntermittentWeldLength = value
 
value = instance.IntermittentWeldLength
```

```

System.double IntermittentWeldLength {get; set;}
```

```

property System.double IntermittentWeldLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length of weld for intermittent weld beads (see **Remarks**)

Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::IntermittentWeld](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.md) is true.

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)
