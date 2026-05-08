# GetLeader Method (ICallout)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetLeader`

Gets the leader properties of the callout.
Gets the leader properties of the callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLeader( _
   ByRef Visible As System.Boolean, _
   ByRef Multiple As System.Boolean _
) As System.Boolean
```

```

Dim instance As ICallout
Dim Visible As System.Boolean
Dim Multiple As System.Boolean
Dim value As System.Boolean
 
value = instance.GetLeader(Visible, Multiple)
```

```

System.bool GetLeader( 
   out System.bool Visible,
   out System.bool Multiple
)
```

```

System.bool GetLeader( 
   [Out] System.bool Visible,
   [Out] System.bool Multiple
) 
```

#### Parameters

*Visible*
:   True if leader is displayed, false if not (see **Remarks**)

*Multiple*
:   True if multiple leaders are displayed, false if not

Remarks

If Visible is false, then [ICallout::TargetStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~TargetStyle.md) is swCalloutTargetStyle\_None.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)  
[ICallout::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetLeader.md)
