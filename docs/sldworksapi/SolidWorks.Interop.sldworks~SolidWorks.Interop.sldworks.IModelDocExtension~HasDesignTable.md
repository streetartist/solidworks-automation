# HasDesignTable Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasDesignTable`

Gets whether a document has a design table.
Gets whether a document has a design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HasDesignTable() As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.HasDesignTable()
```

```

System.bool HasDesignTable()
```

```

System.bool HasDesignTable(); 
```

#### Return Value

True if document has a design table, false if not (see **Remarks**)

Remarks

This method always returns false for drawing documents because in drawing documents the design table is attached to the drawing view and not the document. Use [IView::HasDesignTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~HasDesignTable.md) to determine if a drawing view in a drawing document has a design table.

Example

[Delete Design Table (VBA)](Delete_Design_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
