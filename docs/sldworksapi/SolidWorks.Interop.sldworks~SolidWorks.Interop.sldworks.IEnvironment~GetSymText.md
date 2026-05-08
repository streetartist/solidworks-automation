# GetSymText Method (IEnvironment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymText`

Gets an array containing the text associated with the specified geometric tolerance symbol.
Gets an array containing the text associated with the specified geometric tolerance symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymText( _
   ByVal SymId As System.String _
) As System.Object
```

```

Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object
 
value = instance.GetSymText(SymId)
```

```

System.object GetSymText( 
   System.string SymId
)
```

```

System.Object^ GetSymText( 
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

You can use [IEnvironment::GetSymEdgeCounts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts.md) to determine how many text strings are in the specified geometric tolerance symbol. For example, passing <MOD-MMC> in SymID returns one text string ("M") and one circle.

The format of the return data is an array of strings. The size of the array returned is based on the number of text pieces in this symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md)  
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)
