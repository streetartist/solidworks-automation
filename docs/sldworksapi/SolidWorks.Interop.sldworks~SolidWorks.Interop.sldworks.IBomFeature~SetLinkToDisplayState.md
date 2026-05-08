# SetLinkToDisplayState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~SetLinkToDisplayState`

Sets the name of the Display State to which to link this BOM feature.
Sets the name of the Display State to which to link this BOM feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLinkToDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Integer
```

```

Dim instance As IBomFeature
Dim DisplayStateName As System.String
Dim value As System.Integer
 
value = instance.SetLinkToDisplayState(DisplayStateName)
```

```

System.int SetLinkToDisplayState( 
   System.string DisplayStateName
)
```

```

System.int SetLinkToDisplayState( 
   System.String^ DisplayStateName
) 
```

#### Parameters

*DisplayStateName*
:   Name of the Display State to link to the BOM

#### Return Value

Return code as defined by [swLinkBomToDisplayStateError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLinkBomToDisplayStateError_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::GetLinkToDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetLinkToDisplayState.md)
