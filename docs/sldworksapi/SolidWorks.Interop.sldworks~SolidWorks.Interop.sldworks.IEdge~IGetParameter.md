# IGetParameter Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetParameter`

Gets the parameterization of the edge.
Gets the parameterization of the edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetParameter( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

```

Dim instance As IEdge
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double
 
value = instance.IGetParameter(X, Y, Z)
```

```

System.double IGetParameter( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.double IGetParameter( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X value

*Y*
:   Y value

*Z*
:   Z value

#### Return Value

Pointer to an array of doubles (see **Remarks**)

Remarks

This method returns an array of 2 doubles:

- retval[0] - Parametric value of the specified point
- retval[1] - BOOL value; True for success, false for failure

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetParameter.md)
