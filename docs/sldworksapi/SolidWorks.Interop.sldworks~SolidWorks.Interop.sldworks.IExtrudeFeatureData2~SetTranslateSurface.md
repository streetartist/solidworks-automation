# SetTranslateSurface Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetTranslateSurface`

Sets the translate surface setting for this extrude feature.
Sets the translate surface setting for this extrude feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTranslateSurface( _
   ByVal Fwd As System.Boolean, _
   ByVal ValIn As System.Boolean _
) 
```

```

Dim instance As IExtrudeFeatureData2
Dim Fwd As System.Boolean
Dim ValIn As System.Boolean
 
instance.SetTranslateSurface(Fwd, ValIn)
```

```

void SetTranslateSurface( 
   System.bool Fwd,
   System.bool ValIn
)
```

```

void SetTranslateSurface( 
   System.bool Fwd,
   System.bool ValIn
) 
```

#### Parameters

*Fwd*
:   True makes the end of the extrusion a translation of the reference surface in the forward direction, false makes the end of the extrusion a translation of the reference surface in the reverse direction

*ValIn*
:   True to enable the translate surface setting, false to disable it

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::GetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetTranslateSurface.md)  
[IExtrudeFeatureData2::GetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetReverseOffset.md)  
[IExtrudeFeatureData2::SetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetReverseOffset.md)  
[IExtrudeFeatureData2::FromOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance.md)  
[IExtrudeFeatureData2::FromOffsetReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.md)
