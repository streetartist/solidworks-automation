# GetSymEdgeCounts Method (IEnvironment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts`

Gets an array that contains the number of lines, arcs, circles, text strings, and triangles in the specified geometric tolerance symbol.
Gets an array that contains the number of lines, arcs, circles, text strings, and triangles in the specified geometric tolerance symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymEdgeCounts( _
   ByVal SymId As System.String _
) As System.Object
```

```

Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object
 
value = instance.GetSymEdgeCounts(SymId)
```

```

System.object GetSymEdgeCounts( 
   System.string SymId
)
```

```

System.Object^ GetSymEdgeCounts( 
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

Format of return information is the following array of short integers:

retval[0] = line count

retval[1] = arc count

retval[2] = circle count

retval[3] = text count

retval[4] = triangle count

Example

See the [IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md)  
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)  
[IEnvironment::IGetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymEdgeCounts.md)  
[IEnvironment::GetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymArcs.md)  
[IEnvironment::GetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymCircles.md)  
[IEnvironment::GetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymLines.md)  
[IEnvironment::GetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymText.md)  
[IEnvironment::GetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymTextPoints.md)  
[IEnvironment::GetSymTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTriangles.md)
