# BeadSize Property (IWeldmentBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadSize`

Gets or sets the length of the leg of the weld bead.
Gets or sets the length of the leg of the weld bead.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BeadSize( _
   ByVal Side As System.Integer _
) As System.Double
```

```

Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim value As System.Double
 
instance.BeadSize(Side) = value
 
value = instance.BeadSize(Side)
```

```

System.double BeadSize( 
   System.int Side
) {get; set;}
```

```

property System.double BeadSize {
   System.double get(System.int Side);
   void set (System.int Side, System.double value);
}
```

#### Parameters

*Side*
:   Side as defined by [swWeldBeadSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

#### Property Value

Length of the leg

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)
