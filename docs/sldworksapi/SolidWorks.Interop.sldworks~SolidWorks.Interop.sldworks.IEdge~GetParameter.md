# GetParameter Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetParameter`

Gets the parameterization of the edge.
Gets the parameterization of the edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetParameter( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As IEdge
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.GetParameter(X, Y, Z)
```

```

System.object GetParameter( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ GetParameter( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X value

*Y*
:   Y value

*Z*
:   Z value

#### Return Value

Array containing parameterization of the edge

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
[IEdge::IGetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetParameter.md)
