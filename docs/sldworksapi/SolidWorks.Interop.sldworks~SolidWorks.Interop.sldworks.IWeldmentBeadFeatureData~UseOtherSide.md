# UseOtherSide Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~UseOtherSide`

Gets or sets whether to apply the weld bead to both sides of the intersecting faces.
Gets or sets whether to apply the weld bead to both sides of the intersecting faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseOtherSide As System.Boolean
```

```

Dim instance As IWeldmentBeadFeatureData
Dim value As System.Boolean
 
instance.UseOtherSide = value
 
value = instance.UseOtherSide
```

```

System.bool UseOtherSide {get; set;}
```

```

property System.bool UseOtherSide {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to apply the weld bead to both sides, false to not

Remarks

This property is valid, and optional, for full length and intermittent weld beads only. Use [IWeldmentBeadFeatureData::BeadType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadType.md) to determine the type of weld bead.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)
