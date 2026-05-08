# GetTargetAreaSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetAreaSize`

Gets the size of the datum target symbol area.
Gets the size of the datum target symbol area.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTargetAreaSize( _
   ByVal WhichOne As System.Integer _
) As System.String
```

```

Dim instance As IDatumTargetSym
Dim WhichOne As System.Integer
Dim value As System.String
 
value = instance.GetTargetAreaSize(WhichOne)
```

```

System.string GetTargetAreaSize( 
   System.int WhichOne
)
```

```

System.String^ GetTargetAreaSize( 
   System.int WhichOne
) 
```

#### Parameters

*WhichOne*
:   0-based index indicating which size value to get (see [Remarks](#Remarks))

#### Return Value

Target area size (see Remarks)

Remarks

Use [IDatumTargetSym::GetTargetShape](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetShape.md) to get the style for the target area.

|  |  |
| --- | --- |
| **If the target area style for this symbol is a ...** | **Then...** |
| Point | There is one size value, which might be empty. Retrieve the text using an index value of 0. SOLIDWORKS displays the text in the upper half of the symbol, preceded by a diameter character. |
| Circle | There is one size value. Retrieve the text using an index value of 0. SOLIDWORKS displays the text in the upper half of the symbol, preceded by a diameter character. |
| Rectangle | There are two size values. Retrieve the text using an index value of 0 and 1. SOLIDWORKS displays the texts in the upper half of the symbol, separated by an x character. |

Use [IDatumTargetSym::SetTargetArea](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetTargetArea.md) to set the target area size.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)  
[IDatumTargetSym::GetDisplayTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.md)  
[IDatumTargetSym::SetTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetTargetArea.md)
