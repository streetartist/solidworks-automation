# SetTargetArea Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetTargetArea`

Sets the datum target area style and size.
Sets the datum target area style and size.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTargetArea( _
   ByVal Shape As System.Integer, _
   ByVal Size1 As System.String, _
   ByVal Size2 As System.String _
) As System.Boolean
```

```

Dim instance As IDatumTargetSym
Dim Shape As System.Integer
Dim Size1 As System.String
Dim Size2 As System.String
Dim value As System.Boolean
 
value = instance.SetTargetArea(Shape, Size1, Size2)
```

```

System.bool SetTargetArea( 
   System.int Shape,
   System.string Size1,
   System.string Size2
)
```

```

System.bool SetTargetArea( 
   System.int Shape,
   System.String^ Size1,
   System.String^ Size2
) 
```

#### Parameters

*Shape*
:   Target area shape or style as defined in [swDatumTargetAreaShape\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumTargetAreaShape_e.html)

*Size1*
:   Target area diameter or width (see **Remarks**)

*Size2*
:   Target area height (see Remarks)

#### Return Value

True if the target area parameters were set successfully, false if they were not

Remarks

|  |  |
| --- | --- |
| **If the target area style for this symbol is...** | **Then...** |
| Point | There is one size value, which might be empty. Retrieve the text using an index value of 0. SOLIDWORKS displays the text in the upper half of the symbol, preceded by a diameter character. |
| Circle | There is one size value. Retrieve the text using an index value of 0. SOLIDWORKS displays the text in the upper half of the symbol, preceded by a diameter character. |
| Rectangle | There are two size values. Retrieve the text using an index value of 0 and 1. SOLIDWORKS displays the texts in the upper half of the symbol, separated by an x character. |

If the specified target area style is not one of the values in swDatumTargetAreaShape\_e, SOLIDWORKS does not modify the symbol, and the returns false.

Use [IDatumTargetSym::GetTargetShape](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetShape.md) to get the target area style. Use [IDatumTargetSym::GetTargetAreaSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetAreaSize.md) to get the target area size.

To see the model or drawing changes, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw your window.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)
