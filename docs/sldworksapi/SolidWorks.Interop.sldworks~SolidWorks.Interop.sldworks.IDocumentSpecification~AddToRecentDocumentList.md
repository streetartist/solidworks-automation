# AddToRecentDocumentList Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AddToRecentDocumentList`

Gets or sets whether to add the opened document to the Recent Documents list.
Gets or sets whether to add the opened document to the Recent Documents list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AddToRecentDocumentList As System.Integer
```

```

Dim instance As IDocumentSpecification
Dim value As System.Integer
 
instance.AddToRecentDocumentList = value
 
value = instance.AddToRecentDocumentList
```

```

System.int AddToRecentDocumentList {get; set;}
```

```

property System.int AddToRecentDocumentList {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Recent Document list actions as defined by [swAddToRecentDocumentList\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddToRecentDocumentList_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
