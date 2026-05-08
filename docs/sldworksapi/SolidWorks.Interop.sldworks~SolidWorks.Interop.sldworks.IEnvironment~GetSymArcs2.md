# GetSymArcs2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymArcs2`

Gets an array of information about all arcs in the specified geometric tolerance symbol.
Gets an array of information about all arcs in the specified geometric tolerance symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymArcs2( _
   ByVal SymId As System.String _
) As System.Object
```

```

Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object
 
value = instance.GetSymArcs2(SymId)
```

```

System.object GetSymArcs2( 
   System.string SymId
)
```

```

System.Object^ GetSymArcs2( 
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

Each arc in the geometric tolerance symbol is defined by three points (center, arc start, and arc end), whether the arc is filled, and whether the chord joining the start and end points is drawn. The size of the array returned is based on the number of arcs within this geometric tolerance symbol. You can determine this number by calling [IEnvironment::GetSymEdgeCounts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts.md).

The return value contains the following array for each arc:

[ x coordinate of center point,

  y coordinate of center point,

  z coordinate of center point,

  x coordinate of start point,

  y coordinate of start point,

  z coordinate of start point,

  x coordinate of end point,

  y coordinate of end point,

  z coordinate of end point,

  whether arch is filled,

  whether the chord joining the start and end points is drawn ]

Example

See the [IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md)  
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)
