# SetMinimumAcceptableClearance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetMinimumAcceptableClearance`

Sets the minimum acceptable clearance value.
Sets the minimum acceptable clearance value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMinimumAcceptableClearance( _
   ByVal Value As System.Double _
) As System.Boolean
```

```

Dim instance As IClearanceVerificationMgr
Dim Value As System.Double
Dim value As System.Boolean
 
value = instance.SetMinimumAcceptableClearance(Value)
```

```

System.bool SetMinimumAcceptableClearance( 
   System.double Value
)
```

```

System.bool SetMinimumAcceptableClearance( 
   System.double Value
) 
```

#### Parameters

*Value*
:   Minimum acceptable clearance value

#### Return Value

True if minimum acceptable clearance value successfuly set, false if not

Example

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md)  
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.md)  
[IClearanceVerificationMgr::IgnoreClearanceEqualToSpecifiedValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~IgnoreClearanceEqualToSpecifiedValue.md)
