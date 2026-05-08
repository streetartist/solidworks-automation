# SortMethod Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~SortMethod`

Gets and sets the method for sorting the BOM table.
Gets and sets the method for sorting the BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SortMethod As System.Integer
```

```

Dim instance As IBomTableSortData
Dim value As System.Integer
 
instance.SortMethod = value
 
value = instance.SortMethod
```

```

System.int SortMethod {get; set;}
```

```

property System.int SortMethod {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Sort method as defined by [swBomTableSortMethod\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBomTableSortMethod_e.html)

Example

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)  
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.md)
