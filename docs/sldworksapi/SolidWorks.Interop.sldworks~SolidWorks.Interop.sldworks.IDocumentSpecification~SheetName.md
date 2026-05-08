# SheetName Property (IDocumentSpecification)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~SheetName`

Gets or sets the name of the sheet in a drawing document to open.
Gets or sets the name of the sheet in a drawing document to open.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SheetName As System.String
```

```

Dim instance As IDocumentSpecification
Dim value As System.String
 
instance.SheetName = value
 
value = instance.SheetName
```

```

System.string SheetName {get; set;}
```

```

property System.String^ SheetName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Sheet name

Example

[Open Specified Sheet in Drawing Document (VB.NET)](Open_Specified_Sheet_in_Drawing_Document_Example_VBNET.htm)  
[Open Specified Sheet in Drawing Document (VBA)](Open_Specified_Sheet_in_Drawing_Document_Example_VB.htm)  
[Open Specified Sheet in Drawing Document (C#)](Open_Specified_Sheet_in_Drawing_Document_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
