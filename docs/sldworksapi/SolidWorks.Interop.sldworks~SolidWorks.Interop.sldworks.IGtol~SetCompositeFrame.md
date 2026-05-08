# SetCompositeFrame Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetCompositeFrame`

Obsolete. Superseded by IGtol::SetCompositeFrame2.
Obsolete. Superseded by [IGtol::SetCompositeFrame2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetCompositeFrame2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCompositeFrame( _
   ByVal Composite As System.Boolean _
) 
```

```

Dim instance As IGtol
Dim Composite As System.Boolean
 
instance.SetCompositeFrame(Composite)
```

```

void SetCompositeFrame( 
   System.bool Composite
)
```

```

void SetCompositeFrame( 
   System.bool Composite
) 
```

#### Parameters

*Composite*
:   True to put the first two frames of this Gtol into a composite frame, false to not

Remarks

Sets whether to put the first two frames of this Gtol into a composite frame.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetCompositeFrame Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetCompositeFrame.md)
