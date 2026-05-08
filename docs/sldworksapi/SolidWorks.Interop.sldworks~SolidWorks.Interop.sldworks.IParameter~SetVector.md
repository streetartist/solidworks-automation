# SetVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector`

Obsolete. Superseded by IParameter::SetVector2.
Obsolete. Superseded by [IParameter::SetVector2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetVector( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As IParameter
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.SetVector(X, Y, Z)
```

```

System.bool SetVector( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool SetVector( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*

*Y*

*Z*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md)  
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.md)
