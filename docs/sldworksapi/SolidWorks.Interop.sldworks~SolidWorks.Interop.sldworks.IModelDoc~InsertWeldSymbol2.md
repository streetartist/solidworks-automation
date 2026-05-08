# InsertWeldSymbol2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertWeldSymbol2`

Obsolete. Superseded by IModelDoc2::InsertWeldSymbol2.
Obsolete. Superseded by [IModelDoc2::InsertWeldSymbol2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertWeldSymbol2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertWeldSymbol2( _
   ByVal Dim1 As System.String, _
   ByVal Symbol As System.String, _
   ByVal Dim2 As System.String, _
   ByVal Symmetric As System.Boolean, _
   ByVal FieldWeld As System.Boolean, _
   ByVal ShowOtherSide As System.Boolean, _
   ByVal DashOnTop As System.Boolean, _
   ByVal Peripheral As System.Boolean, _
   ByVal HasProcess As System.Boolean, _
   ByVal ProcessValue As System.String _
) 
```

```

Dim instance As IModelDoc
Dim Dim1 As System.String
Dim Symbol As System.String
Dim Dim2 As System.String
Dim Symmetric As System.Boolean
Dim FieldWeld As System.Boolean
Dim ShowOtherSide As System.Boolean
Dim DashOnTop As System.Boolean
Dim Peripheral As System.Boolean
Dim HasProcess As System.Boolean
Dim ProcessValue As System.String
 
instance.InsertWeldSymbol2(Dim1, Symbol, Dim2, Symmetric, FieldWeld, ShowOtherSide, DashOnTop, Peripheral, HasProcess, ProcessValue)
```

```

void InsertWeldSymbol2( 
   System.string Dim1,
   System.string Symbol,
   System.string Dim2,
   System.bool Symmetric,
   System.bool FieldWeld,
   System.bool ShowOtherSide,
   System.bool DashOnTop,
   System.bool Peripheral,
   System.bool HasProcess,
   System.string ProcessValue
)
```

```

void InsertWeldSymbol2( 
   System.String^ Dim1,
   System.String^ Symbol,
   System.String^ Dim2,
   System.bool Symmetric,
   System.bool FieldWeld,
   System.bool ShowOtherSide,
   System.bool DashOnTop,
   System.bool Peripheral,
   System.bool HasProcess,
   System.String^ ProcessValue
) 
```

#### Parameters

*Dim1*

*Symbol*

*Dim2*

*Symmetric*

*FieldWeld*

*ShowOtherSide*

*DashOnTop*

*Peripheral*

*HasProcess*

*ProcessValue*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
