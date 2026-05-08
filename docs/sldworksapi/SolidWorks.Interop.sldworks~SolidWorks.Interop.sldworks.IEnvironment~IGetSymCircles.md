# IGetSymCircles Method (IEnvironment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymCircles`

Gets an array that defines all circles in the specified geometric tolerance symbol.
Gets an array that defines all circles in the specified geometric tolerance symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSymCircles( _
   ByVal SymId As System.String _
) As System.Double
```

```

Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Double
 
value = instance.IGetSymCircles(SymId)
```

```

System.double IGetSymCircles( 
   System.string SymId
)
```

```

System.double IGetSymCircles( 
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

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Each circle in the symbol is defined by its radius and center point. The size of the array returned is based on the number of circles within this geometric tolerance symbol. You can determine this number using the return value circle count from [IEnvironment::IGetSymEdgeCounts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymEdgeCounts.md).

The format of return value is the following array of doubles (in this example, for the *i*th circle):

> retval[4 \* i] = radius
>
> retval[4 \* i + 1] = x coordinate of center point
>
> retval[4 \* i + 2] = y coordinate of center point
>
> retval[4 \* i + 3] = z coordinate of center point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md)  
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)  
[IEnvironment::GetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymCircles.md)
