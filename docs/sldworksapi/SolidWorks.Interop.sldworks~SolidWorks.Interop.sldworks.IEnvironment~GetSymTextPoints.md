# GetSymTextPoints Method (IEnvironment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymTextPoints`

Gets an array that defines all text points in the specified geometric tolerance symbol.
Gets an array that defines all text points in the specified geometric tolerance symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymTextPoints( _
   ByVal SymId As System.String _
) As System.Object
```

```

Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object
 
value = instance.GetSymTextPoints(SymId)
```

```

System.object GetSymTextPoints( 
   System.string SymId
)
```

```

System.Object^ GetSymTextPoints( 
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

The size of the array returned is based on the number of text pieces within this geometric tolerance symbol. You can determine this number using the return value text count from [IEnvironment::GetSymEdgeCounts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts.md).

The return value is an array of doubles as follows:

retval[0] x coordinate of text 1

retval[1] y coordinate of text 1

retval[2] z coordinate of text 1

retval[3] x coordinate of text 2

retval[4] y coordinate of text 2

retval[5] z coordinate of text 2

retval[ (n\*3-3)] X coordinate of text n

retval[ (n\*3-2)] Y coordinate of text n

retval[ (n\*3-1)] Z coordinate of text n

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md)  
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)  
[IEnvironment::IGetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTextPoints.md)
