# IGetClosestPointOn Method (IVertex)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn`

Gets the closest point on the vertex using the X, Y, Z input point.
Gets the closest point on the vertex using the X, Y, Z input point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

```

Dim instance As IVertex
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double
 
value = instance.IGetClosestPointOn(X, Y, Z)
```

```

System.double IGetClosestPointOn( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.double IGetClosestPointOn( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X value of the input point

*Y*
:   Y value of the input point

*Z*
:   Z value of the input point

#### Return Value

- in-process, unmanaged C++: Pointer to an array of five doubles representing the X, Y, Z point on the vertex

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVertex Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)  
[IVertex Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.md)  
[IVertex::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetClosestPointOn.md)
