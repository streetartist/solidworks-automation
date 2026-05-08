# SetReverseOffset Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetReverseOffset`

Sets the reverse offset direction setting for the end condition of this extruded surface.
Sets the reverse offset direction setting for the end condition of this extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetReverseOffset( _
   ByVal Fwd As System.Boolean, _
   ByVal RevOffset As System.Boolean _
) 
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Fwd As System.Boolean
Dim RevOffset As System.Boolean
 
instance.SetReverseOffset(Fwd, RevOffset)
```

```

void SetReverseOffset( 
   System.bool Fwd,
   System.bool RevOffset
)
```

```

void SetReverseOffset( 
   System.bool Fwd,
   System.bool RevOffset
) 
```

#### Parameters

*Fwd*
:   True sets the reverse offset setting in the forward direction, false sets it in the reverse direction

*RevOffset*
:   True enables the reverse offset setting, false disables it

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::GetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetReverseOffset.md)
