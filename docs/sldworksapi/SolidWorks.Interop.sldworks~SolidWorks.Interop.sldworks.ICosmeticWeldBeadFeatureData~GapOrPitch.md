# GapOrPitch Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GapOrPitch`

Gets or sets whether to use gap or pitch spacing for intermittent weld beads.
Gets or sets whether to use gap or pitch spacing for intermittent weld beads.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GapOrPitch As System.Boolean
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean
 
instance.GapOrPitch = value
 
value = instance.GapOrPitch
```

```

System.bool GapOrPitch {get; set;}
```

```

property System.bool GapOrPitch {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use gap spacing, false to use pitch spacing (see **Remarks**)

Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::IntermittentWeld](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.md) is true.

| If this property is... | Then to get and set the gap between the weld beads, call... |
| --- | --- |
| True | [ICosmeticWeldBeadFeatureData::Gap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Gap.md) |
| False | [ICosmeticWeldBeadFeatureData::Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Pitch.md) |

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)  
[ICosmeticWeldBeadFeatureData::IntermittentWeldLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeldLength.md)  
[ICosmeticWeldBeadFeatureData::Staggered Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Staggered.md)
