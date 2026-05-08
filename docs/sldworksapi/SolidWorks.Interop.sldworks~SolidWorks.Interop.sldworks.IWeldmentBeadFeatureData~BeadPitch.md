# BeadPitch Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadPitch`

Gets or sets the distance between the start of each weld bead.
Gets or sets the distance between the start of each weld bead.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BeadPitch( _
   ByVal Side As System.Integer _
) As System.Double
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim value As System.Double
 
instance.BeadPitch(Side) = value
 
value = instance.BeadPitch(Side)
```

```

System.double BeadPitch( 
   System.int Side
) {get; set;}
```

```

property System.double BeadPitch {
   System.double get(System.int Side);
   void set (System.int Side, System.double value);
}
```

#### Parameters

*Side*
:   Side as defined by [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

#### Property Value

Pitch

Remarks

This property is only valid for intermittent or staggered types of weld beads. Use [IWeldmentBeadFeatureData::BeadType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadType.md) to determine the type of weld bead.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)
