# SetIgesInfo Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetIgesInfo`

Sends IGES-specific data to the geometric modeler.
Sends IGES-specific data to the geometric modeler.

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

Dim instance As IBody2
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
:   Name of the system as defined in [swIGESPreferredSystem\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swIGESPreferredSystem_e.html)

*Granularity*
:   Level of granularity

*AttemptKnitting*
:   True knits the objects, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
