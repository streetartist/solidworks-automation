# PrintOut Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut`

Obsolete. Superseded by IModelDocExtension::PrintOut2.
Obsolete. Superseded by [IModelDocExtension::PrintOut2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PrintOut( _
   ByVal FromPage As System.Integer, _
   ByVal ToPage As System.Integer, _
   ByVal Copies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String _
) 
```

```

Dim instance As IModelDocExtension
Dim FromPage As System.Integer
Dim ToPage As System.Integer
Dim Copies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim PrintFileName As System.String
 
instance.PrintOut(FromPage, ToPage, Copies, Collate, Printer, PrintFileName)
```

```

void PrintOut( 
   System.int FromPage,
   System.int ToPage,
   System.int Copies,
   System.bool Collate,
   System.string Printer,
   System.string PrintFileName
)
```

```

void PrintOut( 
   System.int FromPage,
   System.int ToPage,
   System.int Copies,
   System.bool Collate,
   System.String^ Printer,
   System.String^ PrintFileName
) 
```

#### Parameters

*FromPage*

*ToPage*

*Copies*

*Collate*

*Printer*

*PrintFileName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
