# RevisionTable Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~RevisionTable`

Gets the revision table annotation for this drawing sheet.
Gets the revision table annotation for this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property RevisionTable As RevisionTableAnnotation
```

```

Dim instance As ISheet
Dim value As RevisionTableAnnotation
 
value = instance.RevisionTable
```

```

RevisionTableAnnotation RevisionTable {get;}
```

```

property RevisionTableAnnotation^ RevisionTable {
   RevisionTableAnnotation^ get();
}
```

#### Property Value

[Revision table annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)

Example

[Get Revision Table Annotation (VBA)](Get_Revision_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::InsertRevisionTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertRevisionTable.md)
