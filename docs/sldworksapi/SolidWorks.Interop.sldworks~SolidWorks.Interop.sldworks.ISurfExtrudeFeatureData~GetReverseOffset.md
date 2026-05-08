# GetReverseOffset Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetReverseOffset`

Gets the reverse offset direction setting for the end condition of this extruded surface.
Gets the reverse offset direction setting for the end condition of this extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReverseOffset( _
   ByVal Fwd As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Fwd As System.Boolean
Dim value As System.Boolean
 
value = instance.GetReverseOffset(Fwd)
```

```

System.bool GetReverseOffset( 
   System.bool Fwd
)
```

```

System.bool GetReverseOffset( 
   System.bool Fwd
) 
```

#### Parameters

*Fwd*
:   True gets the reverse offset setting in the forward direction, false gets it in the reverse direction

#### Return Value

True if the reverse offset setting is enabled, false if it is disabled

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::SetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetReverseOffset.md)
