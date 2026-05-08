# PrintOut2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~PrintOut2`

Obsolete. Superseded by IModelDoc2::PrintOut2.
Obsolete. Superseded by [IModelDoc2::PrintOut2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintOut2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PrintOut2( _
   ByVal FromPage As System.Integer, _
   ByVal ToPage As System.Integer, _
   ByVal NumCopies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal Scale As System.Double, _
   ByVal PrintToFile As System.Boolean, _
   ByVal PtfName As System.String _
) 
```

```

Dim instance As IModelDoc
Dim FromPage As System.Integer
Dim ToPage As System.Integer
Dim NumCopies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim Scale As System.Double
Dim PrintToFile As System.Boolean
Dim PtfName As System.String
 
instance.PrintOut2(FromPage, ToPage, NumCopies, Collate, Printer, Scale, PrintToFile, PtfName)
```

```

void PrintOut2( 
   System.int FromPage,
   System.int ToPage,
   System.int NumCopies,
   System.bool Collate,
   System.string Printer,
   System.double Scale,
   System.bool PrintToFile,
   System.string PtfName
)
```

```

void PrintOut2( 
   System.int FromPage,
   System.int ToPage,
   System.int NumCopies,
   System.bool Collate,
   System.String^ Printer,
   System.double Scale,
   System.bool PrintToFile,
   System.String^ PtfName
) 
```

#### Parameters

*FromPage*

*ToPage*

*NumCopies*

*Collate*

*Printer*

*Scale*

*PrintToFile*

*PtfName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
