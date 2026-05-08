# IntermittentWeld Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld`

Gets or sets whether to enable intermittent weld properties.
Gets or sets whether to enable intermittent weld properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IntermittentWeld As System.Boolean
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean
 
instance.IntermittentWeld = value
 
value = instance.IntermittentWeld
```

```

System.bool IntermittentWeld {get; set;}
```

```

property System.bool IntermittentWeld {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable intermittent weld properties, false to not (see **Remarks**)

Remarks

If this property is true, you can use the following properties:

- [ICosmeticWeldBeadFeatureData::Gap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Gap.md)
- [ICosmeticWeldBeadFeatureData::GapOrPitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GapOrPitch.md)
- [ICosmeticWeldBeadFeatureData::Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Pitch.md)
- [ICosmeticWeldBeadFeatureData::IntermittentWeldLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeldLength.md)
- [ICosmeticWeldBeadFeatureData::Staggered](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~Staggered.md)

Example

See [ICosmeticWeldBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)
