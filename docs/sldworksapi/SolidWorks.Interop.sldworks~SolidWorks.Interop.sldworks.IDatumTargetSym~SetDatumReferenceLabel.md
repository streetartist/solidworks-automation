# SetDatumReferenceLabel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumReferenceLabel`

Sets the specified datum target reference label.
Sets the specified datum target reference label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDatumReferenceLabel( _
   ByVal WhichOne As System.Integer, _
   ByVal Text As System.String _
) As System.Boolean
```

```

Dim instance As IDatumTargetSym
Dim WhichOne As System.Integer
Dim Text As System.String
Dim value As System.Boolean
 
value = instance.SetDatumReferenceLabel(WhichOne, Text)
```

```

System.bool SetDatumReferenceLabel( 
   System.int WhichOne,
   System.string Text
)
```

```

System.bool SetDatumReferenceLabel( 
   System.int WhichOne,
   System.String^ Text
) 
```

#### Parameters

*WhichOne*
:   0-based index indicating the datum reference label to set

*Text*
:   Datum reference label

#### Return Value

True if the datum reference label is set successfully, false if it was not

Remarks

Use [IDatumTargetSym::GetDatumReferenceLabel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDatumReferenceLabel.md) to get the datum target reference labels.

To see the change in a drawing, call [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Example

[Insert and Modify Datum Target Symbol (C#)](Insert_and_Modify_Datum_Target_Symbol_Example_CSharp.htm)  
[Insert and Modify Datum Target Symbol (VB.NET)](Insert_and_Modify_Datum_Target_Symbol_Example_VBNET.htm)  
[Insert and Modify Datum Target Symbol (VBA)](Insert_and_Modify_Datum_Target_Symbol_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)
