# GetDatumReferenceLabel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDatumReferenceLabel`

Gets the specified datum target reference label.
Gets the specified datum target reference label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumReferenceLabel( _
   ByVal WhichOne As System.Integer _
) As System.String
```

```

Dim instance As IDatumTargetSym
Dim WhichOne As System.Integer
Dim value As System.String
 
value = instance.GetDatumReferenceLabel(WhichOne)
```

```

System.string GetDatumReferenceLabel( 
   System.int WhichOne
)
```

```

System.String^ GetDatumReferenceLabel( 
   System.int WhichOne
) 
```

#### Parameters

*WhichOne*
:   0-based index indicating the datum reference label to get

#### Return Value

Datum reference label

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
[IDatumTargetSym::SetDatumReferenceLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumReferenceLabel.md)
