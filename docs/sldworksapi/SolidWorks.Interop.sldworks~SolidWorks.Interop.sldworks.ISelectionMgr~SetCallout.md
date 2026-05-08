# SetCallout Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetCallout`

Adds a callout to the currently selected object.
Adds a callout to the currently selected object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCallout( _
   ByVal Index As System.Integer, _
   ByVal PCallout As Callout _
) As System.Boolean
```

```

Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim PCallout As Callout
Dim value As System.Boolean
 
value = instance.SetCallout(Index, PCallout)
```

```

System.bool SetCallout( 
   System.int Index,
   Callout PCallout
)
```

```

System.bool SetCallout( 
   System.int Index,
   Callout^ PCallout
) 
```

#### Parameters

*Index*
:   Index number of the selected object

*PCallout*
:   [Callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md) (see **Remarks**)

#### Return Value

True if the callout is added to the selected object, false if not

Remarks

Use [ISelectionMgr::CreateCallout2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateCallout2.md) to set the properties of the callout. Then use ISelectionMgr::SetCallout to add the callout to an already selected object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
