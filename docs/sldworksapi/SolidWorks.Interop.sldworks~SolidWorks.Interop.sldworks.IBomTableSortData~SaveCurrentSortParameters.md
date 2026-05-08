# SaveCurrentSortParameters Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~SaveCurrentSortParameters`

Gets and sets whether to save the current sort settings in the BOM table in the drawing.
Gets and sets whether to save the current sort settings in the BOM table in the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SaveCurrentSortParameters As System.Boolean
```

```

Dim instance As IBomTableSortData
Dim value As System.Boolean
 
instance.SaveCurrentSortParameters = value
 
value = instance.SaveCurrentSortParameters
```

```

System.bool SaveCurrentSortParameters {get; set;}
```

```

property System.bool SaveCurrentSortParameters {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to save the current sort settings in the BOM table, false to not

Remarks

After setting this property to true, you must call [IBomTableAnnotation::Sort](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Sort.md) to actually save the sort settings in the BOM table in the drawing. Thereafter, instead of setting all of the sorting parameters every time you instantiate a new IBomTableAnnotation for this table, you can simply call [IBomTableAnnotation::ApplySavedSortScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~ApplySavedSortScheme.md) to re-sort the table using the sort settings saved in the BOM table.

Example

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)  
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.md)
