# GetIsBound Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetIsBound`

Gets whether the specified geometric tolerance symbol is bound.
Gets whether the specified geometric tolerance symbol is bound.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetIsBound( _
   ByVal SymId As System.String, _
   ByRef Retval As System.Boolean _
) 
```

```

Dim instance As IEnvironment
Dim SymId As System.String
Dim Retval As System.Boolean
 
instance.GetIsBound(SymId, Retval)
```

```

void GetIsBound( 
   System.string SymId,
   out System.bool Retval
)
```

```

void GetIsBound( 
   System.String^ SymId,
   [Out] System.bool Retval
) 
```

#### Parameters

*SymId*
:   Name of the geometric tolerance symbol formatted as:

    <*LibraryName-SymbolName*>

    where *LibraryName* and *SymbolName* are in the SOLIDWORKS text file **C:\ProgramData\SolidWorks\SolidWorks 20***nn*\**lang**\**english\gtol.sym****.**

    NOTE: You must include the right- and left-angle brackets and separate *LibraryName* and *SymbolName* with a hyphen; for example, <MOD-DEG>.

*Retval*
:   True if the geometric tolerance symbol is bound, false if not

Remarks

Bound controls the horizontal spacing of a geometric tolerance symbol within a row of text in notes and dimensions.

Example

See the [IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.md)  
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.md)
