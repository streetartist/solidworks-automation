# GetSymArcs Method (IEnvironment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymArcs`

Obsolete. Superseded by IEnvironment::GetSymArcs2.
Obsolete. Superseded by [IEnvironment::GetSymArcs2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymArcs2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymArcs( _
   ByVal SymId As System.String _
) As System.Object
```

```

Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object
 
value = instance.GetSymArcs(SymId)
```

```

System.object GetSymArcs( 
   System.string SymId
)
```

```

System.Object^ GetSymArcs( 
   System.String^ SymId
) 
```

#### Parameters

*SymId*
:   Name of the geometric tolerance symbol formatted as:

    <LibraryName-SymbolName>

    where LibraryName and SymbolName are a [pre-defined SOLIDWORKS symbol](sldworksAPIProgGuide.chm::/Miscellaneous/Geometric_Tolerance_Symbol_Libraries.htm) in the SOLIDWORKS text file **gtol.sym**, typically installed at **C:\ProgramData\SolidWorks\SolidWorks 20***nn*\**lang**\**english****.**

    NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.

#### Return Value

Array (see **Remarks**)

Remarks

Each arc in the geometric tolerance symbol is defined by three points (center, arc start, and end). The size of the array returned is based on the number of arcs within this geometric tolerance symbol. You can determine this number using the return value arc count from [IEnvironment::GetSymEdgeCounts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts.md).

The format of return value is the following array of doubles (in this example, for the *i*th arc):

retval[9 \* i + 0] = x coordinate of center point

retval[9 \* i + 1] = y coordinate of center point

retval[9 \* i + 2] = z coordinate of center point

retval[9 \* i + 3] = x coordinate of arc start point

retval[9 \* i + 4] = y coordinate of arc start point

retval[9 \* i + 5] = z coordinate of arc start point

retval[9 \* i + 6] = x coordinate of arc end point

retval[9 \* i + 7] = y coordinate of arc end point

retval[9 \* i + 8] = z coordinate of arc end point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md)  
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)  
[IEnvironment::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymArcs.md)
