# SetPTZHeight Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetPTZHeight`

Obsolete. Superseded by IGtol::SetPTZHeight2.
Obsolete. Superseded by [IGtol::SetPTZHeight2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetPTZHeight( _
   ByVal PtzHt As System.String, _
   ByVal DisplayIn As System.Boolean _
) 
```

```

Dim instance As IGtol
Dim PtzHt As System.String
Dim DisplayIn As System.Boolean
 
instance.SetPTZHeight(PtzHt, DisplayIn)
```

```

void SetPTZHeight( 
   System.string PtzHt,
   System.bool DisplayIn
)
```

```

void SetPTZHeight( 
   System.String^ PtzHt,
   System.bool DisplayIn
) 
```

#### Parameters

*PtzHt*
:   Height of the projected tolerance zone

*DisplayIn*
:   True to display the projected zone tolerance, false to not

Remarks

The projected tolerance zone (PTZ) displays in the first tolerance window of the first control frame of the GTol. If PtzHt is not empty, its value is displayed after the PTZ symbol, which is a P enclosed in a circle.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetPTZHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetPTZHeight.md)
