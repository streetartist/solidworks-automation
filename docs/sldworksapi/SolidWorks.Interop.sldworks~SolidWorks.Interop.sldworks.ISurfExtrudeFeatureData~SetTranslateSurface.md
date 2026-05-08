# SetTranslateSurface Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetTranslateSurface`

Sets the translate surface setting for this extruded surface.
Sets the translate surface setting for this extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTranslateSurface( _
   ByVal Fwd As System.Boolean, _
   ByVal Trans As System.Boolean _
) 
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Fwd As System.Boolean
Dim Trans As System.Boolean
 
instance.SetTranslateSurface(Fwd, Trans)
```

```

void SetTranslateSurface( 
   System.bool Fwd,
   System.bool Trans
)
```

```

void SetTranslateSurface( 
   System.bool Fwd,
   System.bool Trans
) 
```

#### Parameters

*Fwd*
:   True sets the translate surface setting in the forward direction, false sets it in the reverse direction

*Trans*
:   True enables the translate surface setting, false disables it

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::GetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetTranslateSurface.md)
