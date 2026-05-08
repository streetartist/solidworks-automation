# GetSymTriangles Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymTriangles`

Gets an array that defines all triangles in the specified geometric tolerance symbol.
Gets an array that defines all triangles in the specified geometric tolerance symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymTriangles( _
   ByVal SymId As System.String _
) As System.Object
```

```

Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object
 
value = instance.GetSymTriangles(SymId)
```

```

System.object GetSymTriangles( 
   System.string SymId
)
```

```

System.Object^ GetSymTriangles( 
   System.String^ SymId
) 
```

#### Parameters

*SymId*
:   Name of the geometric tolerance symbol formatted as:

    <*LibraryName-SymbolName*>

    where *LibraryName* and *SymbolName* are in the SOLIDWORKS text file **C:\ProgramData\SolidWorks\SolidWorks 20***nn*\**lang**\**english\gtol.sym****.**

    NOTE: You must include the right- and left-angle brackets and separate *LibraryName* and *SymbolName* with a hyphen; for example, <MOD-DEG>.

#### Return Value

Array (see **Remarks**)

Remarks

The size of the array returned by this method is based on the number of triangles in this geometric tolerance symbol. You can determine this number using the return value triangle count from [IEnvironment::GetSymEdgeCounts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts.md).

The format of the returned data is an array of doubles:

retval[0] x coordinate of triangle point 1

retval[1] y coordinate of triangle point 1

retval[2] z coordinate of triangle point 1

retval[3] x coordinate of triangle point 2

retval[4] y coordinate of triangle point 2

retval[5] z coordinate of triangle point 2

retval[6] x coordinate of triangle point 3

retval[7] y coordinate of triangle point 3

retval[8] z coordinate of triangle point 3

retval[9] Boolean returned as a double that describes if the triangle is filled

retval[10] describes the [line type](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) of the triangle

 where this set of data repeats itself for each triangle in the specified geometric tolerance symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md)  
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)  
[IEnvironment::IGetSymTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTriangles.md)
