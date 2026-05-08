# Gap Property (ICosmeticWeldBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Gap`

Gets or sets the gap between intermittent weld beads.
Gets or sets the gap between intermittent weld beads.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Gap As System.Double
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double
 
instance.Gap = value
 
value = instance.Gap
```

```

System.double Gap {get; set;}
```

```

property System.double Gap {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Gap between intermittent weld beads (see **Remarks**)

Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::GapOrPitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GapOrPitch.md) is true and [ICosmeticWeldBeadFeatureData::IntermittentWeld](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.md) is true.

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)
