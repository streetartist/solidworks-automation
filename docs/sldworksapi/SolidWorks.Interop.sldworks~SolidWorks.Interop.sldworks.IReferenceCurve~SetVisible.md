# SetVisible Method (IReferenceCurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~SetVisible`

Hides or shows the reference curve feature.
Hides or shows the reference curve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetVisible( _
   ByVal Visible As System.Boolean _
) As System.Boolean
```

```

Dim instance As IReferenceCurve
Dim Visible As System.Boolean
Dim value As System.Boolean
 
value = instance.SetVisible(Visible)
```

```

System.bool SetVisible( 
   System.bool Visible
)
```

```

System.bool SetVisible( 
   System.bool Visible
) 
```

#### Parameters

*Visible*
:   True for visible, false for hidden

#### Return Value

True if set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md)  
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.md)
