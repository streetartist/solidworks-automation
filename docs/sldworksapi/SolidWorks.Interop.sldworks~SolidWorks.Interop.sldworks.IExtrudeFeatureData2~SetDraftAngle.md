# SetDraftAngle Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftAngle`

Sets the draft angle of the extrusion in the forward or reverse direction.
Sets the draft angle of the extrusion in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDraftAngle( _
   ByVal Forward As System.Boolean, _
   ByVal DraftAngle As System.Double _
) 
```

```

Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim DraftAngle As System.Double
 
instance.SetDraftAngle(Forward, DraftAngle)
```

```

void SetDraftAngle( 
   System.bool Forward,
   System.double DraftAngle
)
```

```

void SetDraftAngle( 
   System.bool Forward,
   System.double DraftAngle
) 
```

#### Parameters

*Forward*
:   True for forward direction, false for reverse

*DraftAngle*
:   Draft angle of the extrusion in radians

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudedFeatureData2::GetDraftAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftAngle.md)  
[IExtrudedFeatureData2::GetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftOutward.md)  
[IExtrudedFeatureData2::GetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDraftWhileExtruding.md)  
[IExtrudedFeatureData2::SetDraftOutward Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftOutward.md)  
[IExtrudedFeatureData2::SetDraftWhileExtruding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDraftWhileExtruding.md)
