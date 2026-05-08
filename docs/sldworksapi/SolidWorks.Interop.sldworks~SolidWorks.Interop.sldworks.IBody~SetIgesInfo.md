# SetIgesInfo Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~SetIgesInfo`

Obsolete. Superseded by IBody2::SetIgesetInfo.
Obsolete. Superseded by [IBody2::SetIgesetInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetIgesInfo.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetIgesInfo( _
   ByVal SystemName As System.String, _
   ByVal Granularity As System.Double, _
   ByVal AttemptKnitting As System.Boolean _
) 
```

```

Dim instance As IBody
Dim SystemName As System.String
Dim Granularity As System.Double
Dim AttemptKnitting As System.Boolean
 
instance.SetIgesInfo(SystemName, Granularity, AttemptKnitting)
```

```

void SetIgesInfo( 
   System.string SystemName,
   System.double Granularity,
   System.bool AttemptKnitting
)
```

```

void SetIgesInfo( 
   System.String^ SystemName,
   System.double Granularity,
   System.bool AttemptKnitting
) 
```

#### Parameters

*SystemName*

*Granularity*

*AttemptKnitting*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
