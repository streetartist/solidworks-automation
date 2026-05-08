# GetDesignTable Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDesignTable`

Gets the design table associated with this part or assembly document.
Gets the design table associated with this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDesignTable() As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.GetDesignTable()
```

```

System.object GetDesignTable()
```

```

System.Object^ GetDesignTable(); 
```

#### Return Value

[Design table](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)

Remarks

If you call this method from a drawing document, null or Nothing is returned.

To access design tables from a drawing document you must get the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object associated with a particular drawing view and then call this method from that IModelDoc2 object. To determine if a drawing view has a design table associated with it, use [IView::HasDesignTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~HasDesignTable.md).

Example

[Add Row to Design Table (VBA)](Add_Row_to_Design_Table_Example_VB.htm)  
[Get Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)  
[Get or Set Whether Edits Update Design Table (VBA)](Get_or_Set_Whether_Edits_Update_Design_Table_Example_VB.htm)  
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)  
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)  
[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CloseFamilyTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CloseFamilyTable.md)  
[IModelDoc2::DeleteDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteDesignTable.md)  
[IModelDoc2::InsertFamilyTableEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableEdit.md)  
[IModelDoc2::InsertFamilyTableNew Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableNew.md)  
[IModelDoc2::InsertFamilyTableOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableOpen.md)  
[IModelDocExtension::HasDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasDesignTable.md)  
[IModelDoc2::IGetDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetDesignTable.md)  
[IModelDoc2::GetDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDesignTable.md)  
[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)
