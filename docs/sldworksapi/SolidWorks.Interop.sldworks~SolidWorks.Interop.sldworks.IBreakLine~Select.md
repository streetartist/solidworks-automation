# Select Method (IBreakLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Select`

Selects the break line and marks it.
Selects the break line and marks it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As IBreakLine
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.Select(Append, Data)
```

```

System.bool Select( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool Select( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True appends the break line to the selection list, false replaces the selection list with this break line

*Data*
:   Pointer to the [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the selection is successful, false if not

Example

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)  
[Create Break View (V.NET)](Create_Broken_View_Example_VBNET.htm)  
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)  
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.md)
